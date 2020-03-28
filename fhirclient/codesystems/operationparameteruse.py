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

class OperationParameterUse(object):
    """ Whether an operation parameter is an input or an output parameter.
    URL: http://hl7.org/fhir/operation-parameter-use
    ValueSet: http://hl7.org/fhir/ValueSet/operation-parameter-use
    """
    # This is an input parameter.
    IN = "in"
    # This is an output parameter.
    OUT = "out"

    allowed_values = [IN, OUT]