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

class MeasureImprovementNotation(object):
    """ Observation values that indicate what change in a measurement value or score is indicative of an improvement in the
measured item or scored issue.
    URL: http://terminology.hl7.org/CodeSystem/measure-improvement-notation
    ValueSet: http://hl7.org/fhir/ValueSet/measure-improvement-notation
    """
    # Improvement is indicated as an increase in the score or measurement (e.g. Higher score indicates better
	/// quality).
    increase = "increase"
    # Improvement is indicated as a decrease in the score or measurement (e.g. Lower score indicates better quality).
    decrease = "decrease"