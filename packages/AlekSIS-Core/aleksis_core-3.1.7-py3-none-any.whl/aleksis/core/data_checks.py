import logging
from datetime import timedelta

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.aggregates import Count
from django.utils.functional import classproperty
from django.utils.text import slugify
from django.utils.translation import gettext as _

import reversion
from reversion import set_comment

from .mixins import RegistryObject
from .util.celery_progress import ProgressRecorder, recorded_task
from .util.core_helpers import get_site_preferences
from .util.email import send_email


class SolveOption:
    """Define a solve option for one or more data checks.

    Solve options are used in order to give the data admin typical
    solutions to a data issue detected by a data check.

    Example definition

    .. code-block:: python

        from aleksis.core.data_checks import SolveOption
        from django.utils.translation import gettext as _

        class DeleteSolveOption(SolveOption):
            name = "delete" # has to be unqiue
            verbose_name = _("Delete") # should make use of i18n

            @classmethod
            def solve(cls, check_result: "DataCheckResult"):
                check_result.related_object.delete()
                check_result.delete()

    After the solve option has been successfully executed,
    the corresponding data check result has to be deleted.
    """

    name: str = "default"
    verbose_name: str = ""

    @classmethod
    def solve(cls, check_result: "DataCheckResult"):
        pass


class IgnoreSolveOption(SolveOption):
    """Mark the object with data issues as solved."""

    name = "ignore"
    verbose_name = _("Ignore problem")

    @classmethod
    def solve(cls, check_result: "DataCheckResult"):
        """Mark the object as solved without doing anything more."""
        check_result.solved = True
        check_result.save()


class DataCheck(RegistryObject):
    """Define a data check.

    Data checks should be used to search objects of
    any type which are broken or need some extra action.

    Defining data checks
    --------------------
    Data checks are defined by inheriting from the class DataCheck
    and registering the inherited class in the data check registry.

    Example:

    ``data_checks.py``
    ******************

    .. code-block:: python

        from aleksis.core.data_checks import DataCheck, DATA_CHECK_REGISTRY
        from django.utils.translation import gettext as _

        class ExampleDataCheck(DataCheck):
            name = "example" # has to be unique
            verbose_name = _("Ensure that there are no examples.")
            problem_name = _("There is an example.") # should both make use of i18n

            solve_options = {
                IgnoreSolveOption.name: IgnoreSolveOption
            }

            @classmethod
            def check_data(cls):
                from example_app.models import ExampleModel

                wrong_examples = ExampleModel.objects.filter(wrong_value=True)

                for example in wrong_examples:
                    cls.register_result(example)

    ``models.py``
    *************

    .. code-block:: python

        from .data_checks import ExampleDataCheck

        # ...

        class ExampleModel(Model):
            data_checks = [ExampleDataCheck]


    Solve options are used in order to give the data admin typical solutions to this specific issue.
    They are defined by inheriting from SolveOption.
    More information about defining solve options can be find there.

    The dictionary ``solve_options`` should include at least the IgnoreSolveOption,
    but preferably also own solve options. The keys in this dictionary
    have to be ``<YourOption>SolveOption.name``
    and the values must be the corresponding solve option classes.

    The class method ``check_data`` does the actual work. In this method
    your code should find all objects with issues and should register
    them in the result database using the class method ``register_result``.

    Data checks have to be registered in their corresponding model.
    This can be done by adding a list ``data_checks``
    containing the data check classes.

    Executing data checks
    ---------------------
    The data checks can be executed by using the
    celery task named ``aleksis.core.data_checks.check_data``.
    We recommend to create a periodic task in the backend
    which executes ``check_data`` on a regular base (e. g. every day).

    .. warning::
        To use the option described above, you must have setup celery properly.

    Notifications about results
    ---------------------------
    The data check tasks can notify persons via email
    if there are new data issues. You can set these persons
    by adding them to the preference
    ``Email recipients for data checks problem emails`` in the site configuration.

    To enable this feature, you also have to activate
    the preference ``Send emails if data checks detect problems``.
    """  # noqa: D412

    verbose_name: str = ""
    problem_name: str = ""

    solve_options = {IgnoreSolveOption.name: IgnoreSolveOption}

    _current_results = []

    @classmethod
    def check_data(cls):
        """Find all objects with data issues and register them."""
        pass

    @classmethod
    def run_check_data(cls):
        """Wrap ``check_data`` to ensure that post-processing tasks are run."""
        cls.check_data()
        cls.delete_old_results()

    @classmethod
    def solve(cls, check_result: "DataCheckResult", solve_option: str):
        """Execute a solve option for an object detected by this check.

        :param check_result: The result item from database
        :param solve_option: The name of the solve option that should be executed
        """
        with reversion.create_revision():
            solve_option_obj = cls.solve_options[solve_option]
            set_comment(
                _(
                    f"Solve option '{solve_option_obj.verbose_name}' "
                    f"for data check '{cls.verbose_name}'"
                )
            )
            solve_option_obj.solve(check_result)

    @classmethod
    def register_result(cls, instance) -> "DataCheckResult":
        """Register an object with data issues in the result database.

        :param instance: The affected object
        :return: The database entry
        """
        from aleksis.core.models import DataCheckResult

        ct = ContentType.objects.get_for_model(instance)
        result, __ = DataCheckResult.objects.get_or_create(
            data_check=cls.name, content_type=ct, object_id=instance.id
        )

        # Track all existing problems (for deleting old results)
        cls._current_results.append(result)

        return result

    @classmethod
    def delete_old_results(cls):
        """Delete old data check results for problems which exist no longer."""
        DataCheckResult = apps.get_model("core", "DataCheckResult")

        pks = [r.pk for r in cls._current_results]
        old_results = DataCheckResult.objects.filter(data_check=cls.name).exclude(pk__in=pks)

        if old_results:
            logging.info(f"Delete {old_results.count()} old data check results.")
            old_results.delete()

        # Reset list with existing problems
        cls._current_results = []

    @classproperty
    def data_checks_choices(cls):
        return [(check.name, check.verbose_name) for check in cls.registered_objects_list]


