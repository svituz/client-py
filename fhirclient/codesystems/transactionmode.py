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

class TransactionMode(object):
    """ A code that indicates how transactions are supported.
    URL: http://hl7.org/fhir/transaction-mode
    ValueSet: http://hl7.org/fhir/ValueSet/transaction-mode
    """
    # Neither batch or transaction is supported.
    NOTSUPPORTED = "not-supported"
    # Batches are  supported.
    BATCH = "batch"
    # Transactions are supported.
    TRANSACTION = "transaction"
    # Both batches and transactions are supported.
    BOTH = "both"

    allowed_values = [NOTSUPPORTED, BATCH, TRANSACTION, BOTH]