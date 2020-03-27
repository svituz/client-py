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

class EventStatus(object):
    """ Codes identifying the lifecycle stage of an event.
    URL: http://hl7.org/fhir/event-status
    ValueSet: http://hl7.org/fhir/ValueSet/event-status
    """
    # The core event has not started yet, but some staging activities have begun (e.g. surgical suite preparation).
	/// Preparation stages may be tracked for billing purposes.
    preparation = "preparation"
    # The event is currently occurring.
    inProgress = "in-progress"
    # The event was terminated prior to any activity beyond preparation.  I.e. The 'main' activity has not yet begun.
	/// The boundary between preparatory and the 'main' activity is context-specific.
    notDone = "not-done"
    # The event has been temporarily stopped but is expected to resume in the future.
    onHold = "on-hold"
    # The event was terminated prior to the full completion of the intended activity but after at least some of the
	/// 'main' activity (beyond preparation) has occurred.
    stopped = "stopped"
    # The event has now concluded.
    completed = "completed"
    # This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it.  (If real-world activity has occurred, the status should be "stopped" rather than "entered-in-error".).
    enteredInError = "entered-in-error"
    # The authoring/source system does not know which of the status values currently applies for this event.  Note:
	/// This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the
	/// authoring/source system does not know which.
    unknown = "unknown"