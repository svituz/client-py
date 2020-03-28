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

class GoalAcceptanceStatus(object):
    """ Codes indicating whether the goal has been accepted by a stakeholder.
    URL: http://terminology.hl7.org/CodeSystem/goal-acceptance-status
    ValueSet: http://hl7.org/fhir/ValueSet/goal-acceptance-status
    """
    # Stakeholder supports pursuit of the goal.
    AGREE = "agree"
    # Stakeholder is not in support of the pursuit of the goal.
    DISAGREE = "disagree"
    # Stakeholder has not yet made a decision on whether they support the goal.
    PENDING = "pending"

    allowed_values = [AGREE, DISAGREE, PENDING]