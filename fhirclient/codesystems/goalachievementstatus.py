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

class GoalAchievementStatus(object):
    """ Describes the progression, or lack thereof, towards the goal against the target.
    URL: http://terminology.hl7.org/CodeSystem/goal-achievement
    ValueSet: http://hl7.org/fhir/ValueSet/goal-achievement
    """
    # The goal is being sought but has not yet been reached. (Also applies if the goal was reached in the past but
    # there has been regression and the goal is again being sought).
    INPROGRESS = "in-progress"
    # The goal is being sought, and is progressing.
    IMPROVING = "improving"
    # The goal is being sought, but is regressing.
    WORSENING = "worsening"
    # The goal is being sought, but the trend is flat.
    NOCHANGE = "no-change"
    # The goal has been met.
    ACHIEVED = "achieved"
    # The goal has been met, but ongoing activity is needed to sustain the goal objective.
    SUSTAINING = "sustaining"
    # The goal has not been met and there might or might not have been progress towards target.
    NOTACHIEVED = "not-achieved"
    # The goal has not been met and little to no progress towards target.
    NOPROGRESS = "no-progress"
    # The goal is not possible to be met.
    NOTATTAINABLE = "not-attainable"

    allowed_values = [INPROGRESS, IMPROVING, WORSENING, NOCHANGE, ACHIEVED, SUSTAINING, NOTACHIEVED, NOPROGRESS, NOTATTAINABLE]