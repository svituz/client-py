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
    """The action must be performed before the start of the related action."""
    BEFORESTART = "before-start"
    """The action must be performed before the related action."""
    BEFORE = "before"
    """The action must be performed before the end of the related action."""
    BEFOREEND = "before-end"
    """The action must be performed concurrent with the start of the related action."""
    CONCURRENTWITHSTART = "concurrent-with-start"
    """The action must be performed concurrent with the related action."""
    CONCURRENT = "concurrent"
    """The action must be performed concurrent with the end of the related action."""
    CONCURRENTWITHEND = "concurrent-with-end"
    """The action must be performed after the start of the related action."""
    AFTERSTART = "after-start"
    """The action must be performed after the related action."""
    AFTER = "after"
    """The action must be performed after the end of the related action."""
    AFTEREND = "after-end"
    allowed_values = ['BEFORESTART', 'BEFORE', 'BEFOREEND', 'CONCURRENTWITHSTART', 'CONCURRENT', 'CONCURRENTWITHEND', 'AFTERSTART', 'AFTER', 'AFTEREND']