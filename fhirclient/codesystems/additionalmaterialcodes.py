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

class AdditionalMaterialCodes(object):
    """ This value set includes sample additional material type codes.
    URL: http://hl7.org/fhir/additionalmaterials
    ValueSet: http://hl7.org/fhir/ValueSet/additionalmaterials
    """
    # XRay
    XRAY = "xray"
    # Image
    IMAGE = "image"
    # Email
    EMAIL = "email"
    # Model
    MODEL = "model"
    # Document
    DOCUMENT = "document"
    # Other
    OTHER = "other"

    allowed_values = [XRAY, IMAGE, EMAIL, MODEL, DOCUMENT, OTHER]