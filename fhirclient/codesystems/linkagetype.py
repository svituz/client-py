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

class LinkageType(object):
    """ Used to distinguish different roles a resource can play within a set of linked resources.
    URL: http://hl7.org/fhir/linkage-type
    ValueSet: http://hl7.org/fhir/ValueSet/linkage-type
    """
    """The resource represents the "source of truth" (from the perspective of this Linkage resource) for the underlying
	/// event/condition/etc."""
    SOURCE = "source"
    """The resource represents an alternative view of the underlying event/condition/etc.  The resource may still be
	/// actively maintained, even though it is not considered to be the source of truth."""
    ALTERNATE = "alternate"
    """The resource represents an obsolete record of the underlying event/condition/etc.  It is not expected to be
	/// actively maintained."""
    HISTORICAL = "historical"
    allowed_values = ['SOURCE', 'ALTERNATE', 'HISTORICAL']