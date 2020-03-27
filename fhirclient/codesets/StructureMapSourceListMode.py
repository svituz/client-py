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
    first = "first"
    # Process this rule for all but the first.
    not_first = "not_first"
    # Only process this rule for the last in the list.
    last = "last"
    # Process this rule for all but the last.
    not_last = "not_last"
    # Only process this rule is there is only item.
    only_one = "only_one"