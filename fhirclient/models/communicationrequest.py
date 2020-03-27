#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.
    
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    
    resource_type = "CommunicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Fulfills plan or proposal.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
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
        
        self.doNotPerform = None
        """ True if request is prohibiting action.
        Type `bool`. """
        
        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.about = None
        """ Resources that pertain to this communication request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When scheduled.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When scheduled.
        Type `Period` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ When request transitioned to being actionable.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.requester = None
        """ Who/what is requesting service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why is communication needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why is communication needed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about communication request.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(CommunicationRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False, None), 
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, requeststatus.RequestStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("doNotPerform", "doNotPerform", bool, False, None, False, None), 
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("about", "about", fhirreference.FHIRReference, True, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("payload", "payload", CommunicationRequestPayload, True, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("requester", "requester", fhirreference.FHIRReference, False, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False, None), 
            ("sender", "sender", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) to be communicated to the recipient.
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
        
        super(CommunicationRequestPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend([
            ("contentString", "contentString", fhirdatatypes.FHIRString, False, "content", True, None), 
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True, None), 
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import requestpriority

from fhirclient.codesystems import requeststatus

