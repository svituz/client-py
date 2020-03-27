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

class ResearchStudyObjectiveType(object):
    """ Codes for the kind of study objective.
    URL: http://terminology.hl7.org/CodeSystem/research-study-objective-type
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-objective-type
    """
    # The main question to be answered, and the one that drives any statistical planning for the study—e.g.,
	/// calculation of the sample size to provide the appropriate power for statistical testing.
    primary = "primary"
    # Question to be answered in the study that is of lesser importance than the primary objective.
    secondary = "secondary"
    # Exploratory questions to be answered in the study.
    exploratory = "exploratory"