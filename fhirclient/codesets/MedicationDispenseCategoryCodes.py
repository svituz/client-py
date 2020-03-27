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

class MedicationDispenseCategoryCodes(object):
    """ MedicationDispense Category Codes
    URL: http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-category
    ValueSet: http://hl7.org/fhir/ValueSet/medicationdispense-category
    """
    # Includes dispenses for medications to be administered or consumed in an inpatient or acute care setting.
    inpatient = "inpatient"
    # Includes dispenses for medications to be administered or consumed in an outpatient setting (for example,
	/// Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office).
    outpatient = "outpatient"
    # Includes dispenses for medications to be administered or consumed by the patient in their home (this would
	/// include long term care or nursing homes, hospices, etc.).
    community = "community"
    # Includes dispenses for medications created when the patient is being released from a facility.
    discharge = "discharge"