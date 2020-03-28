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

class SortDirection(object):
    """ The possible sort directions, ascending or descending.
    URL: http://hl7.org/fhir/sort-direction
    ValueSet: http://hl7.org/fhir/ValueSet/sort-direction
    """
    # Sort by the value ascending, so that lower values appear first.
    ASCENDING = "ascending"
    # Sort by the value descending, so that lower values appear last.
    DESCENDING = "descending"

    allowed_values = [ASCENDING, DESCENDING]