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

class ActionParticipantType(object):
    """ The type of participant for the action.
    URL: http://hl7.org/fhir/action-participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/action-participant-type
    """
    """The participant is the patient under evaluation."""
    PATIENT = "patient"
    """The participant is a practitioner involved in the patient's care."""
    PRACTITIONER = "practitioner"
    """The participant is a person related to the patient."""
    RELATEDPERSON = "related-person"
    """The participant is a system or device used in the care of the patient."""
    DEVICE = "device"
    allowed_values = ['PATIENT', 'PRACTITIONER', 'RELATEDPERSON', 'DEVICE']