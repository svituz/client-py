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

class MedicationAdministrationCategoryCodes(object):
    """ MedicationAdministration Category Codes
    URL: http://terminology.hl7.org/CodeSystem/medication-admin-category
    ValueSet: http://hl7.org/fhir/ValueSet/medication-admin-category
    """
    """Includes administrations in an inpatient or acute care setting"""
    INPATIENT = "inpatient"
    """Includes administrations in an outpatient setting (for example, Emergency Department, Outpatient Clinic,
	/// Outpatient Surgery, Doctor's office)"""
    OUTPATIENT = "outpatient"
    """Includes administrations by the patient in their home (this would include long term care or nursing homes,
	/// hospices, etc.)"""
    COMMUNITY = "community"
    allowed_values = ['INPATIENT', 'OUTPATIENT', 'COMMUNITY']