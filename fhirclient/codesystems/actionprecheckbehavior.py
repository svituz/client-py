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

class ActionPrecheckBehavior(object):
    """ Defines selection frequency behavior for an action or group.
    URL: http://hl7.org/fhir/action-precheck-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-precheck-behavior
    """
    """An action with this behavior is one of the most frequent action that is, or should be, included by an end user,
	/// for the particular context in which the action occurs. The system displaying the action to the end user should
	/// consider "pre-checking" such an action as a convenience for the user."""
    YES = "yes"
    """An action with this behavior is one of the less frequent actions included by the end user, for the particular
	/// context in which the action occurs. The system displaying the actions to the end user would typically not "pre-
	/// check" such an action."""
    NO = "no"
    allowed_values = ['YES', 'NO']