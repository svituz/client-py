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

class QuantityComparator(object):
    """ How the Quantity should be understood and represented.
    URL: http://hl7.org/fhir/quantity-comparator
    ValueSet: http://hl7.org/fhir/ValueSet/quantity-comparator
    """
    # The actual value is less than the given value.
    LT = "<"
    # The actual value is less than or equal to the given value.
    LTE = "<="
    # The actual value is greater than or equal to the given value.
    GTE = ">="
    # The actual value is greater than the given value.
    GT = ">"

    allowed_values = [LT, LTE, GTE, GT]