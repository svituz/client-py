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

class RestfulCapabilityMode(object):
    """ The mode of a RESTful capability statement.
    URL: http://hl7.org/fhir/restful-capability-mode
    ValueSet: http://hl7.org/fhir/ValueSet/restful-capability-mode
    """
    """The application acts as a client for this resource."""
    CLIENT = "client"
    """The application acts as a server for this resource."""
    SERVER = "server"
    allowed_values = ['CLIENT', 'SERVER']