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

class ConsentProvisionType(object):
    """ How a rule statement is applied, such as adding additional consent or removing consent.
    URL: http://hl7.org/fhir/consent-provision-type
    ValueSet: http://hl7.org/fhir/ValueSet/consent-provision-type
    """
    """Consent is denied for actions meeting these rules."""
    DENY = "deny"
    """Consent is provided for actions meeting these rules."""
    PERMIT = "permit"
    allowed_values = ['DENY', 'PERMIT']