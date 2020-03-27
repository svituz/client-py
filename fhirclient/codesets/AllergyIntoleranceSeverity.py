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

class AllergyIntoleranceSeverity(object):
    """ Clinical assessment of the severity of a reaction event as a whole, potentially considering multiple different
manifestations.
    URL: http://hl7.org/fhir/reaction-event-severity
    ValueSet: http://hl7.org/fhir/ValueSet/reaction-event-severity
    """
    # Causes mild physiological effects.
    mild = "mild"
    # Causes moderate physiological effects.
    moderate = "moderate"
    # Causes severe physiological effects.
    severe = "severe"