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

class DefinitionResourceType(object):
    """ A list of all the definition resource types defined in this version of the FHIR specification.
    URL: http://hl7.org/fhir/definition-resource-types
    ValueSet: http://hl7.org/fhir/ValueSet/definition-resource-types
    """
    # This resource allows for the definition of some activity to be performed, independent of a particular patient,
	/// practitioner, or other performance context.
    activityDefinition = "ActivityDefinition"
    # The EventDefinition resource provides a reusable description of when a particular event can occur.
    eventDefinition = "EventDefinition"
    # The Measure resource provides the definition of a quality measure.
    measure = "Measure"
    # A formal computable definition of an operation (on the RESTful interface) or a named query (using the search
	/// interaction).
    operationDefinition = "OperationDefinition"
    # This resource allows for the definition of various types of plans as a sharable, consumable, and executable
	/// artifact. The resource is general enough to support the description of a broad range of clinical artifacts such
	/// as clinical decision support rules, order sets and protocols.
    planDefinition = "PlanDefinition"
    # A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide
	/// detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data
	/// collection.
    questionnaire = "Questionnaire"