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

class MeasureScoring(object):
    """ The scoring type of the measure.
    URL: http://terminology.hl7.org/CodeSystem/measure-scoring
    ValueSet: http://hl7.org/fhir/ValueSet/measure-scoring
    """
    # The measure score is defined using a proportion.
    PROPORTION = "proportion"
    # The measure score is defined using a ratio.
    RATIO = "ratio"
    # The score is defined by a calculation of some quantity.
    CONTINUOUSVARIABLE = "continuous-variable"
    # The measure is a cohort definition.
    COHORT = "cohort"

    allowed_values = [PROPORTION, RATIO, CONTINUOUSVARIABLE, COHORT]