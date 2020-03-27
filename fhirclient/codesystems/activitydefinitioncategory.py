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

class ActivityDefinitionCategory(object):
    """ High-level categorization of the type of activity.
    URL: http://terminology.hl7.org/CodeSystem/activity-definition-category
    ValueSet: http://hl7.org/fhir/ValueSet/activity-definition-category
    """
    """The activity is intended to provide or is related to treatment of the patient."""
    TREATMENT = "treatment"
    """The activity is intended to provide or is related to education of the patient."""
    EDUCATION = "education"
    """The activity is intended to perform or is related to assessment of the patient."""
    ASSESSMENT = "assessment"
    allowed_values = ['TREATMENT', 'EDUCATION', 'ASSESSMENT']