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

class AnimalSpecies(object):
    """ This example value set defines a set of codes that can be used to indicate species of animal patients.
    URL: http://hl7.org/fhir/animal-species
    """
    """Canis lupus familiaris"""
    CANISLF = "canislf"
    """Ovis aries"""
    OVISA = "ovisa"
    """Serinus canaria domestica"""
    SERINUSCD = "serinuscd"
    allowed_values = ['CANISLF', 'OVISA', 'SERINUSCD']