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

class EnteralFormulaAdditiveTypeCode(object):
    """ EnteralFormulaAdditiveType: Codes for the type of modular component such as protein, carbohydrate or fiber to be
provided in addition to or mixed with the base formula. This value set is provided as a suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/entformula-additive
    ValueSet: http://hl7.org/fhir/ValueSet/entformula-additive
    """
    # Modular lipid enteral formula component
    lipid = "lipid"
    # Modular protein enteral formula component
    protein = "protein"
    # Modular carbohydrate enteral formula component
    carbohydrate = "carbohydrate"
    # Modular fiber enteral formula component
    fiber = "fiber"
    # Added water
    water = "water"