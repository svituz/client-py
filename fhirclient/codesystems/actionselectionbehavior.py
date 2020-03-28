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

class ActionSelectionBehavior(object):
    """ Defines selection behavior of a group.
    URL: http://hl7.org/fhir/action-selection-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-selection-behavior
    """
    # Any number of the actions in the group may be chosen, from zero to all.
    ANY = "any"
    # All the actions in the group must be selected as a single unit.
    ALL = "all"
    # All the actions in the group are meant to be chosen as a single unit: either all must be selected by the end
    # user, or none may be selected.
    ALLORNONE = "all-or-none"
    # The end user must choose one and only one of the selectable actions in the group. The user SHALL NOT choose none
    # of the actions in the group.
    EXACTLYONE = "exactly-one"
    # The end user may choose zero or at most one of the actions in the group.
    ATMOSTONE = "at-most-one"
    # The end user must choose a minimum of one, and as many additional as desired.
    ONEORMORE = "one-or-more"

    allowed_values = [ANY, ALL, ALLORNONE, EXACTLYONE, ATMOSTONE, ONEORMORE]