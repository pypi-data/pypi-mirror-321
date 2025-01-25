import os
from datetime import datetime, timedelta
from importlib import import_module, metadata
from itertools import groupby
from operator import itemgetter
from types import ModuleType
from typing import Any, Callable, Dict, Optional, Sequence, Union
from warnings import warn

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files import File
from django.db.models import Model, QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.functional import lazy
from django.utils.module_loading import import_string

from cachalot.api import invalidate
from cachalot.signals import post_invalidation
from cache_memoize import cache_memoize


def copyright_years(years: Sequence[int], separator: str = ", ", joiner: str = "–") -> str:
    """Take a sequence of integers and produces a string with ranges.

    >>> copyright_years([1999, 2000, 2001, 2005, 2007, 2008, 2009])
    '1999–2001, 2005, 2007–2009'
    """
    ranges = [
        list(map(itemgetter(1), group))
        for _, group in groupby(enumerate(years), lambda e: e[1] - e[0])
    ]
    years_strs = [
        str(range_[0]) if len(range_) == 1 else joiner.join([str(range_[0]), str(range_[-1])])
        for range_ in ranges
    ]

    return separator.join(years_strs)


def get_app_packages(only_official: bool = False) -> Sequence[str]:
    """Find all registered apps from the setuptools entrypoint."""
    apps = []

    for ep in metadata.entry_points().get("aleksis.app", []):
        path = f"{ep.module}.{ep.attr}"
        if path.startswith("aleksis.apps.") or not only_official:
            apps.append(path)

    return apps


def get_app_module(app: str, name: str) -> Optional[ModuleType]:
    """Get a named module of an app."""
    pkg = ".".join(app.split(".")[:-2])

    while "." in pkg:
        try:
            return import_module(f"{pkg}.{name}")
        except ImportError:
            # Import errors are non-fatal.
            pkg = ".".join(pkg.split(".")[:-1])

    # The app does not have this module
    return None


def merge_app_settings(
    setting: str, original: Union[dict, list], deduplicate: bool = False
) -> Union[dict, list]:
    """Merge app settings.

    Get a named settings constant from all apps and merge it into the original.
    To use this, add a settings.py file to the app, in the same format as Django's
    main settings.py.

    Note: Only selected names will be imported frm it to minimise impact of
    potentially malicious apps!
    """
    for app in get_app_packages():
        mod_settings = get_app_module(app, "settings")
        if not mod_settings:
            continue

        app_setting = getattr(mod_settings, setting, None)
        if not app_setting:
            # The app might not have this setting or it might be empty. Ignore it in that case.
            continue

        for entry in app_setting:
            if entry in original:
                if not deduplicate:
                    raise AttributeError(f"{entry} already set in original.")
            else:
                if isinstance(original, list):
                    original.append(entry)
                elif isinstance(original, dict):
                    original[entry] = app_setting[entry]
                else:
                    raise TypeError("Only dict and list settings can be merged.")


def get_app_settings_overrides() -> dict[str, Any]:
    """Get app settings overrides.

    Official apps (those under the ``aleksis.apps` namespace) can override
    or add settings by listing them in their ``settings.overrides``.
    """
    overrides = {}

    for app in get_app_packages(True):
        mod_settings = get_app_module(app, "settings")
        if not mod_settings:
            continue

        if hasattr(mod_settings, "overrides"):
            for name in mod_settings.overrides:
                overrides[name] = getattr(mod_settings, name)

    return overrides


def get_site_preferences():
    """Get the preferences manager of the current site."""
    from django.contrib.sites.models import Site  # noqa

    return Site.objects.get_current().preferences


def lazy_preference(section: str, name: str) -> Callable[[str, str], Any]:
    """Lazily get a config value from dynamic preferences.

    Useful to bind preferences
    to other global settings to make them available to third-party apps that are not
    aware of dynamic preferences.
    """

    def _get_preference(section: str, name: str) -> Any:
        return get_site_preferences()[f"{section}__{name}"]

    # The type is guessed from the default value to improve lazy()'s behaviour
    # FIXME Reintroduce the behaviour described above
    return lazy(_get_preference, str)(section, name)


def get_or_create_favicon(title: str, default: str, is_favicon: bool = False) -> "Favicon":
    """Ensure that there is always a favicon object."""
    from favicon.models import Favicon  # noqa

    if not os.path.exists(default):
        warn("staticfiles are not ready yet, not creating default icons")
        return
    elif os.path.isdir(default):
        raise ImproperlyConfigured(f"staticfiles are broken: unexpected directory at {default}")

    favicon, created = Favicon.on_site.get_or_create(
        title=title, defaults={"isFavicon": is_favicon}
    )

    changed = False

    if favicon.isFavicon != is_favicon:
        favicon.isFavicon = True
        changed = True

    if created:
        favicon.faviconImage.save(os.path.basename(default), File(open(default, "rb")))
        changed = True

    if changed:
        favicon.save()

    return favicon


