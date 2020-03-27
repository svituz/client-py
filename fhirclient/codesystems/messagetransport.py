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

class MessageTransport(object):
    """ The protocol used for message transport.
    URL: http://terminology.hl7.org/CodeSystem/message-transport
    ValueSet: http://hl7.org/fhir/ValueSet/message-transport
    """
    """The application sends or receives messages using HTTP POST (may be over http: or https:)."""
    HTTP = "http"
    """The application sends or receives messages using File Transfer Protocol."""
    FTP = "ftp"
    """The application sends or receives messages using HL7's Minimal Lower Level Protocol."""
    MLLP = "mllp"
    allowed_values = ['HTTP', 'FTP', 'MLLP']