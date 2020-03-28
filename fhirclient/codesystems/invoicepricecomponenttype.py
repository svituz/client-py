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

class InvoicePriceComponentType(object):
    """ Codes indicating the kind of the price component.
    URL: http://hl7.org/fhir/invoice-priceComponentType
    ValueSet: http://hl7.org/fhir/ValueSet/invoice-priceComponentType
    """
    # the amount is the base price used for calculating the total price before applying surcharges, discount or taxes.
    BASE = "base"
    # the amount is a surcharge applied on the base price.
    SURCHARGE = "surcharge"
    # the amount is a deduction applied on the base price.
    DEDUCTION = "deduction"
    # the amount is a discount applied on the base price.
    DISCOUNT = "discount"
    # the amount is the tax component of the total price.
    TAX = "tax"
    # the amount is of informational character, it has not been applied in the calculation of the total price.
    INFORMATIONAL = "informational"

    allowed_values = [BASE, SURCHARGE, DEDUCTION, DISCOUNT, TAX, INFORMATIONAL]