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
    READ = "read"
    # Read the state of a specific version of the resource.
    VREAD = "vread"
    # Update an existing resource by its id.
    UPDATE = "update"
    # Update an existing resource by its id (or create it if it is new).
    UPDATECREATE = "updateCreate"
    # Patch an existing resource by its id.
    PATCH = "patch"
    # Delete a resource.
    DELETE = "delete"
    # Conditionally delete a single resource based on search parameters.
    DELETECONDSINGLE = "deleteCondSingle"
    # Conditionally delete one or more resources based on search parameters.
    DELETECONDMULTIPLE = "deleteCondMultiple"
    # Retrieve the change history for a particular resource or resource type.
    HISTORY = "history"
    # Create a new resource with a server assigned id.
    CREATE = "create"
    # Search based on some filter criteria.
    SEARCH = "search"
    # Update, create or delete a set of resources as independent actions.
    BATCH = "batch"
    # Update, create or delete a set of resources as a single transaction.
    TRANSACTION = "transaction"
    # Get a capability statement for the system.
    CAPABILITIES = "capabilities"
    # Realizes an ActivityDefinition in a specific context
    APPLY = "apply"
    # Closure Table Maintenance
    CLOSURE = "closure"
    # Finding Codes based on supplied properties
    FINDMATCHES = "find-matches"
    # Compare two systems CapabilityStatements
    CONFORMS = "conforms"
    # Aggregates and returns the parameters and data requirements for a resource and all its dependencies as a single
    # module definition
    DATAREQUIREMENTS = "data-requirements"
    # Generate a Document
    DOCUMENT = "document"
    # Request clinical decision support guidance based on a specific decision support module
    EVALUATE = "evaluate"
    # Invoke an eMeasure and obtain the results
    EVALUATEMEASURE = "evaluate-measure"
    # Return all the related information as described in the Encounter or Patient
    EVERYTHING = "everything"
    # Value Set Expansion
    EXPAND = "expand"
    # Find a functional list
    FIND = "find"
    # Invoke a GraphQL query
    GRAPHQL = "graphql"
    # Test if a server implements a client's required operations
    IMPLEMENTS = "implements"
    # Last N Observations Query
    LASTN = "lastn"
    # Concept Look Up and Decomposition
    LOOKUP = "lookup"
    # Find patient matches using MPI based logic
    MATCH = "match"
    # Access a list of profiles, tags, and security labels
    META = "meta"
    # Add profiles, tags, and security labels to a resource
    METAADD = "meta-add"
    # Delete profiles, tags, and security labels for a resource
    METADELETE = "meta-delete"
    # Populate Questionnaire
    POPULATE = "populate"
    # Generate HTML for Questionnaire
    POPULATEHTML = "populatehtml"
    # Generate a link to a Questionnaire completion webpage
    POPULATELINK = "populatelink"
    # Process a message according to the defined event
    PROCESSMESSAGE = "process-message"
    # Build Questionnaire
    QUESTIONNAIRE = "questionnaire"
    # Observation Statistics
    STATS = "stats"
    # Fetch a subset of the CapabilityStatement resource
    SUBSET = "subset"
    # CodeSystem Subsumption Testing
    SUBSUMES = "subsumes"
    # Model Instance Transformation
    TRANSFORM = "transform"
    # Concept Translation
    TRANSLATE = "translate"
    # Validate a resource
    VALIDATE = "validate"
    # ValueSet based Validation
    VALIDATECODE = "validate-code"

    allowed_values = [READ, VREAD, UPDATE, UPDATECREATE, PATCH, DELETE, DELETECONDSINGLE, DELETECONDMULTIPLE, HISTORY, CREATE, SEARCH, BATCH, TRANSACTION, CAPABILITIES, APPLY, CLOSURE, FINDMATCHES, CONFORMS, DATAREQUIREMENTS, DOCUMENT, EVALUATE, EVALUATEMEASURE, EVERYTHING, EXPAND, FIND, GRAPHQL, IMPLEMENTS, LASTN, LOOKUP, MATCH, META, METAADD, METADELETE, POPULATE, POPULATEHTML, POPULATELINK, PROCESSMESSAGE, QUESTIONNAIRE, STATS, SUBSET, SUBSUMES, TRANSFORM, TRANSLATE, VALIDATE, VALIDATECODE]