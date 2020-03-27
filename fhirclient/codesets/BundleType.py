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

class BundleType(object):
    """ Indicates the purpose of a bundle - how it is intended to be used.
    URL: http://hl7.org/fhir/bundle-type
    ValueSet: http://hl7.org/fhir/ValueSet/bundle-type
    """
    # The bundle is a document. The first resource is a Composition.
    document = "document"
    # The bundle is a message. The first resource is a MessageHeader.
    message = "message"
    # The bundle is a transaction - intended to be processed by a server as an atomic commit.
    transaction = "transaction"
    # The bundle is a transaction response. Because the response is a transaction response, the transaction has
	/// succeeded, and all responses are error free.
    transactionResponse = "transaction-response"
    # The bundle is a set of actions - intended to be processed by a server as a group of independent actions.
    batch = "batch"
    # The bundle is a batch response. Note that as a batch, some responses may indicate failure and others success.
    batchResponse = "batch-response"
    # The bundle is a list of resources from a history interaction on a server.
    history = "history"
    # The bundle is a list of resources returned as a result of a search/query interaction, operation, or message.
    searchset = "searchset"
    # The bundle is a set of resources collected into a single package for ease of distribution that imposes no
	/// processing obligations or behavioral rules beyond persistence.
    collection = "collection"