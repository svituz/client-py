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

class DocumentReferenceStatus(object):
    """ The status of the document reference.
    URL: http://hl7.org/fhir/document-reference-status
    ValueSet: http://hl7.org/fhir/ValueSet/document-reference-status
    """
    # This is the current reference for this document.
    CURRENT = "current"
    # This reference has been superseded by another reference.
    SUPERSEDED = "superseded"
    # This reference was created in error.
    ENTEREDINERROR = "entered-in-error"

    allowed_values = [CURRENT, SUPERSEDED, ENTEREDINERROR]