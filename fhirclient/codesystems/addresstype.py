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

class AddressType(object):
    """ The type of an address (physical / postal).
    URL: http://hl7.org/fhir/address-type
    ValueSet: http://hl7.org/fhir/ValueSet/address-type
    """
    """Mailing addresses - PO Boxes and care-of addresses."""
    POSTAL = "postal"
    """A physical address that can be visited."""
    PHYSICAL = "physical"
    """An address that is both physical and postal."""
    BOTH = "both"
    allowed_values = ['POSTAL', 'PHYSICAL', 'BOTH']