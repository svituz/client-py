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

class MedicationKnowledgeStatusCodes(object):
    """ MedicationKnowledge Status Codes
    URL: http://terminology.hl7.org/CodeSystem/medicationknowledge-status
    ValueSet: http://hl7.org/fhir/ValueSet/medicationknowledge-status
    """
    # The medication is available for use.
    active = "active"
    # The medication is not available for use.
    inactive = "inactive"
    # The medication was entered in error.
    enteredInError = "entered-in-error"