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

class ListMode(object):
    """ The processing mode that applies to this list.
    URL: http://hl7.org/fhir/list-mode
    ValueSet: http://hl7.org/fhir/ValueSet/list-mode
    """
    # This list is the master list, maintained in an ongoing fashion with regular updates as the real world list it is
    # tracking changes.
    WORKING = "working"
    # This list was prepared as a snapshot. It should not be assumed to be current.
    SNAPSHOT = "snapshot"
    # A point-in-time list that shows what changes have been made or recommended.  E.g. a discharge medication list
    # showing what was added and removed during an encounter.
    CHANGES = "changes"

    allowed_values = [WORKING, SNAPSHOT, CHANGES]