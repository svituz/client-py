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

class RequestStatus(object):
    """ Codes identifying the lifecycle stage of a request.
    URL: http://hl7.org/fhir/request-status
    ValueSet: http://hl7.org/fhir/ValueSet/request-status
    """
    # The request has been created but is not yet complete or ready for action.
    draft = "draft"
    # The request is in force and ready to be acted upon.
    active = "active"
    # The request (and any implicit authorization to act) has been temporarily withdrawn but is expected to resume in
	/// the future.
    onHold = "on-hold"
    # The request (and any implicit authorization to act) has been terminated prior to the known full completion of
	/// the intended actions.  No further activity should occur.
    revoked = "revoked"
    # The activity described by the request has been fully performed.  No further activity will occur.
    completed = "completed"
    # This request should never have existed and should be considered 'void'.  (It is possible that real-world
	/// decisions were based on it.  If real-world activity has occurred, the status should be "revoked" rather than
	/// "entered-in-error".).
    enteredInError = "entered-in-error"
    # The authoring/source system does not know which of the status values currently applies for this request.  Note:
	/// This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the
	/// authoring/source system does not know which.
    unknown = "unknown"