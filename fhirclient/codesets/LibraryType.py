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

class LibraryType(object):
    """ The type of knowledge asset this library contains.
    URL: http://terminology.hl7.org/CodeSystem/library-type
    ValueSet: http://hl7.org/fhir/ValueSet/library-type
    """
    # The resource is a shareable library of formalized knowledge.
    logicLibrary = "logic-library"
    # The resource is a definition of an information model.
    modelDefinition = "model-definition"
    # The resource is a collection of knowledge assets.
    assetCollection = "asset-collection"
    # The resource defines the dependencies, parameters, and data requirements for a particular module or evaluation
	/// context.
    moduleDefinition = "module-definition"