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

class ActionCardinalityBehavior(object):
    """ Defines behavior for an action or a group for how many times that item may be repeated.
    URL: http://hl7.org/fhir/action-cardinality-behavior
    ValueSet: http://hl7.org/fhir/ValueSet/action-cardinality-behavior
    """
    # The action may only be selected one time.
    single = "single"
    # The action may be selected multiple times.
    multiple = "multiple"