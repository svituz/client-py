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

class AssertionResponseTypes(object):
    """ The type of response code to use for assertion.
    URL: http://hl7.org/fhir/assert-response-code-types
    ValueSet: http://hl7.org/fhir/ValueSet/assert-response-code-types
    """
    """Response code is 200."""
    OKAY = "okay"
    """Response code is 201."""
    CREATED = "created"
    """Response code is 204."""
    NOCONTENT = "noContent"
    """Response code is 304."""
    NOTMODIFIED = "notModified"
    """Response code is 400."""
    BAD = "bad"
    """Response code is 403."""
    FORBIDDEN = "forbidden"
    """Response code is 404."""
    NOTFOUND = "notFound"
    """Response code is 405."""
    METHODNOTALLOWED = "methodNotAllowed"
    """Response code is 409."""
    CONFLICT = "conflict"
    """Response code is 410."""
    GONE = "gone"
    """Response code is 412."""
    PRECONDITIONFAILED = "preconditionFailed"
    """Response code is 422."""
    UNPROCESSABLE = "unprocessable"
    allowed_values = ['OKAY', 'CREATED', 'NOCONTENT', 'NOTMODIFIED', 'BAD', 'FORBIDDEN', 'NOTFOUND', 'METHODNOTALLOWED', 'CONFLICT', 'GONE', 'PRECONDITIONFAILED', 'UNPROCESSABLE']