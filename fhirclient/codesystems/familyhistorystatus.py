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

class FamilyHistoryStatus(object):
    """ A code that identifies the status of the family history record.
    URL: http://hl7.org/fhir/history-status
    ValueSet: http://hl7.org/fhir/ValueSet/history-status
    """
    """Some health information is known and captured, but not complete - see notes for details."""
    PARTIAL = "partial"
    """All available related health information is captured as of the date (and possibly time) when the family member
	/// history was taken."""
    COMPLETED = "completed"
    """This instance should not have been part of this patient's medical record."""
    ENTEREDINERROR = "entered-in-error"
    """Health information for this family member is unavailable/unknown."""
    HEALTHUNKNOWN = "health-unknown"
    allowed_values = ['PARTIAL', 'COMPLETED', 'ENTEREDINERROR', 'HEALTHUNKNOWN']