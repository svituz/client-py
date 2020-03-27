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

class AllergyIntoleranceCriticality(object):
    """ Estimate of the potential clinical harm, or seriousness, of a reaction to an identified substance.
    URL: http://hl7.org/fhir/allergy-intolerance-criticality
    ValueSet: http://hl7.org/fhir/ValueSet/allergy-intolerance-criticality
    """
    # Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ
	/// system failure.
    low = "low"
    # Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ
	/// system failure.
    high = "high"
    # Unable to assess the worst case result of a future exposure.
    unableToAssess = "unable-to-assess"