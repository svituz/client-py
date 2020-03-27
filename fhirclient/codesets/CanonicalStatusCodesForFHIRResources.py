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

class CanonicalStatusCodesForFHIRResources(object):
    """ The master set of status codes used throughout FHIR. All status codes are mapped to one of these codes.
    URL: http://hl7.org/fhir/resource-status
    ValueSet: http://hl7.org/fhir/ValueSet/resource-status
    """
    # The resource was created in error, and should not be treated as valid (note: in many cases, for various data
	/// integrity related reasons, the information cannot be removed from the record)
    error = "error"
    # The resource describes an action or plan that is proposed, and not yet approved by the participants
    proposed = "proposed"
    # The resource describes a course of action that is planned and agreed/approved, but at the time of recording was
	/// still future
    planned = "planned"
    # The information in the resource is still being prepared and edited
    draft = "draft"
    # A fulfiller has been asked to perform this action, but it has not yet occurred
    requested = "requested"
    # The fulfiller has received the request, but not yet agreed to carry out the action
    received = "received"
    # The fulfiller chose not to perform the action
    declined = "declined"
    # The fulfiller has decided to perform the action, and plans are in train to do this in the future
    accepted = "accepted"
    # The pre-conditions for the action are all fulfilled, and it is imminent
    arrived = "arrived"
    # The resource describes information that is currently valid or a process that is presently occuring
    active = "active"
    # The process described/requested in this resource has been halted for some reason
    suspended = "suspended"
    # The process described/requested in the resource could not be completed, and no further action is planned
    failed = "failed"
    # The information in this resource has been replaced by information in another resource
    replaced = "replaced"
    # The process described/requested in the resource has been completed, and no further action is planned
    complete = "complete"
    # The resource describes information that is no longer valid or a process that is stopped occurring
    inactive = "inactive"
    # The process described/requested in the resource did not complete - usually due to some workflow error, and no
	/// further action is planned
    abandoned = "abandoned"
    # Authoring system does not know the status
    unknown = "unknown"
    # The information in this resource is not yet approved
    unconfirmed = "unconfirmed"
    # The information in this resource is approved
    confirmed = "confirmed"
    # The issue identified by this resource is no longer of concern
    resolved = "resolved"
    # This information has been ruled out by testing and evaluation
    refuted = "refuted"
    # Potentially true?
    differential = "differential"
    # This information is still being assembled
    partial = "partial"
    # not available at this time/location
    busyUnavailable = "busy-unavailable"
    # Free for scheduling
    free = "free"
    # Ready to act
    onTarget = "on-target"
    # Ahead of the planned timelines
    aheadOfTarget = "ahead-of-target"
    # behindTarget
    behindTarget = "behind-target"
    # Behind the planned timelines
    notReady = "not-ready"
    # The device transducer is disconnected
    transducDiscon = "transduc-discon"
    # The hardware is disconnected
    hwDiscon = "hw-discon"