#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GraphDefinition) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

class GraphDefinition(domainresource.DomainResource):
    """ Definition of a graph of resources.
    
    A formal computable definition of a graph of resources - that is, a
    coherent set of resources that form a graph by following references. The
    Graph Definition resource defines a set and makes rules about the set.
    """
    
    resource_type = "GraphDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the graph definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.jurisdiction = None
        """ Intended jurisdiction for graph definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Links this graph makes rules about.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this graph definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profile on base resource.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.purpose = None
        """ Why this graph definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.start = None
        """ Type of resource at which the graph starts.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.url = None
        """ Canonical identifier for this graph definition, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the graph definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(GraphDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, True),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("start", "start", fhirdatatypes.FHIRCode, False, None, True),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js



from . import backboneelement

class GraphDefinitionLink(backboneelement.BackboneElement):
    """ Links this graph makes rules about.
    """
    
    resource_type = "GraphDefinitionLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Why this link is specified.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.max = None
        """ Maximum occurrences for this link.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum occurrences for this link.
        Type `int`. """
        
        self.path = None
        """ Path in the resource that contains the link.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.sliceName = None
        """ Which slice (if profiled).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.target = None
        """ Potential target for the link.
        List of `GraphDefinitionLinkTarget` items (represented as `dict` in JSON). """
        
        super(GraphDefinitionLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("max", "max", fhirdatatypes.FHIRString, False, None, False),
            ("min", "min", int, False, None, False),
            ("path", "path", fhirdatatypes.FHIRString, False, None, False),
            ("sliceName", "sliceName", fhirdatatypes.FHIRString, False, None, False),
            ("target", "target", GraphDefinitionLinkTarget, True, None, False),
        ])
        return js




class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ Potential target for the link.
    """
    
    resource_type = "GraphDefinitionLinkTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        """ Compartment Consistency Rules.
        List of `GraphDefinitionLinkTargetCompartment` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Additional links from target resource.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        self.params = None
        """ Criteria for reverse lookup.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profile for the target resource.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.type = None
        """ Type of resource this link refers to.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(GraphDefinitionLinkTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("params", "params", fhirdatatypes.FHIRString, False, None, False),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js




class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ Compartment Consistency Rules.
    """
    
    resource_type = "GraphDefinitionLinkTargetCompartment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.description = None
        """ Documentation for FHIRPath expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expression = None
        """ Custom rule, as a FHIRPath expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.rule = None
        """ identical | matching | different | custom.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.use = None
        """ condition | requirement.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(GraphDefinitionLinkTargetCompartment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False),
            ("rule", "rule", fhirdatatypes.FHIRCode, False, None, True),
            ("use", "use", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js



import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

