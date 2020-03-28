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

class ExampleScenarioActorType(object):
    """ The type of actor - system or human.
    URL: http://hl7.org/fhir/examplescenario-actor-type
    ValueSet: http://hl7.org/fhir/ValueSet/examplescenario-actor-type
    """
    # A person.
    PERSON = "person"
    # A system.
    ENTITY = "entity"

    allowed_values = [PERSON, ENTITY]