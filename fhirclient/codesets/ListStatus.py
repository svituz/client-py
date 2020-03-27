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

class ListStatus(object):
    """ The current state of the list.
    URL: http://hl7.org/fhir/list-status
    ValueSet: http://hl7.org/fhir/ValueSet/list-status
    """
    # The list is considered to be an active part of the patient's record.
    current = "current"
    # The list is "old" and should no longer be considered accurate or relevant.
    retired = "retired"
    # The list was never accurate.  It is retained for medico-legal purposes only.
    enteredInError = "entered-in-error"