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

class GoalCategory(object):
    """ Example codes for grouping goals to use for filtering or presentation.
    URL: http://terminology.hl7.org/CodeSystem/goal-category
    ValueSet: http://hl7.org/fhir/ValueSet/goal-category
    """
    # Goals related to the consumption of food and/or beverages.
    DIETARY = "dietary"
    # Goals related to the personal protection of the subject.
    SAFETY = "safety"
    # Goals related to the manner in which the subject acts.
    BEHAVIORAL = "behavioral"
    # Goals related to the practice of nursing or established by nurses.
    NURSING = "nursing"
    # Goals related to the mobility and/or motor capability of the subject.
    PHYSIOTHERAPY = "physiotherapy"

    allowed_values = [DIETARY, SAFETY, BEHAVIORAL, NURSING, PHYSIOTHERAPY]