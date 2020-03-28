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

class ContractTermTypeCodes(object):
    """ This value set includes sample Contract Term Type codes.
    URL: http://terminology.hl7.org/CodeSystem/contracttermtypecodes
    ValueSet: http://hl7.org/fhir/ValueSet/contract-term-type
    """
    # Based on specialized statutes that deal with particular subjects.
    STATUTORY = "statutory"
    # Execution of the term in the contract is conditional on the execution of other actions.
    SUBJECTTO = "subject-to"

    allowed_values = [STATUTORY, SUBJECTTO]