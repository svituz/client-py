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

class ParticipationStatus(object):
    """ The Participation status of an appointment.
    URL: http://hl7.org/fhir/participationstatus
    ValueSet: http://hl7.org/fhir/ValueSet/participationstatus
    """
    # The participant has accepted the appointment.
    accepted = "accepted"
    # The participant has declined the appointment and will not participate in the appointment.
    declined = "declined"
    # The participant has  tentatively accepted the appointment. This could be automatically created by a system and
	/// requires further processing before it can be accepted. There is no commitment that attendance will occur.
    tentative = "tentative"
    # The participant needs to indicate if they accept the appointment by changing this status to one of the other
	/// statuses.
    needsAction = "needs-action"