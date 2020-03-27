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

class ExampleServiceModifierCodes(object):
    """ This value set includes sample Service Modifier codes which may support differential payment.
    URL: http://hl7.org/fhir/ex-servicemodifier
    ValueSet: http://hl7.org/fhir/ValueSet/service-modifiers
    """
    """Services provided on the side of the road or such other non-conventional setting."""
    SR = "sr"
    """Services provided outside or normal business hours."""
    AH = "ah"
    allowed_values = ['SR', 'AH']