def get_pwa_icons():
    from django.conf import settings  # noqa

    favicon = get_or_create_favicon("pwa_icon", settings.DEFAULT_FAVICON_PATHS["pwa_icon"])
    favicon_imgs = favicon.get_favicons(config_override=settings.PWA_ICONS_CONFIG)
    return favicon_imgs


def is_impersonate(request: HttpRequest) -> bool:
    """Check whether the user was impersonated by an admin."""
    if hasattr(request, "user"):
        return getattr(request.user, "is_impersonate", False)
    else:
        return False


def has_person(obj: Union[HttpRequest, Model]) -> bool:
    """Check wehether a model object has a person attribute linking it to a Person object.

    The passed object can also be a HttpRequest object, in which case its
    associated User object is unwrapped and tested.
    """
    if isinstance(obj, HttpRequest):
        if hasattr(obj, "user"):
            obj = obj.user
        else:
            return False

    if obj.is_anonymous:
        return False

    person = getattr(obj, "person", None)
    if person is None:
        return False
    elif getattr(person, "is_dummy", False):
        return False
    else:
        return True


def custom_information_processor(request: Union[HttpRequest, None]) -> dict:
    """Provide custom information in all templates."""
    pwa_icons = get_pwa_icons()
    regrouped_pwa_icons = {}
    for pwa_icon in pwa_icons:
        regrouped_pwa_icons.setdefault(pwa_icon.rel, {})
        regrouped_pwa_icons[pwa_icon.rel][pwa_icon.size] = pwa_icon

    # This dictionary is passed to the frontend and made available as
    #  `$root.$aleksisFrontendSettings` in Vue.
    frontend_settings = {
        "sentry": {
            "enabled": settings.SENTRY_ENABLED,
        },
        "urls": {
            "base": settings.BASE_URL,
            "graphql": reverse("graphql"),
        },
    }

    context = {
        "ADMINS": settings.ADMINS,
        "PWA_ICONS": regrouped_pwa_icons,
        "SENTRY_ENABLED": settings.SENTRY_ENABLED,
        "SITE_PREFERENCES": get_site_preferences(),
        "BASE_URL": settings.BASE_URL,
        "FRONTEND_SETTINGS": frontend_settings,
    }

    if settings.SENTRY_ENABLED:
        frontend_settings["sentry"].update(settings.SENTRY_SETTINGS)

        import sentry_sdk

        span = sentry_sdk.Hub.current.scope.span
        if span is not None:
            context["SENTRY_TRACE_ID"] = span.to_traceparent()

    return context


def now_tomorrow() -> datetime:
    """Return current time tomorrow."""
    return timezone.now() + timedelta(days=1)


def objectgetter_optional(
    model: Model, default: Optional[Any] = None, default_eval: bool = False
) -> Callable[[HttpRequest, Optional[int]], Model]:
    """Get an object by pk, defaulting to None."""

    def get_object(request: HttpRequest, id_: Optional[int] = None, **kwargs) -> Optional[Model]:
        if id_ is not None:
            return get_object_or_404(model, pk=id_)
        else:
            try:
                return eval(default) if default_eval else default  # noqa:S307
            except (AttributeError, KeyError, IndexError):
                return None

    return get_object


@cache_memoize(3600)
def get_content_type_by_perm(perm: str) -> Union["ContentType", None]:
    from django.contrib.contenttypes.models import ContentType  # noqa

    try:
        return ContentType.objects.get(
            app_label=perm.split(".", 1)[0], permission__codename=perm.split(".", 1)[1]
        )
    except ContentType.DoesNotExist:
        return None


@cache_memoize(3600)
def queryset_rules_filter(
    obj: Union[HttpRequest, Model], queryset: QuerySet, perm: str
) -> QuerySet:
    """Filter queryset by user and permission."""
    wanted_objects = set()
    if isinstance(obj, HttpRequest) and hasattr(obj, "user"):
        obj = obj.user

    for item in queryset:
        if obj.has_perm(perm, item):
            wanted_objects.add(item.pk)

    return queryset.filter(pk__in=wanted_objects)


def generate_random_code(length, packet_size) -> str:
    """Generate random code for e.g. invitations."""
    return get_random_string(packet_size * length).lower()


def monkey_patch() -> None:  # noqa
    """Monkey-patch dependencies for special behaviour."""
    # Unwrap promises in JSON serializer instead of stringifying
    from django.core.serializers import json
    from django.utils.functional import Promise

    class DjangoJSONEncoder(json.DjangoJSONEncoder):
        def default(self, o: Any) -> Any:
            if isinstance(o, Promise) and hasattr(o, "copy"):
                return o.copy()
            return super().default(o)

    json.DjangoJSONEncoder = DjangoJSONEncoder


