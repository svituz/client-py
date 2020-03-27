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

class TestScriptOperationCode(object):
    """ This value set defines a set of codes that are used to indicate the supported operations of a testing engine or tool.
    URL: http://terminology.hl7.org/CodeSystem/testscript-operation-codes
    ValueSet: http://hl7.org/fhir/ValueSet/testscript-operation-codes
    """
    # Read the current state of the resource.
    read = "read"
    # Read the state of a specific version of the resource.
    vread = "vread"
    # Update an existing resource by its id.
    update = "update"
    # Update an existing resource by its id (or create it if it is new).
    updateCreate = "updateCreate"
    # Patch an existing resource by its id.
    patch = "patch"
    # Delete a resource.
    delete = "delete"
    # Conditionally delete a single resource based on search parameters.
    deleteCondSingle = "deleteCondSingle"
    # Conditionally delete one or more resources based on search parameters.
    deleteCondMultiple = "deleteCondMultiple"
    # Retrieve the change history for a particular resource or resource type.
    history = "history"
    # Create a new resource with a server assigned id.
    create = "create"
    # Search based on some filter criteria.
    search = "search"
    # Update, create or delete a set of resources as independent actions.
    batch = "batch"
    # Update, create or delete a set of resources as a single transaction.
    transaction = "transaction"
    # Get a capability statement for the system.
    capabilities = "capabilities"
    # Realizes an ActivityDefinition in a specific context
    apply = "apply"
    # Closure Table Maintenance
    closure = "closure"
    # Finding Codes based on supplied properties
    findMatches = "find-matches"
    # Compare two systems CapabilityStatements
    conforms = "conforms"
    # Aggregates and returns the parameters and data requirements for a resource and all its dependencies as a single
	/// module definition
    dataRequirements = "data-requirements"
    # Generate a Document
    document = "document"
    # Request clinical decision support guidance based on a specific decision support module
    evaluate = "evaluate"
    # Invoke an eMeasure and obtain the results
    evaluateMeasure = "evaluate-measure"
    # Return all the related information as described in the Encounter or Patient
    everything = "everything"
    # Value Set Expansion
    expand = "expand"
    # Find a functional list
    find = "find"
    # Invoke a GraphQL query
    graphql = "graphql"
    # Test if a server implements a client's required operations
    implements = "implements"
    # Last N Observations Query
    lastn = "lastn"
    # Concept Look Up and Decomposition
    lookup = "lookup"
    # Find patient matches using MPI based logic
    match = "match"
    # Access a list of profiles, tags, and security labels
    meta = "meta"
    # Add profiles, tags, and security labels to a resource
    metaAdd = "meta-add"
    # Delete profiles, tags, and security labels for a resource
    metaDelete = "meta-delete"
    # Populate Questionnaire
    populate = "populate"
    # Generate HTML for Questionnaire
    populatehtml = "populatehtml"
    # Generate a link to a Questionnaire completion webpage
    populatelink = "populatelink"
    # Process a message according to the defined event
    processMessage = "process-message"
    # Build Questionnaire
    questionnaire = "questionnaire"
    # Observation Statistics
    stats = "stats"
    # Fetch a subset of the CapabilityStatement resource
    subset = "subset"
    # CodeSystem Subsumption Testing
    subsumes = "subsumes"
    # Model Instance Transformation
    transform = "transform"
    # Concept Translation
    translate = "translate"
    # Validate a resource
    validate = "validate"
    # ValueSet based Validation
    validateCode = "validate-code"