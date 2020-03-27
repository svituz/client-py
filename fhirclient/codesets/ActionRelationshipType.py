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

class ActionRelationshipType(object):
    """ Defines the types of relationships between actions.
    URL: http://hl7.org/fhir/action-relationship-type
    ValueSet: http://hl7.org/fhir/ValueSet/action-relationship-type
    """
    # The action must be performed before the start of the related action.
    beforeStart = "before-start"
    # The action must be performed before the related action.
    before = "before"
    # The action must be performed before the end of the related action.
    beforeEnd = "before-end"
    # The action must be performed concurrent with the start of the related action.
    concurrentWithStart = "concurrent-with-start"
    # The action must be performed concurrent with the related action.
    concurrent = "concurrent"
    # The action must be performed concurrent with the end of the related action.
    concurrentWithEnd = "concurrent-with-end"
    # The action must be performed after the start of the related action.
    afterStart = "after-start"
    # The action must be performed after the related action.
    after = "after"
    # The action must be performed after the end of the related action.
    afterEnd = "after-end"