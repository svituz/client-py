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

class AssertionDirectionType(object):
    """ The type of direction to use for assertion.
    URL: http://hl7.org/fhir/assert-direction-codes
    ValueSet: http://hl7.org/fhir/ValueSet/assert-direction-codes
    """
    # The assertion is evaluated on the response. This is the default value.
    response = "response"
    # The assertion is evaluated on the request.
    request = "request"