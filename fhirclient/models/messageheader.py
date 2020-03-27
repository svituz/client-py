#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MessageHeader)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    
    resource_type = "MessageHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.eventCoding = None
        """ Code for the event this message represents or link to event
        definition.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri = None
        """ Code for the event this message represents or link to event
        definition.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.destination = None
        """ Message destination application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
        
        self.sender = None
        """ Real world sender of the message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.enterer = None
        """ The source of the data entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.author = None
        """ The source of the decision.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ Message source application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Final responsibility for event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.response = None
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        
        self.focus = None
        """ The actual content of the message.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ Link to the definition for this message.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True, None), 
            ("eventUri", "eventUri", fhirdatatypes.FHIRUri, False, "event", True, None), 
            ("destination", "destination", MessageHeaderDestination, True, None, False, None), 
            ("sender", "sender", fhirreference.FHIRReference, False, None, False, None), 
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("source", "source", MessageHeaderSource, False, None, True, None), 
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False, None), 
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("response", "response", MessageHeaderResponse, False, None, False, None), 
            ("focus", "focus", fhirreference.FHIRReference, True, None, False, None), 
            ("definition", "definition", fhirdatatypes.FHIRCanonical, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).
    
    The destination application which the message is intended for.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.target = None
        """ Particular delivery destination within the destination.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Actual destination address or id.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.receiver = None
        """ Intended "real-world" recipient for the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("target", "target", fhirreference.FHIRReference, False, None, False, None), 
            ("endpoint", "endpoint", fhirdatatypes.FHIRUrl, False, None, True, None), 
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js




class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Id of original message.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.code = None
        """ ok | transient-error | fatal-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.details = None
        """ Specific list of hints/warnings/errors.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", fhirdatatypes.FHIRId, False, None, True, None), 
            ("code", "code", fhirdatatypes.FHIRCode, False, None, True, responsetype.ResponseType), 
            ("details", "details", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js




class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.
    
    The source application from which this message originated.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.software = None
        """ Name of software running the system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.version = None
        """ Version of software running.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Actual message source address or id.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("software", "software", fhirdatatypes.FHIRString, False, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactpoint.ContactPoint, False, None, False, None), 
            ("endpoint", "endpoint", fhirdatatypes.FHIRUrl, False, None, True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import responsetype

