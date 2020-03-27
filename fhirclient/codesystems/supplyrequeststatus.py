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

class SupplyRequestStatus(object):
    """ Status of the supply request.
    URL: http://hl7.org/fhir/supplyrequest-status
    ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-status
    """
    """The request has been created but is not yet complete or ready for action."""
    DRAFT = "draft"
    """The request is ready to be acted upon."""
    ACTIVE = "active"
    """The authorization/request to act has been temporarily withdrawn but is expected to resume in the future."""
    SUSPENDED = "suspended"
    """The authorization/request to act has been terminated prior to the full completion of the intended actions.  No
	/// further activity should occur."""
    CANCELLED = "cancelled"
    """Activity against the request has been sufficiently completed to the satisfaction of the requester."""
    COMPLETED = "completed"
    """This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".)."""
    ENTEREDINERROR = "entered-in-error"
    """The authoring/source system does not know which of the status values currently applies for this observation.
	/// Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the
	/// authoring/source system does not know which."""
    UNKNOWN = "unknown"
    allowed_values = ['DRAFT', 'ACTIVE', 'SUSPENDED', 'CANCELLED', 'COMPLETED', 'ENTEREDINERROR', 'UNKNOWN']