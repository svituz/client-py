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

class DefinitionTopic(object):
    """ High-level categorization of the definition, used for searching, sorting, and filtering.
    URL: http://terminology.hl7.org/CodeSystem/definition-topic
    ValueSet: http://hl7.org/fhir/ValueSet/definition-topic
    """
    # The definition is related to treatment of the patient.
    treatment = "treatment"
    # The definition is related to education of the patient.
    education = "education"
    # The definition is related to assessment of the patient.
    assessment = "assessment"