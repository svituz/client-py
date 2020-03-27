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

class KnowledgeResourceType(object):
    """ A list of all the knowledge resource types defined in this version of the FHIR specification.
    URL: http://hl7.org/fhir/knowledge-resource-types
    ValueSet: http://hl7.org/fhir/ValueSet/knowledge-resource-types
    """
    # The definition of a specific activity to be taken, independent of any particular patient or context.
    activityDefinition = "ActivityDefinition"
    # A set of codes drawn from one or more code systems.
    codeSystem = "CodeSystem"
    # A map from one set of concepts to one or more other concepts.
    conceptMap = "ConceptMap"
    # Represents a library of quality improvement components.
    library = "Library"
    # A quality measure definition.
    measure = "Measure"
    # The definition of a plan for a series of actions, independent of any specific patient or context.
    planDefinition = "PlanDefinition"
    # Structural Definition.
    structureDefinition = "StructureDefinition"
    # A Map of relationships between 2 structures that can be used to transform data.
    structureMap = "StructureMap"
    # A set of codes drawn from one or more code systems.
    valueSet = "ValueSet"