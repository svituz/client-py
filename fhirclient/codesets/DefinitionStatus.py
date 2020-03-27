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

class DefinitionStatus(object):
    """ Codes identifying the lifecycle stage of a definition.
    URL: http://terminology.hl7.org/CodeSystem/definition-status
    ValueSet: http://hl7.org/fhir/ValueSet/definition-status
    """
    # The definition is in the design stage and is not yet considered to be "ready for use".
    draft = "draft"
    # The definition is considered ready for use.
    active = "active"
    # The definition should no longer be used.
    withdrawn = "withdrawn"
    # The authoring/source system does not know which of the status values currently applies for this resource.  Note:
	/// This concept is not to be used for "other" - one of the listed statuses is presumed to apply,  but the
	/// authoring/source system does not know which.
    unknown = "unknown"