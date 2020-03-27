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

class ExpansionProcessingRule(object):
    """ Defines how concepts are processed into the expansion when it's for UI presentation.
    URL: http://terminology.hl7.org/CodeSystem/expansion-processing-rule
    ValueSet: http://hl7.org/fhir/ValueSet/expansion-processing-rule
    """
    """The expansion (when in UI mode) includes all codes *and* any defined groups (in extensions)."""
    ALLCODES = "all-codes"
    """The expanion (when in UI mode) lists the groups, and then any codes that have not been included in a group."""
    UNGROUPED = "ungrouped"
    """The expansion (when in UI mode) only includes the defined groups."""
    GROUPSONLY = "groups-only"
    allowed_values = ['ALLCODES', 'UNGROUPED', 'GROUPSONLY']