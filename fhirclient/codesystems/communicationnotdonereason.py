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
    """The communication was not done due to an unknown reason."""
    UNKNOWN = "unknown"
    """The communication was not done due to a system error."""
    SYSTEMERROR = "system-error"
    """The communication was not done due to an invalid phone number."""
    INVALIDPHONENUMBER = "invalid-phone-number"
    """The communication was not done due to the recipient being unavailable."""
    RECIPIENTUNAVAILABLE = "recipient-unavailable"
    """The communication was not done due to a family objection."""
    FAMILYOBJECTION = "family-objection"
    """The communication was not done due to a patient objection."""
    PATIENTOBJECTION = "patient-objection"
    allowed_values = ['UNKNOWN', 'SYSTEMERROR', 'INVALIDPHONENUMBER', 'RECIPIENTUNAVAILABLE', 'FAMILYOBJECTION', 'PATIENTOBJECTION']