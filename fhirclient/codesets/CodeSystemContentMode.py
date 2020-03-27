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

class CodeSystemContentMode(object):
    """ The extent of the content of the code system (the concepts and codes it defines) are represented in a code system
resource.
    URL: http://hl7.org/fhir/codesystem-content-mode
    ValueSet: http://hl7.org/fhir/ValueSet/codesystem-content-mode
    """
    # None of the concepts defined by the code system are included in the code system resource.
    notPresent = "not-present"
    # A few representative concepts are included in the code system resource. There is no useful intent in the subset
	/// choice and there's no process to make it workable: it's not intended to be workable.
    example = "example"
    # A subset of the code system concepts are included in the code system resource. This is a curated subset released
	/// for a specific purpose under the governance of the code system steward, and that the intent, bounds and
	/// consequences of the fragmentation are clearly defined in the fragment or the code system documentation.
	/// Fragments are also known as partitions.
    fragment = "fragment"
    # All the concepts defined by the code system are included in the code system resource.
    complete = "complete"
    # The resource doesn't define any new concepts; it just provides additional designations and properties to another
	/// code system.
    supplement = "supplement"