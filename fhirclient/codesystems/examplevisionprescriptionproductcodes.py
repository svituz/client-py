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

class ExampleVisionPrescriptionProductCodes(object):
    """ This value set includes a smattering of Prescription Product codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct
    ValueSet: http://hl7.org/fhir/ValueSet/vision-product
    """
    # A lens to be fitted to a frame to comprise a pair of glasses.
    LENS = "lens"
    # A lens to be fitted for wearing directly on an eye.
    CONTACT = "contact"

    allowed_values = [LENS, CONTACT]