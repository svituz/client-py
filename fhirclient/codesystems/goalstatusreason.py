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
    """Goal suspended or ended because of a surgical procedure."""
    SURGERY = "surgery"
    """Goal suspended or ended because of a significant life event (marital change, bereavement, etc.)."""
    LIFEEVENT = "life-event"
    """Goal has been superseded by a new goal."""
    REPLACED = "replaced"
    """Patient wishes the goal to be set aside, at least temporarily."""
    PATIENTREQUEST = "patient-request"
    """Goal cannot be reached temporarily."""
    TEMPNOTATTAINABLE = "temp-not-attainable"
    """Goal cannot be reached permanently."""
    PERMANENTNOTATTAINABLE = "permanent-not-attainable"
    """Goal cannot be reached due to financial barrier or reason."""
    FINANCIALBARRIER = "financial-barrier"
    """Goal cannot be reached due to a lack of transportation."""
    LACKOFTRANSPORTATION = "lack-of-transportation"
    """Goal cannot be reached due to a lack of social support."""
    LACKOFSOCIALSUPPORT = "lack-of-social-support"
    allowed_values = ['SURGERY', 'LIFEEVENT', 'REPLACED', 'PATIENTREQUEST', 'TEMPNOTATTAINABLE', 'PERMANENTNOTATTAINABLE', 'FINANCIALBARRIER', 'LACKOFTRANSPORTATION', 'LACKOFSOCIALSUPPORT']