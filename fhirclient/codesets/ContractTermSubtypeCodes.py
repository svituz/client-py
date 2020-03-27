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

class ContractTermSubtypeCodes(object):
    """ This value set includes sample Contract Term SubType codes.
    URL: http://terminology.hl7.org/CodeSystem/contracttermsubtypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-term-subtype
    """
    # Terms that go to the very root of a contract.
    condition = "condition"
    # Less imperative than a condition, so the contract will survive a breach
    warranty = "warranty"
    # Breach of which might or might not go to the root of the contract depending upon the nature of the breach
    innominate = "innominate"