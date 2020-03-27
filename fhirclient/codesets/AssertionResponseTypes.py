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
    # Response code is 200.
    okay = "okay"
    # Response code is 201.
    created = "created"
    # Response code is 204.
    noContent = "noContent"
    # Response code is 304.
    notModified = "notModified"
    # Response code is 400.
    bad = "bad"
    # Response code is 403.
    forbidden = "forbidden"
    # Response code is 404.
    notFound = "notFound"
    # Response code is 405.
    methodNotAllowed = "methodNotAllowed"
    # Response code is 409.
    conflict = "conflict"
    # Response code is 410.
    gone = "gone"
    # Response code is 412.
    preconditionFailed = "preconditionFailed"
    # Response code is 422.
    unprocessable = "unprocessable"