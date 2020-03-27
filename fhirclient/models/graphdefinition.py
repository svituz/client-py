#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/GraphDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

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
        
        self.url = None
        """ Canonical identifier for this graph definition, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.version = None
        """ Business version of the graph definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this graph definition (computer friendly).
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
        """ Natural language description of the graph definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for graph definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this graph definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.start = None
        """ Type of resource at which the graph starts.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profile on base resource.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.link = None
        """ Links this graph makes rules about.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        super(GraphDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("start", "start", fhirdatatypes.FHIRCode, False, None, True, resourcetype.ResourceType), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("link", "link", GraphDefinitionLink, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class GraphDefinitionLink(backboneelement.BackboneElement):
    """ Links this graph makes rules about.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ Path in the resource that contains the link.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.sliceName = None
        """ Which slice (if profiled).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum occurrences for this link.
        Type `int`. """
        
        self.max = None
        """ Maximum occurrences for this link.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Why this link is specified.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.target = None
        """ Potential target for the link.
        List of `GraphDefinitionLinkTarget` items (represented as `dict` in JSON). """
        
        super(GraphDefinitionLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, False, None), 
            ("sliceName", "sliceName", fhirdatatypes.FHIRString, False, None, False, None), 
            ("min", "min", int, False, None, False, None), 
            ("max", "max", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("target", "target", GraphDefinitionLinkTarget, True, None, False, None), 
        ])
        return js




class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ Potential target for the link.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type of resource this link refers to.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.params = None
        """ Criteria for reverse lookup.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profile for the target resource.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.compartment = None
        """ Compartment Consistency Rules.
        List of `GraphDefinitionLinkTargetCompartment` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Additional links from target resource.
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        super(GraphDefinitionLinkTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, resourcetype.ResourceType), 
            ("params", "params", fhirdatatypes.FHIRString, False, None, False, None), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False, None), 
            ("link", "link", GraphDefinitionLink, True, None, False, None), 
        ])
        return js




class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ Compartment Consistency Rules.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.use = None
        """ condition | requirement.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.rule = None
        """ identical | matching | different | custom.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.expression = None
        """ Custom rule, as a FHIRPath expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Documentation for FHIRPath expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(GraphDefinitionLinkTargetCompartment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("use", "use", fhirdatatypes.FHIRCode, False, None, True, graphcompartmentuse.GraphCompartmentUse), 
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, compartmenttype.CompartmentType), 
            ("rule", "rule", fhirdatatypes.FHIRCode, False, None, True, graphcompartmentrule.GraphCompartmentRule), 
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import compartmenttype

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import graphcompartmentrule

from fhirclient.codesystems import graphcompartmentuse

from fhirclient.codesystems import publicationstatus

from fhirclient.codesystems import resourcetype

from fhirclient.models import usagecontext

