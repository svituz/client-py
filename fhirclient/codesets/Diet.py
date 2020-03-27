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

class Diet(object):
    """ This value set defines a set of codes that can be used to indicate dietary preferences or restrictions a patient may
have.
    URL: http://terminology.hl7.org/CodeSystem/diet
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-diet
    """
    # Food without meat, poultry or seafood.
    vegetarian = "vegetarian"
    # Excludes dairy products.
    dairyFree = "dairy-free"
    # Excludes ingredients containing nuts.
    nutFree = "nut-free"
    # Excludes ingredients containing gluten.
    glutenFree = "gluten-free"
    # Food without meat, poultry, seafood, eggs, dairy products and other animal-derived substances.
    vegan = "vegan"
    # Foods that conform to Islamic law.
    halal = "halal"
    # Foods that conform to Jewish dietary law.
    kosher = "kosher"