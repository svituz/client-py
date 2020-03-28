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

class SubstanceCategoryCodes(object):
    """ Substance category codes
    URL: http://terminology.hl7.org/CodeSystem/substance-category
    ValueSet: http://hl7.org/fhir/ValueSet/substance-category
    """
    # A substance that causes an allergic reaction.
    ALLERGEN = "allergen"
    # A substance that is produced by or extracted from a biological source.
    BIOLOGICAL = "biological"
    # A substance that comes directly from a human or an animal (e.g. blood, urine, feces, tears, etc.).
    BODY = "body"
    # Any organic or inorganic substance of a particular molecular identity, including -- (i) any combination of such
    # substances occurring in whole or in part as a result of a chemical reaction or occurring in nature and (ii) any
    # element or uncombined radical (http://www.epa.gov/opptintr/import-export/pubs/importguide.pdf).
    CHEMICAL = "chemical"
    # A food, dietary ingredient, or dietary supplement for human or animal.
    FOOD = "food"
    # A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in man or
    # other animals (Federal Food Drug and Cosmetic Act).
    DRUG = "drug"
    # A finished product which is not normally ingested, absorbed or injected (e.g. steel, iron, wood, plastic and
    # paper).
    MATERIAL = "material"

    allowed_values = [ALLERGEN, BIOLOGICAL, BODY, CHEMICAL, FOOD, DRUG, MATERIAL]