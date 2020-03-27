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

class ImmunizationRecommendationStatusCodes(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the status of the patient towards perceived immunity against a vaccine
preventable disease. This value set is provided as a suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-recommendation-status
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-recommendation-status
    """
    # The patient is due for their next vaccination.
    due = "due"
    # The patient is considered overdue for their next vaccination.
    overdue = "overdue"
    # The patient is immune to the target disease and further immunization against the disease is not likely to
	/// provide benefit.
    immune = "immune"
    # The patient is contraindicated for futher doses.
    contraindicated = "contraindicated"
    # The patient is fully protected and no further doses are recommended.
    complete = "complete"