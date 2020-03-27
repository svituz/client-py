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
    notSupported = "not-supported"
    # Batches are  supported.
    batch = "batch"
    # Transactions are supported.
    transaction = "transaction"
    # Both batches and transactions are supported.
    both = "both"