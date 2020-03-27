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

class GoalStatusReason(object):
    """ Example codes indicating the reason for a current status.  Note that these are in no way complete and might not even be
appropriate for some uses.
    URL: http://hl7.org/fhir/goal-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/goal-status-reason
    """
    # Goal suspended or ended because of a surgical procedure.
    surgery = "surgery"
    # Goal suspended or ended because of a significant life event (marital change, bereavement, etc.).
    lifeEvent = "life-event"
    # Goal has been superseded by a new goal.
    replaced = "replaced"
    # Patient wishes the goal to be set aside, at least temporarily.
    patientRequest = "patient-request"
    # Goal cannot be reached temporarily.
    tempNotAttainable = "temp-not-attainable"
    # Goal cannot be reached permanently.
    permanentNotAttainable = "permanent-not-attainable"
    # Goal cannot be reached due to financial barrier or reason.
    financialBarrier = "financial-barrier"
    # Goal cannot be reached due to a lack of transportation.
    lackOfTransportation = "lack-of-transportation"
    # Goal cannot be reached due to a lack of social support.
    lackOfSocialSupport = "lack-of-social-support"