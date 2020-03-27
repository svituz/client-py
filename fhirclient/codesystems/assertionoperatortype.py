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
    """Default value. Equals comparison."""
    EQUALS = "equals"
    """Not equals comparison."""
    NOTEQUALS = "notEquals"
    """Compare value within a known set of values."""
    IN = "in"
    """Compare value not within a known set of values."""
    NOTIN = "notIn"
    """Compare value to be greater than a known value."""
    GREATERTHAN = "greaterThan"
    """Compare value to be less than a known value."""
    LESSTHAN = "lessThan"
    """Compare value is empty."""
    EMPTY = "empty"
    """Compare value is not empty."""
    NOTEMPTY = "notEmpty"
    """Compare value string contains a known value."""
    CONTAINS = "contains"
    """Compare value string does not contain a known value."""
    NOTCONTAINS = "notContains"
    """Evaluate the FHIRPath expression as a boolean condition."""
    EVAL = "eval"
    allowed_values = ['EQUALS', 'NOTEQUALS', 'IN', 'NOTIN', 'GREATERTHAN', 'LESSTHAN', 'EMPTY', 'NOTEMPTY', 'CONTAINS', 'NOTCONTAINS', 'EVAL']