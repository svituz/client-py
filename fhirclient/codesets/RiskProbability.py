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

class RiskProbability(object):
    """ Codes representing the likelihood of a particular outcome in a risk assessment.
    URL: http://terminology.hl7.org/CodeSystem/risk-probability
    ValueSet: http://hl7.org/fhir/ValueSet/risk-probability
    """
    # The specified outcome is exceptionally unlikely.
    negligible = "negligible"
    # The specified outcome is possible but unlikely.
    low = "low"
    # The specified outcome has a reasonable likelihood of occurrence.
    moderate = "moderate"
    # The specified outcome is more likely to occur than not.
    high = "high"
    # The specified outcome is effectively guaranteed.
    certain = "certain"