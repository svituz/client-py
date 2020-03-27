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

class BiologicallyDerivedProductStatus(object):
    """ Biologically Derived Product Status.
    URL: http://hl7.org/fhir/product-status
    ValueSet: http://hl7.org/fhir/ValueSet/product-status
    """
    """Product is currently available for use."""
    AVAILABLE = "available"
    """Product is not currently available for use."""
    UNAVAILABLE = "unavailable"
    allowed_values = ['AVAILABLE', 'UNAVAILABLE']