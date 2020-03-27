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

class AllergyIntoleranceType(object):
    """ Identification of the underlying physiological mechanism for a Reaction Risk.
    URL: http://hl7.org/fhir/allergy-intolerance-type
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-type
    """
    # A propensity for hypersensitive reaction(s) to a substance.  These reactions are most typically type I
	/// hypersensitivity, plus other "allergy-like" reactions, including pseudoallergy.
    allergy = "allergy"
    # A propensity for adverse reactions to a substance that is not judged to be allergic or "allergy-like".  These
	/// reactions are typically (but not necessarily) non-immune.  They are to some degree idiosyncratic and/or patient-
	/// specific (i.e. are not a reaction that is expected to occur with most or all patients given similar
	/// circumstances).
    intolerance = "intolerance"