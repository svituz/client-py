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

class SearchEntryMode(object):
    """ Why an entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey
information or warning information about the search process.
    URL: http://hl7.org/fhir/search-entry-mode
    ValueSet: http://hl7.org/fhir/ValueSet/search-entry-mode
    """
    # This resource matched the search specification.
    match = "match"
    # This resource is returned because it is referred to from another resource in the search set.
    include = "include"
    # An OperationOutcome that provides additional information about the processing of a search.
    outcome = "outcome"