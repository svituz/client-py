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

class CareTeamStatus(object):
    """ Indicates the status of the care team.
    URL: http://hl7.org/fhir/care-team-status
    ValueSet: http://hl7.org/fhir/ValueSet/care-team-status
    """
    """The care team has been drafted and proposed, but not yet participating in the coordination and delivery of
	/// patient care."""
    PROPOSED = "proposed"
    """The care team is currently participating in the coordination and delivery of care."""
    ACTIVE = "active"
    """The care team is temporarily on hold or suspended and not participating in the coordination and delivery of
	/// care."""
    SUSPENDED = "suspended"
    """The care team was, but is no longer, participating in the coordination and delivery of care."""
    INACTIVE = "inactive"
    """The care team should have never existed."""
    ENTEREDINERROR = "entered-in-error"
    allowed_values = ['PROPOSED', 'ACTIVE', 'SUSPENDED', 'INACTIVE', 'ENTEREDINERROR']