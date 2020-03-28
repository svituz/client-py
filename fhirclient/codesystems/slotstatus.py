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

class SlotStatus(object):
    """ The free/busy status of the slot.
    URL: http://hl7.org/fhir/slotstatus
    ValueSet: http://hl7.org/fhir/ValueSet/slotstatus
    """
    # Indicates that the time interval is busy because one  or more events have been scheduled for that interval.
    BUSY = "busy"
    # Indicates that the time interval is free for scheduling.
    FREE = "free"
    # Indicates that the time interval is busy and that the interval cannot be scheduled.
    BUSYUNAVAILABLE = "busy-unavailable"
    # Indicates that the time interval is busy because one or more events have been tentatively scheduled for that
    # interval.
    BUSYTENTATIVE = "busy-tentative"
    # This instance should not have been part of this patient's medical record.
    ENTEREDINERROR = "entered-in-error"

    allowed_values = [BUSY, FREE, BUSYUNAVAILABLE, BUSYTENTATIVE, ENTEREDINERROR]