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

class SearchComparator(object):
    """ What Search Comparator Codes are supported in search.
    URL: http://hl7.org/fhir/search-comparator
    ValueSet: http://hl7.org/fhir/ValueSet/search-comparator
    """
    """the value for the parameter in the resource is equal to the provided value."""
    EQ = "eq"
    """the value for the parameter in the resource is not equal to the provided value."""
    NE = "ne"
    """the value for the parameter in the resource is greater than the provided value."""
    GT = "gt"
    """the value for the parameter in the resource is less than the provided value."""
    LT = "lt"
    """the value for the parameter in the resource is greater or equal to the provided value."""
    GE = "ge"
    """the value for the parameter in the resource is less or equal to the provided value."""
    LE = "le"
    """the value for the parameter in the resource starts after the provided value."""
    SA = "sa"
    """the value for the parameter in the resource ends before the provided value."""
    EB = "eb"
    """the value for the parameter in the resource is approximately the same to the provided value."""
    AP = "ap"
    allowed_values = ['EQ', 'NE', 'GT', 'LT', 'GE', 'LE', 'SA', 'EB', 'AP']