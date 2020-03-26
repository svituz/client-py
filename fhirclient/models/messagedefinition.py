#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MessageDefinition) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

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
        
        self.allowedResponse = None
        """ Responses to this message.
        List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON). """
        
        self.base = None
        """ Definition this one is based on.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.category = None
        """ consequence | currency | notification.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.description = None
        """ Natural language description of the message definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.eventCoding = None
        """ Event code  or link to the EventDefinition.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri = None
        """ Event code  or link to the EventDefinition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.focus = None
        """ Resource(s) that are the subject of the event.
        List of `MessageDefinitionFocus` items (represented as `dict` in JSON). """
        
        self.graph = None
        """ Canonical reference to a GraphDefinition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.identifier = None
        """ Primary key for the message definition on a given server.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for message definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name for this message definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.parent = None
        """ Protocol/workflow this is part of.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.purpose = None
        """ Why this message definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.replaces = None
        """ Takes the place of.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.responseRequired = None
        """ always | on-error | never | on-success.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this message definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.url = None
        """ Business Identifier for a given MessageDefinition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the message definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(MessageDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend([
            ("allowedResponse", "allowedResponse", MessageDefinitionAllowedResponse, True, None, False),
            ("base", "base", fhirdatatypes.FHIRCanonical, False, None, False),
            ("category", "category", fhirdatatypes.FHIRCode, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, True),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", fhirdatatypes.FHIRUri, False, "event", True),
            ("experimental", "experimental", bool, False, None, False),
            ("focus", "focus", MessageDefinitionFocus, True, None, False),
            ("graph", "graph", fhirdatatypes.FHIRCanonical, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("parent", "parent", fhirdatatypes.FHIRCanonical, True, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("replaces", "replaces", fhirdatatypes.FHIRCanonical, True, None, False),
            ("responseRequired", "responseRequired", fhirdatatypes.FHIRCode, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js



from . import backboneelement

class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ Responses to this message.
    
    Indicates what types of messages may be sent as an application-level
    response to this message.
    """
    
    resource_type = "MessageDefinitionAllowedResponse"
    
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
            ("message", "message", fhirdatatypes.FHIRCanonical, False, None, True),
            ("situation", "situation", fhirdatatypes.FHIRMarkdown, False, None, False),
        ])
        return js




class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ Resource(s) that are the subject of the event.
    
    Identifies the resource (or resources) that are being addressed by the
    event.  For example, the Encounter for an admit message or two Account
    records for a merge.
    """
    
    resource_type = "MessageDefinitionFocus"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of resource.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.max = None
        """ Maximum number of focuses of this type.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum number of focuses of this type.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.profile = None
        """ Profile that must be adhered to by focus.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(MessageDefinitionFocus, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True),
            ("max", "max", fhirdatatypes.FHIRString, False, None, False),
            ("min", "min", fhirdatatypes.FHIRUnsignedInt, False, None, True),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False),
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