def get_allowed_object_ids(request: HttpRequest, models: list) -> list:
    """Get all objects of all given models the user of a given request is allowed to view."""
    allowed_object_ids = []

    for model in models:
        app_label = model._meta.app_label
        model_name = model.__name__.lower()

        # Loop through the pks of all objects of the current model the user is allowed to view
        # and put the corresponding ids into a django-haystack-style-formatted list
        allowed_object_ids += [
            f"{app_label}.{model_name}.{pk}"
            for pk in queryset_rules_filter(
                request, model.objects.all(), f"{app_label}.view_{model_name}_rule"
            ).values_list("pk", flat=True)
        ]

    return allowed_object_ids


def process_custom_context_processors(context_processors: list) -> Dict[str, Any]:
    """Process custom context processors."""
    context = {}
    processors = tuple(import_string(path) for path in context_processors)
    for processor in processors:
        context.update(processor(None))
    return context


def create_default_celery_schedule():
    """Create default periodic tasks in database for tasks that have a schedule defined."""
    from celery import current_app
    from celery.schedules import BaseSchedule, crontab, schedule, solar
    from django_celery_beat.clockedschedule import clocked
    from django_celery_beat.models import (
        ClockedSchedule,
        CrontabSchedule,
        IntervalSchedule,
        PeriodicTask,
        SolarSchedule,
    )

    defined_periodic_tasks = PeriodicTask.objects.values_list("task", flat=True).all()

    for name, task in current_app.tasks.items():
        if name in defined_periodic_tasks:
            # Task is already known in database, skip
            continue

        run_every = getattr(task, "run_every", None)
        if not run_every:
            # Task has no default schedule, skip
            continue

        if isinstance(run_every, (float, int, timedelta)):
            # Schedule is defined as a raw seconds value or timedelta, convert to schedule class
            run_every = schedule(run_every)
        elif not isinstance(run_every, BaseSchedule):
            raise ValueError(f"Task {name} has an invalid schedule defined.")

        # Find matching django-celery-beat schedule model
        if isinstance(run_every, clocked):
            Schedule = ClockedSchedule
            attr = "clocked"
        elif isinstance(run_every, crontab):
            Schedule = CrontabSchedule
            attr = "crontab"
        elif isinstance(run_every, schedule):
            Schedule = IntervalSchedule
            attr = "interval"
        elif isinstance(run_every, solar):
            Schedule = SolarSchedule
            attr = "solar"
        else:
            raise ValueError(f"Task {name} has an unknown schedule class defined.")

        # Get or create schedule in database
        db_schedule = Schedule.from_schedule(run_every)
        db_schedule.save()

        # Create periodic task
        PeriodicTask.objects.create(
            name=f"{name} (default schedule)", task=name, **{attr: db_schedule}
        )


class OOTRouter:
    """Database router for operations that should run out of transaction.

    This router routes database operations for certain apps through
    the separate default_oot connection, to ensure that data get
    updated immediately even during atomic transactions.
    """

    default_db = "default"
    oot_db = "default_oot"

    _cachalot_invalidating = []

    @property
    def oot_labels(self):
        return settings.DATABASE_OOT_LABELS

    @property
    def default_dbs(self):
        return set((self.default_db, self.oot_db))

    def is_same_db(self, db1: str, db2: str):
        return set((db1, db2)).issubset(self.default_dbs)

    def db_for_read(self, model: Model, **hints) -> Optional[str]:
        if model._meta.app_label in self.oot_labels:
            return self.oot_db

        return None

    def db_for_write(self, model: Model, **hints) -> Optional[str]:
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1: Model, obj2: Model, **hints) -> Optional[bool]:
        # Allow relations between default database and OOT connection
        # They are the same database
        if self.is_same_db(obj1._state.db, obj2._state.db):
            return True

        return None

    def allow_migrate(
        self, db: str, app_label: str, model_name: Optional[str] = None, **hints
    ) -> Optional[bool]:
        # Never allow any migrations on the default_oot database
        # It connects to the same database as default, so everything
        # migrated there
        if db == self.oot_db:
            return False

        return None

    @classmethod
    def _invalidate_cachalot(cls, sender, **kwargs):
        if sender in cls._cachalot_invalidating:
            return
        cls._cachalot_invalidating.append(sender)

        if kwargs["db_alias"] == cls.default_db:
            invalidate(sender, db_alias=cls.oot_db)
        elif kwargs["db_alias"] == cls.oot_db:
            invalidate(sender, db_alias=cls.default_db)

        if sender in cls._cachalot_invalidating:
            cls._cachalot_invalidating.remove(sender)


post_invalidation.connect(OOTRouter._invalidate_cachalot)


def get_ip(*args, **kwargs):
    """Recreate ipware.ip.get_ip as it was replaced by get_client_ip."""
    from ipware.ip import get_client_ip  # noqa

    return get_client_ip(*args, **kwargs)[0]
