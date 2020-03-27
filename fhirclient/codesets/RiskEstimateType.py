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

class RiskEstimateType(object):
    """ Whether the risk estimate is dichotomous, continuous or qualitative and the specific type of risk estimate (eg
proportion or median).
    URL: http://terminology.hl7.org/CodeSystem/risk-estimate-type
    ValueSet: http://hl7.org/fhir/ValueSet/risk-estimate-type
    """
    # dichotomous measure (present or absent) reported as a ratio compared to the denominator of 1 (A percentage is a
	/// proportion with denominator of 100).
    proportion = "proportion"
    # A special use case where the proportion is derived from a formula rather than derived from summary evidence.
    derivedProportion = "derivedProportion"
    # continuous numerical measure reported as an average.
    mean = "mean"
    # continuous numerical measure reported as the middle of the range.
    median = "median"
    # descriptive measure reported as total number of items.
    count = "count"
    # descriptive measure reported as narrative.
    descriptive = "descriptive"