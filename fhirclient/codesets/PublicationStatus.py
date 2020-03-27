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

class PublicationStatus(object):
    """ The lifecycle status of an artifact.
    URL: http://hl7.org/fhir/publication-status
    ValueSet: http://hl7.org/fhir/ValueSet/publication-status
    """
    # This resource is still under development and is not yet considered to be ready for normal use.
    draft = "draft"
    # This resource is ready for normal use.
    active = "active"
    # This resource has been withdrawn or superseded and should no longer be used.
    retired = "retired"
    # The authoring system does not know which of the status values currently applies for this resource.  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    unknown = "unknown"