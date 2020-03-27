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

class AllergyIntoleranceCategory(object):
    """ Category of an identified substance associated with allergies or intolerances.
    URL: http://hl7.org/fhir/allergy-intolerance-category
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-category
    """
    """Any substance consumed to provide nutritional support for the body."""
    FOOD = "food"
    """Substances administered to achieve a physiological effect."""
    MEDICATION = "medication"
    """Any substances that are encountered in the environment, including any substance not already classified as food,
	/// medication, or biologic."""
    ENVIRONMENT = "environment"
    """A preparation that is synthesized from living organisms or their products, especially a human or animal protein,
	/// such as a hormone or antitoxin, that is used as a diagnostic, preventive, or therapeutic agent. Examples of
	/// biologic medications include: vaccines; allergenic extracts, which are used for both diagnosis and treatment
	/// (for example, allergy shots); gene therapies; cellular therapies.  There are other biologic products, such as
	/// tissues, which are not typically associated with allergies."""
    BIOLOGIC = "biologic"
    allowed_values = ['FOOD', 'MEDICATION', 'ENVIRONMENT', 'BIOLOGIC']