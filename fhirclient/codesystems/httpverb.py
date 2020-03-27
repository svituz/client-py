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

class HTTPVerb(object):
    """ HTTP verbs (in the HTTP command line). See [HTTP rfc](https://tools.ietf.org/html/rfc7231) for details.
    URL: http://hl7.org/fhir/http-verb
    ValueSet: http://hl7.org/fhir/ValueSet/http-verb
    """
    """HTTP GET Command."""
    GET = "GET"
    """HTTP HEAD Command."""
    HEAD = "HEAD"
    """HTTP POST Command."""
    POST = "POST"
    """HTTP PUT Command."""
    PUT = "PUT"
    """HTTP DELETE Command."""
    DELETE = "DELETE"
    """HTTP PATCH Command."""
    PATCH = "PATCH"
    allowed_values = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'PATCH']