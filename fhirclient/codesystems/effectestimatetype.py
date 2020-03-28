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

class EffectEstimateType(object):
    """ Whether the effect estimate is an absolute effect estimate (absolute difference) or a relative effect estimate (relative
difference), and the specific type of effect estimate (eg relative risk or median difference).
    URL: http://terminology.hl7.org/CodeSystem/effect-estimate-type
    ValueSet: http://hl7.org/fhir/ValueSet/effect-estimate-type
    """
    # relative risk (a type of relative effect estimate).
    RELATIVERR = "relative-RR"
    # odds ratio (a type of relative effect estimate).
    RELATIVEOR = "relative-OR"
    # hazard ratio (a type of relative effect estimate).
    RELATIVEHR = "relative-HR"
    # absolute risk difference (a type of absolute effect estimate).
    ABSOLUTEARD = "absolute-ARD"
    # mean difference (a type of absolute effect estimate).
    ABSOLUTEMEANDIFF = "absolute-MeanDiff"
    # standardized mean difference (a type of absolute effect estimate).
    ABSOLUTESMD = "absolute-SMD"
    # median difference (a type of absolute effect estimate).
    ABSOLUTEMEDIANDIFF = "absolute-MedianDiff"

    allowed_values = [RELATIVERR, RELATIVEOR, RELATIVEHR, ABSOLUTEARD, ABSOLUTEMEANDIFF, ABSOLUTESMD, ABSOLUTEMEDIANDIFF]