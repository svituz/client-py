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

class EncounterStatus(object):
    """ Current state of the encounter.
    URL: http://hl7.org/fhir/encounter-status
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-status
    """
    # The Encounter has not yet started.
    PLANNED = "planned"
    # The Patient is present for the encounter, however is not currently meeting with a practitioner.
    ARRIVED = "arrived"
    # The patient has been assessed for the priority of their treatment based on the severity of their condition.
    TRIAGED = "triaged"
    # The Encounter has begun and the patient is present / the practitioner and the patient are meeting.
    INPROGRESS = "in-progress"
    # The Encounter has begun, but the patient is temporarily on leave.
    ONLEAVE = "onleave"
    # The Encounter has ended.
    FINISHED = "finished"
    # The Encounter has ended before it has begun.
    CANCELLED = "cancelled"
    # This instance should not have been part of this patient's medical record.
    ENTEREDINERROR = "entered-in-error"
    # The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made
    # to provide a meaningful value other than "unknown".
    UNKNOWN = "unknown"

    allowed_values = [PLANNED, ARRIVED, TRIAGED, INPROGRESS, ONLEAVE, FINISHED, CANCELLED, ENTEREDINERROR, UNKNOWN]