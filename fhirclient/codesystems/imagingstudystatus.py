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

class ImagingStudyStatus(object):
    """ The status of the ImagingStudy.
    URL: http://hl7.org/fhir/imagingstudy-status
    ValueSet: http://hl7.org/fhir/ValueSet/imagingstudy-status
    """
    """The existence of the imaging study is registered, but there is nothing yet available."""
    REGISTERED = "registered"
    """At least one instance has been associated with this imaging study."""
    AVAILABLE = "available"
    """The imaging study is unavailable because the imaging study was not started or not completed (also sometimes
	/// called "aborted")."""
    CANCELLED = "cancelled"
    """The imaging study has been withdrawn following a previous final release.  This electronic record should never
	/// have existed, though it is possible that real-world decisions were based on it. (If real-world activity has
	/// occurred, the status should be "cancelled" rather than "entered-in-error".)."""
    ENTEREDINERROR = "entered-in-error"
    """The system does not know which of the status values currently applies for this request. Note: This concept is
	/// not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known which one."""
    UNKNOWN = "unknown"
    allowed_values = ['REGISTERED', 'AVAILABLE', 'CANCELLED', 'ENTEREDINERROR', 'UNKNOWN']