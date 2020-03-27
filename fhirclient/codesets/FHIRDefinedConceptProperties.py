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

class FHIRDefinedConceptProperties(object):
    """ A set of common concept properties for use on coded systems throughout the FHIR eco-system.
    URL: http://hl7.org/fhir/concept-properties
    ValueSet: http://hl7.org/fhir/ValueSet/concept-properties
    """
    # True if the concept is not considered active - e.g. not a valid concept any more. Property type is boolean,
	/// default value is false
    inactive = "inactive"
    # The date at which a concept was deprecated. Concepts that are deprecated but not inactive can still be used, but
	/// their use is discouraged, and they should be expected to be made inactive in a future release. Property type is
	/// dateTime
    deprecated = "deprecated"
    # The concept is not intended to be chosen by the user - only intended to be used as a selector for other
	/// concepts. Note, though, that the interpretation of this is highly contextual; all concepts are selectable in
	/// some context. Property type is boolean
    notSelectable = "notSelectable"
    # The concept identified in this property is a parent of the concept on which it is a property. The property type
	/// will be 'code'. The meaning of 'parent' is defined by the hierarchyMeaning attribute
    parent = "parent"
    # The concept identified in this property is a child of the concept on which it is a property. The property type
	/// will be 'code'. The meaning of 'child' is defined by the hierarchyMeaning attribute
    child = "child"