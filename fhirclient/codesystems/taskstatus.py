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

class TaskStatus(object):
    """ The current status of the task.
    URL: http://hl7.org/fhir/task-status
    ValueSet: http://hl7.org/fhir/ValueSet/task-status
    """
    """The task is not yet ready to be acted upon."""
    DRAFT = "draft"
    """The task is ready to be acted upon and action is sought."""
    REQUESTED = "requested"
    """A potential performer has claimed ownership of the task and is evaluating whether to perform it."""
    RECEIVED = "received"
    """The potential performer has agreed to execute the task but has not yet started work."""
    ACCEPTED = "accepted"
    """The potential performer who claimed ownership of the task has decided not to execute it prior to performing any
	/// action."""
    REJECTED = "rejected"
    """The task is ready to be performed, but no action has yet been taken.  Used in place of
	/// requested/received/accepted/rejected when request assignment and acceptance is a given."""
    READY = "ready"
    """The task was not completed."""
    CANCELLED = "cancelled"
    """The task has been started but is not yet complete."""
    INPROGRESS = "in-progress"
    """The task has been started but work has been paused."""
    ONHOLD = "on-hold"
    """The task was attempted but could not be completed due to some error."""
    FAILED = "failed"
    """The task has been completed."""
    COMPLETED = "completed"
    """The task should never have existed and is retained only because of the possibility it may have used."""
    ENTEREDINERROR = "entered-in-error"
    allowed_values = ['DRAFT', 'REQUESTED', 'RECEIVED', 'ACCEPTED', 'REJECTED', 'READY', 'CANCELLED', 'INPROGRESS', 'ONHOLD', 'FAILED', 'COMPLETED', 'ENTEREDINERROR']