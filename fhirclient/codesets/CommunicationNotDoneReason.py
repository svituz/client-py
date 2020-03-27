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

class CommunicationNotDoneReason(object):
    """ Codes for the reason why a communication did not happen.
    URL: http://terminology.hl7.org/CodeSystem/communication-not-done-reason
    ValueSet: http://hl7.org/fhir/ValueSet/communication-not-done-reason
    """
    # The communication was not done due to an unknown reason.
    unknown = "unknown"
    # The communication was not done due to a system error.
    systemError = "system-error"
    # The communication was not done due to an invalid phone number.
    invalidPhoneNumber = "invalid-phone-number"
    # The communication was not done due to the recipient being unavailable.
    recipientUnavailable = "recipient-unavailable"
    # The communication was not done due to a family objection.
    familyObjection = "family-objection"
    # The communication was not done due to a patient objection.
    patientObjection = "patient-objection"