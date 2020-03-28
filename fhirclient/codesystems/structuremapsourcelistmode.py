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

class StructureMapSourceListMode(object):
    """ If field is a list, how to manage the source.
    URL: http://hl7.org/fhir/map-source-list-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-source-list-mode
    """
    # Only process this rule for the first in the list.
    FIRST = "first"
    # Process this rule for all but the first.
    NOT_FIRST = "not_first"
    # Only process this rule for the last in the list.
    LAST = "last"
    # Process this rule for all but the last.
    NOT_LAST = "not_last"
    # Only process this rule is there is only item.
    ONLY_ONE = "only_one"

    allowed_values = [FIRST, NOT_FIRST, LAST, NOT_LAST, ONLY_ONE]