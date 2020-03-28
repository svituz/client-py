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

class ParticipantType(object):
    """ This value set defines a set of codes that can be used to indicate how an individual participates in an encounter.
    URL: http://terminology.hl7.org/CodeSystem/participant-type
    """
    # A translator who is facilitating communication with the patient during the encounter.
    TRANSLATOR = "translator"
    # A person to be contacted in case of an emergency during the encounter.
    EMERGENCY = "emergency"

    allowed_values = [TRANSLATOR, EMERGENCY]