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

class TriggerType(object):
    """ The type of trigger.
    URL: http://hl7.org/fhir/trigger-type
    ValueSet: http://hl7.org/fhir/ValueSet/trigger-type
    """
    """The trigger occurs in response to a specific named event, and no other information about the trigger is
	/// specified. Named events are completely pre-coordinated, and the formal semantics of the trigger are not
	/// provided."""
    NAMEDEVENT = "named-event"
    """The trigger occurs at a specific time or periodically as described by a timing or schedule. A periodic event
	/// cannot have any data elements, but may have a name assigned as a shorthand for the event."""
    PERIODIC = "periodic"
    """The trigger occurs whenever data of a particular type is changed in any way, either added, modified, or removed."""
    DATACHANGED = "data-changed"
    """The trigger occurs whenever data of a particular type is added."""
    DATAADDED = "data-added"
    """The trigger occurs whenever data of a particular type is modified."""
    DATAMODIFIED = "data-modified"
    """The trigger occurs whenever data of a particular type is removed."""
    DATAREMOVED = "data-removed"
    """The trigger occurs whenever data of a particular type is accessed."""
    DATAACCESSED = "data-accessed"
    """The trigger occurs whenever access to data of a particular type is completed."""
    DATAACCESSENDED = "data-access-ended"
    allowed_values = ['NAMEDEVENT', 'PERIODIC', 'DATACHANGED', 'DATAADDED', 'DATAMODIFIED', 'DATAREMOVED', 'DATAACCESSED', 'DATAACCESSENDED']