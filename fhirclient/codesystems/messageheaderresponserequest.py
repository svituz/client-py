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

class MessageheaderResponseRequest(object):
    """ HL7-defined table of codes which identify conditions under which acknowledgments are required to be returned in response
to a message.
    URL: http://hl7.org/fhir/messageheader-response-request
    ValueSet: http://hl7.org/fhir/ValueSet/messageheader-response-request
    """
    # initiator expects a response for this message.
    ALWAYS = "always"
    # initiator expects a response only if in error.
    ONERROR = "on-error"
    # initiator does not expect a response.
    NEVER = "never"
    # initiator expects a response only if successful.
    ONSUCCESS = "on-success"

    allowed_values = [ALWAYS, ONERROR, NEVER, ONSUCCESS]