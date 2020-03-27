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

class ClaimItemTypeCodes(object):
    """ This value set includes sample Item Type codes.
    URL: http://hl7.org/fhir/ex-claimitemtype
    ValueSet: http://hl7.org/fhir/ValueSet/fm-itemtype
    """
    """A group of products and/or Services, amount ar the summary or detail level products and services."""
    GROUP = "group"
    """A billed product line item."""
    PRODUCT = "product"
    """A billed service line item."""
    SERVICE = "service"
    allowed_values = ['GROUP', 'PRODUCT', 'SERVICE']