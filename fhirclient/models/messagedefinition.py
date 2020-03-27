#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MessageDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MessageDefinition(domainresource.DomainResource):
    """ A resource that defines a type of message that can be exchanged between
    systems.
    
    Defines the characteristics of a message that can be shared between
    systems, including the type of event that initiates the message, the
    content to be transmitted and what response(s), if any, are permitted.
    """
    
    resource_type = "MessageDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Business Identifier for a given MessageDefinition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Primary key for the message definition on a given server.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the message definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this message definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this message definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.replaces = None
        """ Takes the place of.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
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
        """ Natural language description of the message definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for message definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this message definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.base = None
        """ Definition this one is based on.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.parent = None
        """ Protocol/workflow this is part of.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.eventCoding = None
        """ Event code  or link to the EventDefinition.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri = None
        """ Event code  or link to the EventDefinition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.category = None
        """ consequence | currency | notification.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.focus = None
        """ Resource(s) that are the subject of the event.
        List of `MessageDefinitionFocus` items (represented as `dict` in JSON). """
        
        self.responseRequired = None
        """ always | on-error | never | on-success.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.allowedResponse = None
        """ Responses to this message.
        List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON). """
        
        self.graph = None
        """ Canonical reference to a GraphDefinition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        super(MessageDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("replaces", "replaces", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("base", "base", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("parent", "parent", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True, None), 
            ("eventUri", "eventUri", fhirdatatypes.FHIRUri, False, "event", True, None), 
            ("category", "category", fhirdatatypes.FHIRCode, False, None, False, messagesignificancecategory.MessageSignificanceCategory), 
            ("focus", "focus", MessageDefinitionFocus, True, None, False, None), 
            ("responseRequired", "responseRequired", fhirdatatypes.FHIRCode, False, None, False, messageheaderresponserequest.MessageheaderResponseRequest), 
            ("allowedResponse", "allowedResponse", MessageDefinitionAllowedResponse, True, None, False, None), 
            ("graph", "graph", fhirdatatypes.FHIRCanonical, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.
    
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.message = None
        """ Reference to allowed message definition response.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.situation = None
        """ When should this response be used.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(MessageDefinitionAllowedResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinitionAllowedResponse, self).elementProperties()
        js.extend([
            ("message", "message", fhirdatatypes.FHIRCanonical, False, None, True, None), 
            ("situation", "situation", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
        ])
        return js




class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.
    
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of resource.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profile that must be adhered to by focus.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum number of focuses of this type.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.max = None
        """ Maximum number of focuses of this type.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(MessageDefinitionFocus, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, resourcetype.ResourceType), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("min", "min", fhirdatatypes.FHIRUnsignedInt, False, None, True, None), 
            ("max", "max", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.models import identifier

from fhirclient.codesystems import messageheaderresponserequest

from fhirclient.codesystems import messagesignificancecategory

from fhirclient.codesystems import publicationstatus

from fhirclient.codesystems import resourcetype

from fhirclient.models import usagecontext

