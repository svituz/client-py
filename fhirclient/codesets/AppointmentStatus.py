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

class AppointmentStatus(object):
    """ The free/busy status of an appointment.
    URL: http://hl7.org/fhir/appointmentstatus
    ValueSet: http://hl7.org/fhir/ValueSet/appointmentstatus
    """
    # None of the participant(s) have finalized their acceptance of the appointment request, and the start/end time
	/// might not be set yet.
    proposed = "proposed"
    # Some or all of the participant(s) have not finalized their acceptance of the appointment request.
    pending = "pending"
    # All participant(s) have been considered and the appointment is confirmed to go ahead at the date/times
	/// specified.
    booked = "booked"
    # The patient/patients has/have arrived and is/are waiting to be seen.
    arrived = "arrived"
    # The planning stages of the appointment are now complete, the encounter resource will exist and will track
	/// further status changes. Note that an encounter may exist before the appointment status is fulfilled for many
	/// reasons.
    fulfilled = "fulfilled"
    # The appointment has been cancelled.
    cancelled = "cancelled"
    # Some or all of the participant(s) have not/did not appear for the appointment (usually the patient).
    noshow = "noshow"
    # This instance should not have been part of this patient's medical record.
    enteredInError = "entered-in-error"
    # When checked in, all pre-encounter administrative work is complete, and the encounter may begin. (where multiple
	/// patients are involved, they are all present).
    checkedIn = "checked-in"
    # The appointment has been placed on a waitlist, to be scheduled/confirmed in the future when a slot/service is
	/// available.
	/// A specific time might or might not be pre-allocated.
    waitlist = "waitlist"