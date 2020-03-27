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

class AuditEventAction(object):
    """ Indicator for type of action performed during the event that generated the event.
    URL: http://hl7.org/fhir/audit-event-action
    ValueSet: http://hl7.org/fhir/ValueSet/audit-event-action
    """
    """Create a new database object, such as placing an order."""
    C = "C"
    """Display or print data, such as a doctor census."""
    R = "R"
    """Update data, such as revise patient information."""
    U = "U"
    """Delete items, such as a doctor master file record."""
    D = "D"
    """Perform a system or application function such as log-on, program execution or use of an object's method, or
	/// perform a query/search operation."""
    E = "E"
    allowed_values = ['C', 'R', 'U', 'D', 'E']