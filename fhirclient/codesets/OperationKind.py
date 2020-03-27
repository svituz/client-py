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

class OperationKind(object):
    """ Whether an operation is a normal operation or a query.
    URL: http://hl7.org/fhir/operation-kind
    ValueSet: http://hl7.org/fhir/ValueSet/operation-kind
    """
    # This operation is invoked as an operation.
    operation = "operation"
    # This operation is a named query, invoked using the search mechanism.
    query = "query"