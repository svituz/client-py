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

class MedicationDispensePerformerFunctionCodes(object):
    """ MedicationDispense Performer Function Codes
    URL: http://terminology.hl7.org/CodeSystem/medicationdispense-performer-function
    ValueSet: http://hl7.org/fhir/ValueSet/medicationdispense-performer-function
    """
    # Recorded the details of the request
    dataenterer = "dataenterer"
    # Prepared the medication.
    packager = "packager"
    # Performed initial quality assurance on the prepared medication
    checker = "checker"
    # Performed the final quality assurance on the prepared medication against the request. Typically, this is a
	/// pharmacist function.
    finalchecker = "finalchecker"