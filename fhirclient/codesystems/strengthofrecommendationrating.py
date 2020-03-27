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

class StrengthOfRecommendationRating(object):
    """ A rating system that describes the strength of the recommendation, such as the GRADE, DynaMed, or HGPS systems.
    URL: http://terminology.hl7.org/CodeSystem/recommendation-strength
    ValueSet: http://hl7.org/fhir/ValueSet/recommendation-strength
    """
    """Strong recommendation."""
    STRONG = "strong"
    """Weak recommendation."""
    WEAK = "weak"
    allowed_values = ['STRONG', 'WEAK']