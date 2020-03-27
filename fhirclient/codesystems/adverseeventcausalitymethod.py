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

class AdverseEventCausalityMethod(object):
    """ TODO.
    URL: http://terminology.hl7.org/CodeSystem/adverse-event-causality-method
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-causality-method
    """
    """probabilityScale"""
    PROBABILITYSCALE = "ProbabilityScale"
    """bayesian"""
    BAYESIAN = "Bayesian"
    """checklist"""
    CHECKLIST = "Checklist"
    allowed_values = ['PROBABILITYSCALE', 'BAYESIAN', 'CHECKLIST']