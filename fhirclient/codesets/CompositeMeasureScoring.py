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

class CompositeMeasureScoring(object):
    """ The composite scoring method of the measure.
    URL: http://terminology.hl7.org/CodeSystem/composite-measure-scoring
    ValueSet: http://hl7.org/fhir/ValueSet/composite-measure-scoring
    """
    # Opportunity scoring combines the scores from component measures by combining the numerators and denominators for
	/// each component.
    opportunity = "opportunity"
    # All-or-nothing scoring includes an individual in the numerator of the composite measure if they are in the
	/// numerators of all of the component measures in which they are in the denominator.
    allOrNothing = "all-or-nothing"
    # Linear scoring gives an individual a score based on the number of numerators in which they appear.
    linear = "linear"
    # Weighted scoring gives an individual a score based on a weighted factor for each component numerator in which
	/// they appear.
    weighted = "weighted"