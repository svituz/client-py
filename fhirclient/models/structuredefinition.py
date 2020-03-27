#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/StructureDefinition)
#  2020, SMART Health IT.


from . import domainresource

class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
    
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions and constraints on resources and data types.
    """
    
    resource_type = "StructureDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this structure definition, represented as
        a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the structure definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the structure definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this structure definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this structure definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the structure definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for structure definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this structure definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.keyword = None
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.fhirVersion = None
        """ FHIR Version this StructureDefinition targets.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.mapping = None
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ primitive-type | complex-type | resource | logical.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.abstract = None
        """ Whether the structure is abstract.
        Type `bool`. """
        
        self.context = None
        """ If an extension, where it can be used in instances.
        List of `StructureDefinitionContext` items (represented as `dict` in JSON). """
        
        self.contextInvariant = None
        """ FHIRPath invariants - when the extension can be used.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.type = None
        """ Type defined or constrained by this structure.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.baseDefinition = None
        """ Definition that this type is constrained/specialized from.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.derivation = None
        """ specialization | constraint - How relates to base definition.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.snapshot = None
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        
        self.differential = None
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        
        super(StructureDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("keyword", "keyword", coding.Coding, True, None, False),
            ("fhirVersion", "fhirVersion", fhirdatatypes.FHIRCode, False, None, False),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, True),
            ("abstract", "abstract", bool, False, None, True),
            ("context", "context", StructureDefinitionContext, True, None, False),
            ("contextInvariant", "contextInvariant", fhirdatatypes.FHIRString, True, None, False),
            ("type", "type", fhirdatatypes.FHIRUri, False, None, True),
            ("baseDefinition", "baseDefinition", fhirdatatypes.FHIRCanonical, False, None, False),
            ("derivation", "derivation", fhirdatatypes.FHIRCode, False, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
        ])
        return js



from . import backboneelement

class StructureDefinitionContext(backboneelement.BackboneElement):
    """ If an extension, where it can be used in instances.
    
    Identifies the types of resource or data type elements to which the
    extension can be applied.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ fhirpath | element | extension.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.expression = None
        """ Where the extension can be used in instances.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(StructureDefinitionContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionContext, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, True),
        ])
        return js




class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.
    
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js




class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.comment = None
        """ Versions, Issues, Scope limitations etc..
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(StructureDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", fhirdatatypes.FHIRId, False, None, True),
            ("uri", "uri", fhirdatatypes.FHIRUri, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js




class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a standalone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
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
    from . import elementdefinition
except ImportError:
    elementdefinition = sys.modules[__package__ + '.elementdefinition']

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

