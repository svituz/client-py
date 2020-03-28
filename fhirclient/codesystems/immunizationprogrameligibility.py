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

class ImmunizationProgramEligibility(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the patient's eligibility for a vaccination program. This value set is
provided as a suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-program-eligibility
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-program-eligibility
    """
    # The patient is not eligible for the funding program.
    INELIGIBLE = "ineligible"
    # The patient is eligible for the funding program because they are uninsured.
    UNINSURED = "uninsured"

    allowed_values = [INELIGIBLE, UNINSURED]