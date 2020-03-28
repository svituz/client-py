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

class GoalLifecycleStatus(object):
    """ Codes that reflect the current state of a goal and whether the goal is still being targeted.
    URL: http://hl7.org/fhir/goal-status
    ValueSet: http://hl7.org/fhir/ValueSet/goal-status
    """
    # A goal is proposed for this patient.
    PROPOSED = "proposed"
    # A goal is planned for this patient.
    PLANNED = "planned"
    # A proposed goal was accepted or acknowledged.
    ACCEPTED = "accepted"
    # The goal is being sought actively.
    ACTIVE = "active"
    # The goal remains a long term objective but is no longer being actively pursued for a temporary period of time.
    ONHOLD = "on-hold"
    # The goal is no longer being sought.
    COMPLETED = "completed"
    # The goal has been abandoned.
    CANCELLED = "cancelled"
    # The goal was entered in error and voided.
    ENTEREDINERROR = "entered-in-error"
    # A proposed goal was rejected.
    REJECTED = "rejected"

    allowed_values = [PROPOSED, PLANNED, ACCEPTED, ACTIVE, ONHOLD, COMPLETED, CANCELLED, ENTEREDINERROR, REJECTED]