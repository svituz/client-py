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

class PrecisionEstimateType(object):
    """ Method of reporting variability of estimates, such as confidence intervals, interquartile range or standard deviation.
    URL: http://terminology.hl7.org/CodeSystem/precision-estimate-type
    ValueSet: http://hl7.org/fhir/ValueSet/precision-estimate-type
    """
    # confidence interval.
    CI = "CI"
    # interquartile range.
    IQR = "IQR"
    # standard deviation.
    SD = "SD"
    # standard error.
    SE = "SE"