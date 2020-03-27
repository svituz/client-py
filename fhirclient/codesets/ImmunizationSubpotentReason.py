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

class ImmunizationSubpotentReason(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the reason why a dose is considered to be subpotent. This value set is
provided as a suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-subpotent-reason
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-subpotent-reason
    """
    # The full volume of the dose was not administered to the patient.
    partial = "partial"
    # The vaccine experienced a cold chain break.
    coldchainbreak = "coldchainbreak"
    # The vaccine was recalled by the manufacturer.
    recall = "recall"