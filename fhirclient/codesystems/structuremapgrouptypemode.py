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

class StructureMapGroupTypeMode(object):
    """ If this is the default rule set to apply for the source type, or this combination of types.
    URL: http://hl7.org/fhir/map-group-type-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-group-type-mode
    """
    """This group is not a default group for the types."""
    NONE = "none"
    """This group is a default mapping group for the specified types and for the primary source type."""
    TYPES = "types"
    """This group is a default mapping group for the specified types."""
    TYPEANDTYPES = "type-and-types"
    allowed_values = ['NONE', 'TYPES', 'TYPEANDTYPES']