@recorded_task(run_every=timedelta(minutes=15))
def check_data(recorder: ProgressRecorder):
    """Execute all registered data checks and send email if activated."""
    for check in recorder.iterate(DataCheck.registered_objects_list):
        logging.info(f"Run check: {check.verbose_name}")
        check.run_check_data()

    if get_site_preferences()["general__data_checks_send_emails"]:
        send_emails_for_data_checks()


def send_emails_for_data_checks():
    """Notify one or more recipients about new problems with data.

    Recipients can be set in dynamic preferences.
    """
    from .models import DataCheckResult  # noqa

    results = DataCheckResult.objects.filter(solved=False, sent=False)

    if results.exists():
        results_by_check = results.values("data_check").annotate(count=Count("data_check"))

        results_with_checks = []
        for result in results_by_check:
            results_with_checks.append(
                (DataCheck.registered_objects_dict[result["data_check"]], result["count"])
            )

        recipient_list = [
            p.mail_sender
            for p in get_site_preferences()["general__data_checks_recipients"]
            if p.email
        ]

        for group in get_site_preferences()["general__data_checks_recipient_groups"]:
            recipient_list += [p.mail_sender for p in group.announcement_recipients if p.email]

        send_email(
            template_name="data_checks",
            recipient_list=recipient_list,
            context={"results": results_with_checks},
        )

        logging.info("Sent notification email because of unsent data checks")

        results.update(sent=True)


class DeactivateDashboardWidgetSolveOption(SolveOption):
    name = "deactivate_dashboard_widget"
    verbose_name = _("Deactivate DashboardWidget")

    @classmethod
    def solve(cls, check_result: "DataCheckResult"):
        widget = check_result.related_object
        widget.active = False
        widget.save()
        check_result.delete()


class BrokenDashboardWidgetDataCheck(DataCheck):
    name = "broken_dashboard_widgets"
    verbose_name = _("Ensure that there are no broken DashboardWidgets.")
    problem_name = _("The DashboardWidget was reported broken automatically.")
    solve_options = {
        IgnoreSolveOption.name: IgnoreSolveOption,
        DeactivateDashboardWidgetSolveOption.name: DeactivateDashboardWidgetSolveOption,
    }

    @classmethod
    def check_data(cls):
        from .models import DashboardWidget

        broken_widgets = DashboardWidget.objects.filter(broken=True, active=True)

        for widget in broken_widgets:
            logging.info("Check DashboardWidget %s", widget)
            cls.register_result(widget)


def field_validation_data_check_factory(app_name: str, model_name: str, field_name: str) -> type:
    from django.apps import apps

    class FieldValidationDataCheck(DataCheck):
        name = f"field_validation_{slugify(model_name)}_{slugify(field_name)}"
        verbose_name = _(
            "Validate field %s of model %s." % (field_name, app_name + "." + model_name)
        )
        problem_name = _("The field %s couldn't be validated successfully." % field_name)
        solve_options = {
            IgnoreSolveOption.name: IgnoreSolveOption,
        }

        @classmethod
        def check_data(cls):
            model: Model = apps.get_model(app_name, model_name)
            for obj in model.objects.all():
                try:
                    model._meta.get_field(field_name).validate(getattr(obj, field_name), obj)
                except ValidationError as e:
                    logging.info(f"Check {model_name} {obj}")
                    cls.register_result(obj)

    FieldValidationDataCheck.__name__ = model_name + "FieldValidationDataCheck"

    return FieldValidationDataCheck


field_validation_data_check_factory("core", "CustomMenuItem", "icon")
