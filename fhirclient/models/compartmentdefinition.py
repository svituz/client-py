#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class CompartmentDefinition(domainresource.DomainResource):
    """ Compartment Definition for a resource.
    
    A compartment definition that defines how resources are accessed on a
    server.
    """
    
    resource_type = "CompartmentDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this compartment definition, represented
        as a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.version = None
        """ Business version of the compartment definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this compartment definition (computer friendly).
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
        """ Natural language description of the compartment definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this compartment definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.code = None
        """ Patient | Encounter | RelatedPerson | Practitioner | Device.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.search = None
        """ Whether the search syntax is supported.
        Type `bool`. """
        
        self.resource = None
        """ How a resource is related to the compartment.
        List of `CompartmentDefinitionResource` items (represented as `dict` in JSON). """
        
        super(CompartmentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, compartmenttype.CompartmentType), 
            ("search", "search", bool, False, None, True, None), 
            ("resource", "resource", CompartmentDefinitionResource, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """ How a resource is related to the compartment.
    
    Information about how a resource is related to the compartment.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Name of resource type.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.param = None
        """ Search Parameter Name, or chained parameters.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.documentation = None
        """ Additional documentation about the resource and compartment.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CompartmentDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, resourcetype.ResourceType), 
            ("param", "param", fhirdatatypes.FHIRString, True, None, False, None), 
            ("documentation", "documentation", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import compartmenttype

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import publicationstatus

from fhirclient.codesystems import resourcetype

from fhirclient.models import usagecontext

