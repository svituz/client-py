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

class PaymentStatusCodes(object):
    """ This value set includes a sample set of Payment Status codes.
    URL: http://terminology.hl7.org/CodeSystem/paymentstatus
    ValueSet: http://hl7.org/fhir/ValueSet/payment-status
    """
    """The payment has been sent physically or electronically."""
    PAID = "paid"
    """The payment has been received by the payee."""
    CLEARED = "cleared"
    allowed_values = ['PAID', 'CLEARED']