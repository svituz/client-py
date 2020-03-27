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

class TestScriptRequestMethodCode(object):
    """ The allowable request method or HTTP operation codes.
    URL: http://hl7.org/fhir/http-operations
    ValueSet: http://hl7.org/fhir/ValueSet/http-operations
    """
    """HTTP DELETE operation."""
    DELETE = "delete"
    """HTTP GET operation."""
    GET = "get"
    """HTTP OPTIONS operation."""
    OPTIONS = "options"
    """HTTP PATCH operation."""
    PATCH = "patch"
    """HTTP POST operation."""
    POST = "post"
    """HTTP PUT operation."""
    PUT = "put"
    """HTTP HEAD operation."""
    HEAD = "head"
    allowed_values = ['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'HEAD']