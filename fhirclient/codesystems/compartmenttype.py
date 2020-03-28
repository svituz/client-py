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

class CompartmentType(object):
    """ Which type a compartment definition describes.
    URL: http://hl7.org/fhir/compartment-type
    ValueSet: http://hl7.org/fhir/ValueSet/compartment-type
    """
    # The compartment definition is for the patient compartment.
    PATIENT = "Patient"
    # The compartment definition is for the encounter compartment.
    ENCOUNTER = "Encounter"
    # The compartment definition is for the related-person compartment.
    RELATEDPERSON = "RelatedPerson"
    # The compartment definition is for the practitioner compartment.
    PRACTITIONER = "Practitioner"
    # The compartment definition is for the device compartment.
    DEVICE = "Device"

    allowed_values = [PATIENT, ENCOUNTER, RELATEDPERSON, PRACTITIONER, DEVICE]