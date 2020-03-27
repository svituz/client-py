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

class ResourceValidationMode(object):
    """ Codes indicating the type of validation to perform.
    URL: http://hl7.org/fhir/resource-validation-mode
    ValueSet: http://hl7.org/fhir/ValueSet/resource-validation-mode
    """
    # The server checks the content, and then checks that the content would be acceptable as a create (e.g. that the
	/// content would not violate any uniqueness constraints).
    create = "create"
    # The server checks the content, and then checks that it would accept it as an update against the nominated
	/// specific resource (e.g. that there are no changes to immutable fields the server does not allow to change and
	/// checking version integrity if appropriate).
    update = "update"
    # The server ignores the content and checks that the nominated resource is allowed to be deleted (e.g. checking
	/// referential integrity rules).
    delete = "delete"
    # The server checks an existing resource (must be nominated by id, not provided as a parameter) as valid against
	/// the nominated profile.
    profile = "profile"