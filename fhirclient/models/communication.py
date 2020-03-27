#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Communication)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.
    
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """
    
    resource_type = "Communication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this communication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.inResponseTo = None
        """ Reply to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.topic = None
        """ Description of the purpose/content.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.about = None
        """ Resources that pertain to this communication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sent = None
        """ When sent.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.received = None
        """ When received.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why was communication done?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationPayload` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the communication.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(Communication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Communication, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("inResponseTo", "inResponseTo", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, eventstatus.EventStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("topic", "topic", codeableconcept.CodeableConcept, False, None, False, None), 
            ("about", "about", fhirreference.FHIRReference, True, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("sent", "sent", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("received", "received", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False, None), 
            ("sender", "sender", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("payload", "payload", CommunicationPayload, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentString = None
        """ Message part content.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contentAttachment = None
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Message part content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CommunicationPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentString", "contentString", fhirdatatypes.FHIRString, False, "content", True, None), 
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True, None), 
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.codesystems import eventstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import requestpriority

