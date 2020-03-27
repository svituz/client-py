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

class IssueType(object):
    """ A code that describes the type of issue.
    URL: http://hl7.org/fhir/issue-type
    ValueSet: http://hl7.org/fhir/ValueSet/issue-type
    """
    # Content invalid against the specification or a profile.
    invalid = "invalid"
    # A structural issue in the content such as wrong namespace, unable to parse the content completely, invalid
	/// syntax, etc.
    structure = "structure"
    # A required element is missing.
    required = "required"
    # An element or header value is invalid.
    value = "value"
    # A content validation rule failed - e.g. a schematron rule.
    invariant = "invariant"
    # An authentication/authorization/permissions issue of some kind.
    security = "security"
    # The client needs to initiate an authentication process.
    login = "login"
    # The user or system was not able to be authenticated (either there is no process, or the proferred token is
	/// unacceptable).
    unknown = "unknown"
    # User session expired; a login may be required.
    expired = "expired"
    # The user does not have the rights to perform this action.
    forbidden = "forbidden"
    # Some information was not or might not have been returned due to business rules, consent or privacy rules, or
	/// access permission constraints.  This information may be accessible through alternate processes.
    suppressed = "suppressed"
    # Processing issues. These are expected to be final e.g. there is no point resubmitting the same content
	/// unchanged.
    processing = "processing"
    # The interaction, operation, resource or profile is not supported.
    notSupported = "not-supported"
    # An attempt was made to create a duplicate record.
    duplicate = "duplicate"
    # Multiple matching records were found when the operation required only one match.
    multipleMatches = "multiple-matches"
    # The reference provided was not found. In a pure RESTful environment, this would be an HTTP 404 error, but this
	/// code may be used where the content is not found further into the application architecture.
    notFound = "not-found"
    # The reference pointed to content (usually a resource) that has been deleted.
    deleted = "deleted"
    # Provided content is too long (typically, this is a denial of service protection type of error).
    tooLong = "too-long"
    # The code or system could not be understood, or it was not valid in the context of a particular ValueSet.code.
    codeInvalid = "code-invalid"
    # An extension was found that was not acceptable, could not be resolved, or a modifierExtension was not
	/// recognized.
    extension = "extension"
    # The operation was stopped to protect server resources; e.g. a request for a value set expansion on all of SNOMED
	/// CT.
    tooCostly = "too-costly"
    # The content/operation failed to pass some business rule and so could not proceed.
    businessRule = "business-rule"
    # Content could not be accepted because of an edit conflict (i.e. version aware updates). (In a pure RESTful
	/// environment, this would be an HTTP 409 error, but this code may be used where the conflict is discovered further
	/// into the application architecture.).
    conflict = "conflict"
    # Transient processing issues. The system receiving the message may be able to resubmit the same content once an
	/// underlying issue is resolved.
    transient = "transient"
    # A resource/record locking failure (usually in an underlying database).
    lockError = "lock-error"
    # The persistent store is unavailable; e.g. the database is down for maintenance or similar action, and the
	/// interaction or operation cannot be processed.
    noStore = "no-store"
    # An unexpected internal error has occurred.
    exception = "exception"
    # An internal timeout has occurred.
    timeout = "timeout"
    # Not all data sources typically accessed could be reached or responded in time, so the returned information might
	/// not be complete (applies to search interactions and some operations).
    incomplete = "incomplete"
    # The system is not prepared to handle this request due to load management.
    throttled = "throttled"
    # A message unrelated to the processing success of the completed operation (examples of the latter include things
	/// like reminders of password expiry, system maintenance times, etc.).
    informational = "informational"