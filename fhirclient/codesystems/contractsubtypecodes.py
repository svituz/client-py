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

class ContractSubtypeCodes(object):
    """ This value set includes sample Contract Subtype codes.
    URL: http://terminology.hl7.org/CodeSystem/contractsubtypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-subtype
    """
    """Canadian health information disclosure policy."""
    DISCLOSURECA = "disclosure-ca"
    """United States health information disclosure policy."""
    DISCLOSUREUS = "disclosure-us"
    allowed_values = ['DISCLOSURECA', 'DISCLOSUREUS']