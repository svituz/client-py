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

class AssertionOperatorType(object):
    """ The type of operator to use for assertion.
    URL: http://hl7.org/fhir/assert-operator-codes
    ValueSet: http://hl7.org/fhir/ValueSet/assert-operator-codes
    """
    # Default value. Equals comparison.
    equals = "equals"
    # Not equals comparison.
    notEquals = "notEquals"
    # Compare value within a known set of values.
    in = "in"
    # Compare value not within a known set of values.
    notIn = "notIn"
    # Compare value to be greater than a known value.
    greaterThan = "greaterThan"
    # Compare value to be less than a known value.
    lessThan = "lessThan"
    # Compare value is empty.
    empty = "empty"
    # Compare value is not empty.
    notEmpty = "notEmpty"
    # Compare value string contains a known value.
    contains = "contains"
    # Compare value string does not contain a known value.
    notContains = "notContains"
    # Evaluate the FHIRPath expression as a boolean condition.
    eval = "eval"