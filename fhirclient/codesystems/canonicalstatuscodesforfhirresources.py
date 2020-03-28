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
    # integrity related reasons, the information cannot be removed from the record)
    ERROR = "error"
    # The resource describes an action or plan that is proposed, and not yet approved by the participants
    PROPOSED = "proposed"
    # The resource describes a course of action that is planned and agreed/approved, but at the time of recording was
    # still future
    PLANNED = "planned"
    # The information in the resource is still being prepared and edited
    DRAFT = "draft"
    # A fulfiller has been asked to perform this action, but it has not yet occurred
    REQUESTED = "requested"
    # The fulfiller has received the request, but not yet agreed to carry out the action
    RECEIVED = "received"
    # The fulfiller chose not to perform the action
    DECLINED = "declined"
    # The fulfiller has decided to perform the action, and plans are in train to do this in the future
    ACCEPTED = "accepted"
    # The pre-conditions for the action are all fulfilled, and it is imminent
    ARRIVED = "arrived"
    # The resource describes information that is currently valid or a process that is presently occuring
    ACTIVE = "active"
    # The process described/requested in this resource has been halted for some reason
    SUSPENDED = "suspended"
    # The process described/requested in the resource could not be completed, and no further action is planned
    FAILED = "failed"
    # The information in this resource has been replaced by information in another resource
    REPLACED = "replaced"
    # The process described/requested in the resource has been completed, and no further action is planned
    COMPLETE = "complete"
    # The resource describes information that is no longer valid or a process that is stopped occurring
    INACTIVE = "inactive"
    # The process described/requested in the resource did not complete - usually due to some workflow error, and no
    # further action is planned
    ABANDONED = "abandoned"
    # Authoring system does not know the status
    UNKNOWN = "unknown"
    # The information in this resource is not yet approved
    UNCONFIRMED = "unconfirmed"
    # The information in this resource is approved
    CONFIRMED = "confirmed"
    # The issue identified by this resource is no longer of concern
    RESOLVED = "resolved"
    # This information has been ruled out by testing and evaluation
    REFUTED = "refuted"
    # Potentially true?
    DIFFERENTIAL = "differential"
    # This information is still being assembled
    PARTIAL = "partial"
    # not available at this time/location
    BUSYUNAVAILABLE = "busy-unavailable"
    # Free for scheduling
    FREE = "free"
    # Ready to act
    ONTARGET = "on-target"
    # Ahead of the planned timelines
    AHEADOFTARGET = "ahead-of-target"
    # behindTarget
    BEHINDTARGET = "behind-target"
    # Behind the planned timelines
    NOTREADY = "not-ready"
    # The device transducer is disconnected
    TRANSDUCDISCON = "transduc-discon"
    # The hardware is disconnected
    HWDISCON = "hw-discon"

    allowed_values = [ERROR, PROPOSED, PLANNED, DRAFT, REQUESTED, RECEIVED, DECLINED, ACCEPTED, ARRIVED, ACTIVE, SUSPENDED, FAILED, REPLACED, COMPLETE, INACTIVE, ABANDONED, UNKNOWN, UNCONFIRMED, CONFIRMED, RESOLVED, REFUTED, DIFFERENTIAL, PARTIAL, BUSYUNAVAILABLE, FREE, ONTARGET, AHEADOFTARGET, BEHINDTARGET, NOTREADY, TRANSDUCDISCON, HWDISCON]