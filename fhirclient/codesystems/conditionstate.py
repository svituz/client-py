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

class ConditionState(object):
    """ Enumeration indicating whether the condition is currently active, inactive, or has been resolved.
    URL: http://terminology.hl7.org/CodeSystem/condition-state
    ValueSet: http://hl7.org/fhir/ValueSet/condition-state
    """
    """The condition is active."""
    ACTIVE = "active"
    """The condition is inactive, but not resolved."""
    INACTIVE = "inactive"
    """The condition is resolved."""
    RESOLVED = "resolved"
    allowed_values = ['ACTIVE', 'INACTIVE', 'RESOLVED']