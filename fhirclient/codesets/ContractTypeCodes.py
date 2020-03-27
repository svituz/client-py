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

class ContractTypeCodes(object):
    """ This value set includes sample Contract Type codes.
    URL: http://terminology.hl7.org/CodeSystem/contract-type
    ValueSet: http://hl7.org/fhir/ValueSet/contract-type
    """
    # Privacy policy.
    privacy = "privacy"
    # Information disclosure policy.
    disclosure = "disclosure"
    # Health Insurance policy.
    healthinsurance = "healthinsurance"
    # Contract to supply goods or services.
    supply = "supply"
    # Consent Directive.
    consent = "consent"