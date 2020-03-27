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
    # HTTP DELETE operation.
    delete = "delete"
    # HTTP GET operation.
    get = "get"
    # HTTP OPTIONS operation.
    options = "options"
    # HTTP PATCH operation.
    patch = "patch"
    # HTTP POST operation.
    post = "post"
    # HTTP PUT operation.
    put = "put"
    # HTTP HEAD operation.
    head = "head"