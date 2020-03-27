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

class EvidenceVariantState(object):
    """ Used for results by exposure in variant states such as low-risk, medium-risk and high-risk states.
    URL: http://terminology.hl7.org/CodeSystem/evidence-variant-state
    ValueSet: http://hl7.org/fhir/ValueSet/evidence-variant-state
    """
    """low risk estimate."""
    LOWRISK = "low-risk"
    """medium risk estimate."""
    MEDIUMRISK = "medium-risk"
    """high risk estimate."""
    HIGHRISK = "high-risk"
    allowed_values = ['LOWRISK', 'MEDIUMRISK', 'HIGHRISK']