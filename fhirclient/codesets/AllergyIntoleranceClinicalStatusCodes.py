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

class AllergyIntoleranceClinicalStatusCodes(object):
    """ Preferred value set for AllergyIntolerance Clinical Status.
    URL: http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical
    ValueSet: http://hl7.org/fhir/ValueSet/allergyintolerance-clinical
    """
    # The subject is currently experiencing, or is at risk of, a reaction to the identified substance.
    active = "active"
    # The subject is no longer at risk of a reaction to the identified substance.
    inactive = "inactive"
    # A reaction to the identified substance has been clinically reassessed by testing or re-exposure and is
	/// considered no longer to be present. Re-exposure could be accidental, unplanned, or outside of any clinical
	/// setting.
    resolved = "resolved"