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
    dietary = "dietary"
    # Goals related to the personal protection of the subject.
    safety = "safety"
    # Goals related to the manner in which the subject acts.
    behavioral = "behavioral"
    # Goals related to the practice of nursing or established by nurses.
    nursing = "nursing"
    # Goals related to the mobility and/or motor capability of the subject.
    physiotherapy = "physiotherapy"