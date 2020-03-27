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

class BenefitTermCodes(object):
    """ This value set includes a smattering of Benefit Term codes.
    URL: http://terminology.hl7.org/CodeSystem/benefit-term
    ValueSet: http://hl7.org/fhir/ValueSet/benefit-term
    """
    """Annual, renewing on the anniversary"""
    ANNUAL = "annual"
    """Per day"""
    DAY = "day"
    """For the total term, lifetime, of the policy or coverage"""
    LIFETIME = "lifetime"
    allowed_values = ['ANNUAL', 'DAY', 'LIFETIME']