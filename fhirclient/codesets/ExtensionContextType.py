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

class ExtensionContextType(object):
    """ How an extension context is interpreted.
    URL: http://hl7.org/fhir/extension-context-type
    ValueSet: http://hl7.org/fhir/ValueSet/extension-context-type
    """
    # The context is all elements that match the FHIRPath query found in the expression.
    fhirpath = "fhirpath"
    # The context is any element that has an ElementDefinition.id that matches that found in the expression. This
	/// includes ElementDefinition Ids that have slicing identifiers. The full path for the element is
	/// [url]#[elementid]. If there is no #, the Element id is one defined in the base specification.
    element = "element"
    # The context is a particular extension from a particular StructureDefinition, and the expression is just a uri
	/// that identifies the extension.
    extension = "extension"