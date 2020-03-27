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
    # the value for the parameter in the resource is equal to the provided value.
    eq = "eq"
    # the value for the parameter in the resource is not equal to the provided value.
    ne = "ne"
    # the value for the parameter in the resource is greater than the provided value.
    gt = "gt"
    # the value for the parameter in the resource is less than the provided value.
    lt = "lt"
    # the value for the parameter in the resource is greater or equal to the provided value.
    ge = "ge"
    # the value for the parameter in the resource is less or equal to the provided value.
    le = "le"
    # the value for the parameter in the resource starts after the provided value.
    sa = "sa"
    # the value for the parameter in the resource ends before the provided value.
    eb = "eb"
    # the value for the parameter in the resource is approximately the same to the provided value.
    ap = "ap"