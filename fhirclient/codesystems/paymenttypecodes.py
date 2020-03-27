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

class PaymentTypeCodes(object):
    """ This value set includes sample Payment Type codes.
    URL: http://terminology.hl7.org/CodeSystem/payment-type
    ValueSet: http://hl7.org/fhir/ValueSet/payment-type
    """
    """The amount is partial or complete settlement of the amounts due."""
    PAYMENT = "payment"
    """The amount is an adjustment regarding claims already paid."""
    ADJUSTMENT = "adjustment"
    """The amount is an advance against future claims."""
    ADVANCE = "advance"
    allowed_values = ['PAYMENT', 'ADJUSTMENT', 'ADVANCE']