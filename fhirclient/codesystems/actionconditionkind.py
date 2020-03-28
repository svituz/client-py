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

class ActionConditionKind(object):
    """ Defines the kinds of conditions that can appear on actions.
    URL: http://hl7.org/fhir/action-condition-kind
    ValueSet: http://hl7.org/fhir/ValueSet/action-condition-kind
    """
    # The condition describes whether or not a given action is applicable.
    APPLICABILITY = "applicability"
    # The condition is a starting condition for the action.
    START = "start"
    # The condition is a stop, or exit condition for the action.
    STOP = "stop"

    allowed_values = [APPLICABILITY, START, STOP]