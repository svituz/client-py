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

class EventCapabilityMode(object):
    """ The mode of a message capability statement.
    URL: http://hl7.org/fhir/event-capability-mode
    ValueSet: http://hl7.org/fhir/ValueSet/event-capability-mode
    """
    # The application sends requests and receives responses.
    sender = "sender"
    # The application receives requests and sends responses.
    receiver = "receiver"