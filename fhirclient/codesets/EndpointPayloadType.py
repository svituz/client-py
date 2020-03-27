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

class EndpointPayloadType(object):
    """ This is an example value set defined by the FHIR project, that could be used to represent possible payload document
types.
    URL: http://terminology.hl7.org/CodeSystem/endpoint-payload-type
    """
    # Any payload type can be used with this endpoint, it is either a payload agnostic infrastructure (such as a
	/// storage repository), or some other type of endpoint where payload considerations are internally handled, and not
	/// available
    any = "any"
    # This endpoint does not require any content to be sent; simply connecting to the endpoint is enough notification.
	/// This can be used as a 'ping' to wakeup a service to retrieve content, which could be to ensure security
	/// considerations are correctly handled
    none = "none"