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

class MedicationKnowledgeCharacteristicCodes(object):
    """ MedicationKnowledge Characteristic Codes
    URL: http://terminology.hl7.org/CodeSystem/medicationknowledge-characteristic
    ValueSet: http://hl7.org/fhir/ValueSet/medicationknowledge-characteristic
    """
    """Identyifying marks on product"""
    IMPRINTCD = "imprintcd"
    """Description of size of the product"""
    SIZE = "size"
    """Description of the shape of the product"""
    SHAPE = "shape"
    """Description of the color of the product"""
    COLOR = "color"
    """Description of the coating of the product"""
    COATING = "coating"
    """Description of the scoring of the product"""
    SCORING = "scoring"
    """Description of the Logo of the product"""
    LOGO = "logo"
    allowed_values = ['IMPRINTCD', 'SIZE', 'SHAPE', 'COLOR', 'COATING', 'SCORING', 'LOGO']