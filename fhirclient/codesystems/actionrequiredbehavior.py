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

class ActionRequiredBehavior(object):
    """ Defines expectations around whether an action or action group is required.
    URL: http://hl7.org/fhir/action-required-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-required-behavior
    """
    # An action with this behavior must be included in the actions processed by the end user; the end user SHALL NOT
    # choose not to include this action.
    MUST = "must"
    # An action with this behavior may be included in the set of actions processed by the end user.
    COULD = "could"
    # An action with this behavior must be included in the set of actions processed by the end user, unless the end
    # user provides documentation as to why the action was not included.
    MUSTUNLESSDOCUMENTED = "must-unless-documented"

    allowed_values = [MUST, COULD, MUSTUNLESSDOCUMENTED]