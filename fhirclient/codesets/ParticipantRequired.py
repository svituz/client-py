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

class ParticipantRequired(object):
    """ Is the Participant required to attend the appointment.
    URL: http://hl7.org/fhir/participantrequired
    ValueSet: http://hl7.org/fhir/ValueSet/participantrequired
    """
    # The participant is required to attend the appointment.
    required = "required"
    # The participant may optionally attend the appointment.
    optional = "optional"
    # The participant is excluded from the appointment, and might not be informed of the appointment taking place.
	/// (Appointment is about them, not for them - such as 2 doctors discussing results about a patient's test).
    informationOnly = "information-only"