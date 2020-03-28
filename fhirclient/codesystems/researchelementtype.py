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

class ResearchElementType(object):
    """ The possible types of research elements (E.g. Population, Exposure, Outcome).
    URL: http://hl7.org/fhir/research-element-type
    ValueSet: http://hl7.org/fhir/ValueSet/research-element-type
    """
    # The element defines the population that forms the basis for research.
    POPULATION = "population"
    # The element defines an exposure within the population that is being researched.
    EXPOSURE = "exposure"
    # The element defines an outcome within the population that is being researched.
    OUTCOME = "outcome"

    allowed_values = [POPULATION, EXPOSURE, OUTCOME]