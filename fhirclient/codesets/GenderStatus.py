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

class GenderStatus(object):
    """ This example value set defines a set of codes that can be used to indicate the current state of the animal's
reproductive organs.
    URL: http://hl7.org/fhir/animal-genderstatus
    ValueSet: http://hl7.org/fhir/ValueSet/animal-genderstatus
    """
    # The animal has been sterilized, castrated or otherwise made infertile.
    neutered = "neutered"
    # The animal's reproductive organs are intact.
    intact = "intact"
    # Unable to determine whether the animal has been neutered.
    unknown = "unknown"