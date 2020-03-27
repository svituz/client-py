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

class QuestionnaireTextCategories(object):
    """ Codes defining the purpose of a Questionnaire item of type 'text'.
    URL: http://hl7.org/fhir/questionnaire-display-category
    ValueSet: http://hl7.org/fhir/ValueSet/questionnaire-display-category
    """
    # The text provides guidance on how to populate or use a portion of the questionnaire (or the questionnaire as a
	/// whole).
    instructions = "instructions"
    # The text provides guidance on how the information should be or will be handled from a
	/// security/confidentiality/access control perspective when completed
    security = "security"
    # The text provides additional guidance on populating the containing item.  Help text isn't necessarily expected
	/// to be rendered as part of the form, but may instead be made available through fly-over, pop-up button, link to a
	/// "help" page, etc.
    help = "help"