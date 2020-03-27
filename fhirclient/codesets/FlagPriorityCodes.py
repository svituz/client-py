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

class FlagPriorityCodes(object):
    """ This value set is provided as an exemplar. The value set is driven by IHE Table B.8-4: Abnormal Flags, Alert Priority.
    URL: http://hl7.org/fhir/flag-priority-code
    ValueSet: http://hl7.org/fhir/ValueSet/flag-priority
    """
    # No alarm.
    PN = "PN"
    # Low priority.
    PL = "PL"
    # Medium priority.
    PM = "PM"
    # High priority.
    PH = "PH"