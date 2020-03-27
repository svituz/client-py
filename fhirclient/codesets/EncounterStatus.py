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
    planned = "planned"
    # The Patient is present for the encounter, however is not currently meeting with a practitioner.
    arrived = "arrived"
    # The patient has been assessed for the priority of their treatment based on the severity of their condition.
    triaged = "triaged"
    # The Encounter has begun and the patient is present / the practitioner and the patient are meeting.
    inProgress = "in-progress"
    # The Encounter has begun, but the patient is temporarily on leave.
    onleave = "onleave"
    # The Encounter has ended.
    finished = "finished"
    # The Encounter has ended before it has begun.
    cancelled = "cancelled"
    # This instance should not have been part of this patient's medical record.
    enteredInError = "entered-in-error"
    # The encounter status is unknown. Note that "unknown" is a value of last resort and every attempt should be made
	/// to provide a meaningful value other than "unknown".
    unknown = "unknown"