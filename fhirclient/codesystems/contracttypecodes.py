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
    PRIVACY = "privacy"
    # Information disclosure policy.
    DISCLOSURE = "disclosure"
    # Health Insurance policy.
    HEALTHINSURANCE = "healthinsurance"
    # Contract to supply goods or services.
    SUPPLY = "supply"
    # Consent Directive.
    CONSENT = "consent"

    allowed_values = [PRIVACY, DISCLOSURE, HEALTHINSURANCE, SUPPLY, CONSENT]