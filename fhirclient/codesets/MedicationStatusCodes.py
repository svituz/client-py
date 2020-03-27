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

class MedicationStatusCodes(object):
    """ Medication Status Codes
    URL: http://hl7.org/fhir/CodeSystem/medication-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-status
    """
    # The medication is available for use.
    active = "active"
    # The medication is not available for use.
    inactive = "inactive"
    # The medication was entered in error.
    enteredInError = "entered-in-error"