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
    patient = "Patient"
    # The compartment definition is for the encounter compartment.
    encounter = "Encounter"
    # The compartment definition is for the related-person compartment.
    relatedPerson = "RelatedPerson"
    # The compartment definition is for the practitioner compartment.
    practitioner = "Practitioner"
    # The compartment definition is for the device compartment.
    device = "Device"