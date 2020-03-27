#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.
#
#  THIS HAS BEEN ADAPTED FROM Swift Enums WITHOUT EVER BEING IMPLEMENTED IN
#  Python, FOR DEMONSTRATION PURPOSES ONLY.
#

class CarePlanActivityStatus(object):
    """ Codes that reflect the current state of a care plan activity within its overall life cycle.
    URL: http://hl7.org/fhir/care-plan-activity-status
    ValueSet: http://hl7.org/fhir/ValueSet/care-plan-activity-status
    """
    """Care plan activity is planned but no action has yet been taken."""
    NOTSTARTED = "not-started"
    """Appointment or other booking has occurred but activity has not yet begun."""
    SCHEDULED = "scheduled"
    """Care plan activity has been started but is not yet complete."""
    INPROGRESS = "in-progress"
    """Care plan activity was started but has temporarily ceased with an expectation of resumption at a future time."""
    ONHOLD = "on-hold"
    """Care plan activity has been completed (more or less) as planned."""
    COMPLETED = "completed"
    """The planned care plan activity has been withdrawn."""
    CANCELLED = "cancelled"
    """The planned care plan activity has been ended prior to completion after the activity was started."""
    STOPPED = "stopped"
    """The current state of the care plan activity is not known.  Note: This concept is not to be used for "other" -
	/// one of the listed statuses is presumed to apply, but the authoring/source system does not know which one."""
    UNKNOWN = "unknown"
    """Care plan activity was entered in error and voided."""
    ENTEREDINERROR = "entered-in-error"
    allowed_values = ['NOTSTARTED', 'SCHEDULED', 'INPROGRESS', 'ONHOLD', 'COMPLETED', 'CANCELLED', 'STOPPED', 'UNKNOWN', 'ENTEREDINERROR']