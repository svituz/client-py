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

class StructureDefinitionKind(object):
    """ Defines the type of structure that a definition is describing.
    URL: http://hl7.org/fhir/structure-definition-kind
    ValueSet: http://hl7.org/fhir/ValueSet/structure-definition-kind
    """
    """A primitive type that has a value and an extension. These can be used throughout complex datatype, Resource and
	/// extension definitions. Only the base specification can define primitive types."""
    PRIMITIVETYPE = "primitive-type"
    """A  complex structure that defines a set of data elements that is suitable for use in 'resources'. The base
	/// specification defines a number of complex types, and other specifications can define additional types. These
	/// structures do not have a maintained identity."""
    COMPLEXTYPE = "complex-type"
    """A 'resource' - a directed acyclic graph of elements that aggregrates other types into an identifiable entity.
	/// The base FHIR resources are defined by the FHIR specification itself but other 'resources' can be defined in
	/// additional specifications (though these will not be recognised as 'resources' by the FHIR specification (i.e.
	/// they do not get end-points etc, or act as the targets of references in FHIR defined resources - though other
	/// specificatiosn can treat them this way)."""
    RESOURCE = "resource"
    """A pattern or a template that is not intended to be a real resource or complex type."""
    LOGICAL = "logical"
    allowed_values = ['PRIMITIVETYPE', 'COMPLEXTYPE', 'RESOURCE', 'LOGICAL']