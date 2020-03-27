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

class AllergyIntoleranceSubstanceExposureRisk(object):
    """ The risk of an adverse reaction (allergy or intolerance) for this patient upon exposure to the substance (including
pharmaceutical products).
    URL: http://terminology.hl7.org/CodeSystem/allerg-intol-substance-exp-risk
    ValueSet: http://hl7.org/fhir/ValueSet/allerg-intol-substance-exp-risk
    """
    # Known risk of allergy or intolerance reaction upon exposure to the specified substance.
    knownReactionRisk = "known-reaction-risk"
    # No known risk of allergy or intolerance reaction upon exposure to the specified substance.
    noKnownReactionRisk = "no-known-reaction-risk"