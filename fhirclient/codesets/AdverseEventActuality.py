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

class AdverseEventActuality(object):
    """ Overall nature of the adverse event, e.g. real or potential.
    URL: http://hl7.org/fhir/adverse-event-actuality
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-actuality
    """
    # The adverse event actually happened regardless of whether anyone was affected or harmed.
    actual = "actual"
    # A potential adverse event.
    potential = "potential"