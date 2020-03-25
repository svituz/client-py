#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CodeSystem) on 2020-03-25.
#  2020, SMART Health IT.


from . import domainresource

class CodeSystem(domainresource.DomainResource):
    """ Declares the existence of and describes a code system or code system
    supplement.
    
    The CodeSystem resource is used to declare the existence of and describe a
    code system or code system supplement and its key properties, and
    optionally define a part or all of its content.
    """
    
    resource_type = "CodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.caseSensitive = None
        """ If code comparison is case sensitive.
        Type `bool`. """
        
        self.compositional = None
        """ If code system defines a compositional grammar.
        Type `bool`. """
        
        self.concept = None
        """ Concepts in the code system.
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.content = None
        """ not-present | example | fragment | complete | supplement.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.count = None
        """ Total concepts in the code system.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the code system.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.filter = None
        """ Filter that can be used in a value set.
        List of `CodeSystemFilter` items (represented as `dict` in JSON). """
        
        self.hierarchyMeaning = None
        """ grouped-by | is-a | part-of | classified-with.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the code system (business identifier).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for code system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this code system (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.property = None
        """ Additional information supplied about each concept.
        List of `CodeSystemProperty` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.purpose = None
        """ Why this code system is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.supplements = None
        """ Canonical URL of Code System this adds designations and properties
        to.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this code system (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.url = None
        """ Canonical identifier for this code system, represented as a URI
        (globally unique) (Coding.system).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.valueSet = None
        """ Canonical reference to the value set with entire code system.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.version = None
        """ Business version of the code system (Coding.version).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.versionNeeded = None
        """ If definitions are not stable.
        Type `bool`. """
        
        super(CodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", fhirdatatypes.FHIRCode, False, None, True),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("count", "count", fhirdatatypes.FHIRUnsignedInt, False, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("filter", "filter", CodeSystemFilter, True, None, False),
            ("hierarchyMeaning", "hierarchyMeaning", fhirdatatypes.FHIRCode, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("property", "property", CodeSystemProperty, True, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("supplements", "supplements", fhirdatatypes.FHIRCanonical, False, None, False),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("valueSet", "valueSet", fhirdatatypes.FHIRCanonical, False, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("versionNeeded", "versionNeeded", bool, False, None, False),
        ])
        return js



from . import backboneelement

class CodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.
    
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meanings of the hierarchical relationships are.
    """
    
    resource_type = "CodeSystemConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies concept.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.concept = None
        """ Child Concepts (is-a/contains/categorizes).
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Formal definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.designation = None
        """ Additional representations for the concept.
        List of `CodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ Text to display to the user.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.property = None
        """ Property value for the concept.
        List of `CodeSystemConceptProperty` items (represented as `dict` in JSON). """
        
        super(CodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("definition", "definition", fhirdatatypes.FHIRString, False, None, False),
            ("designation", "designation", CodeSystemConceptDesignation, True, None, False),
            ("display", "display", fhirdatatypes.FHIRString, False, None, False),
            ("property", "property", CodeSystemConceptProperty, True, None, False),
        ])
        return js




class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    
    resource_type = "CodeSystemConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Human language of the designation.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.use = None
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ The text value for this designation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CodeSystemConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", fhirdatatypes.FHIRCode, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """ Property value for the concept.
    
    A property value for this concept.
    """
    
    resource_type = "CodeSystemConceptProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Reference to CodeSystem.property.code.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ Value of the property for this concept.
        Type `bool`. """
        
        self.valueCode = None
        """ Value of the property for this concept.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueCoding = None
        """ Value of the property for this concept.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ Value of the property for this concept.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Value of the property for this concept.
        Type `float`. """
        
        self.valueInteger = None
        """ Value of the property for this concept.
        Type `int`. """
        
        self.valueString = None
        """ Value of the property for this concept.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CodeSystemConceptProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True),
        ])
        return js




class CodeSystemFilter(backboneelement.BackboneElement):
    """ Filter that can be used in a value set.
    
    A filter that can be used in a value set compose statement when selecting
    concepts using a filter.
    """
    
    resource_type = "CodeSystemFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies the filter.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.description = None
        """ How or why the filter is used.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.operator = None
        """ = | is-a | descendent-of | is-not-a | regex | in | not-in |
        generalizes | exists.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.value = None
        """ What to use for the value.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CodeSystemFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("operator", "operator", fhirdatatypes.FHIRCode, True, None, True),
            ("value", "value", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class CodeSystemProperty(backboneelement.BackboneElement):
    """ Additional information supplied about each concept.
    
    A property defines an additional slot through which additional information
    can be provided about a concept.
    """
    
    resource_type = "CodeSystemProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Identifies the property on the concepts, and when referred to in
        operations.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.description = None
        """ Why the property is defined, and/or what it conveys.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ code | Coding | string | integer | boolean | dateTime | decimal.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.uri = None
        """ Formal identifier for the property.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        super(CodeSystemProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("uri", "uri", fhirdatatypes.FHIRUri, False, None, False),
        ])
        return js



import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']

try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

