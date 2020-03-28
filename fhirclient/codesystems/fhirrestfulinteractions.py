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

class FHIRRestfulInteractions(object):
    """ The set of interactions defined by the RESTful part of the FHIR specification.
    URL: http://hl7.org/fhir/restful-interaction
    ValueSet: http://hl7.org/fhir/ValueSet/restful-interaction
    """
    # Read the current state of the resource.
    READ = "read"
    # Read the state of a specific version of the resource.
    VREAD = "vread"
    # Update an existing resource by its id (or create it if it is new).
    UPDATE = "update"
    # Update an existing resource by posting a set of changes to it.
    PATCH = "patch"
    # Delete a resource.
    DELETE = "delete"
    # Retrieve the change history for a particular resource, type of resource, or the entire system.
    HISTORY = "history"
    # Retrieve the change history for a particular resource.
    HISTORYINSTANCE = "history-instance"
    # Retrieve the change history for all resources of a particular type.
    HISTORYTYPE = "history-type"
    # Retrieve the change history for all resources on a system.
    HISTORYSYSTEM = "history-system"
    # Create a new resource with a server assigned id.
    CREATE = "create"
    # Search a resource type or all resources based on some filter criteria.
    SEARCH = "search"
    # Search all resources of the specified type based on some filter criteria.
    SEARCHTYPE = "search-type"
    # Search all resources based on some filter criteria.
    SEARCHSYSTEM = "search-system"
    # Get a Capability Statement for the system.
    CAPABILITIES = "capabilities"
    # Update, create or delete a set of resources as a single transaction.
    TRANSACTION = "transaction"
    # perform a set of a separate interactions in a single http operation
    BATCH = "batch"
    # Perform an operation as defined by an OperationDefinition.
    OPERATION = "operation"

    allowed_values = [READ, VREAD, UPDATE, PATCH, DELETE, HISTORY, HISTORYINSTANCE, HISTORYTYPE, HISTORYSYSTEM, CREATE, SEARCH, SEARCHTYPE, SEARCHSYSTEM, CAPABILITIES, TRANSACTION, BATCH, OPERATION]