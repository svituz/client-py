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

class DocumentMode(object):
    """ Whether the application produces or consumes documents.
    URL: http://hl7.org/fhir/document-mode
    ValueSet: http://hl7.org/fhir/ValueSet/document-mode
    """
    """The application produces documents of the specified type."""
    PRODUCER = "producer"
    """The application consumes documents of the specified type."""
    CONSUMER = "consumer"
    allowed_values = ['PRODUCER', 'CONSUMER']