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

class EncounterLocationStatus(object):
    """ The status of the location.
    URL: http://hl7.org/fhir/encounter-location-status
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-location-status
    """
    # The patient is planned to be moved to this location at some point in the future.
    PLANNED = "planned"
    # The patient is currently at this location, or was between the period specified.
    # 
    # A system may update these records when the patient leaves the location to either reserved, or completed.
    ACTIVE = "active"
    # This location is held empty for this patient.
    RESERVED = "reserved"
    # The patient was at this location during the period specified.
    # 
    # Not to be used when the patient is currently at the location.
    COMPLETED = "completed"

    allowed_values = [PLANNED, ACTIVE, RESERVED, COMPLETED]