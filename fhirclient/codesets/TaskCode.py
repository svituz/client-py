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

class TaskCode(object):
    """ Codes indicating the type of action that is expected to be performed
    URL: http://hl7.org/fhir/CodeSystem/task-code
    ValueSet: http://hl7.org/fhir/ValueSet/task-code
    """
    # Take what actions are needed to transition the focus resource from 'draft' to 'active' or 'in-progress', as
	/// appropriate for the resource type.  This may involve additing additional content, approval, validation, etc.
    approve = "approve"
    # Act to perform the actions defined in the focus request.  This might result in a 'more assertive' request (order
	/// for a plan or proposal, filler order for a placer order), but is intend to eventually result in events.  The
	/// degree of fulfillment requested might be limited by Task.restriction.
    fulfill = "fulfill"
    # Abort, cancel or withdraw the focal resource, as appropriate for the type of resource.
    abort = "abort"
    # Replace the focal resource with the specified input resource
    replace = "replace"
    # Update the focal resource of the owning system to reflect the content specified as the Task.focus
    change = "change"
    # Transition the focal resource from 'active' or 'in-progress' to 'suspended'
    suspend = "suspend"
    # Transition the focal resource from 'suspended' to 'active' or 'in-progress' as appropriate for the resource
	/// type.
    resume = "resume"