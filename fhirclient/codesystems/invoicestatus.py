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

class InvoiceStatus(object):
    """ Codes identifying the lifecycle stage of an Invoice.
    URL: http://hl7.org/fhir/invoice-status
    ValueSet: http://hl7.org/fhir/ValueSet/invoice-status
    """
    # the invoice has been prepared but not yet finalized.
    DRAFT = "draft"
    # the invoice has been finalized and sent to the recipient.
    ISSUED = "issued"
    # the invoice has been balaced / completely paid.
    BALANCED = "balanced"
    # the invoice was cancelled.
    CANCELLED = "cancelled"
    # the invoice was determined as entered in error before it was issued.
    ENTEREDINERROR = "entered-in-error"

    allowed_values = [DRAFT, ISSUED, BALANCED, CANCELLED, ENTEREDINERROR]