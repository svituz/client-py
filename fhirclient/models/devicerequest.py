#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceRequest)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_type = "DeviceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.priorRequest = None
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.codeReference = None
        """ Device requested.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.codeCodeableConcept = None
        """ Device requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ Device details.
        List of `DeviceRequestParameter` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Focus of request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter motivating request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ Desired time or schedule for use.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ Desired time or schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ Desired time or schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ When recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.requester = None
        """ Who/what is requesting diagnostics.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ Filler role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Requested Filler.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Coded Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Linked Reason for request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Notes or comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, True, None, False, None), 
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, requeststatus.RequestStatus), 
            ("intent", "intent", fhirdatatypes.FHIRCode, False, None, True, requestintent.RequestIntent), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("codeReference", "codeReference", fhirreference.FHIRReference, False, "code", True, None), 
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, False, "code", True, None), 
            ("parameter", "parameter", DeviceRequestParameter, True, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False, None), 
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("requester", "requester", fhirreference.FHIRReference, False, None, False, None), 
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False, None), 
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.
    
    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Device detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Value of detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of detail.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value of detail.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ Value of detail.
        Type `bool`. """
        
        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False, None), 
            ("valueRange", "valueRange", range.Range, False, "value", False, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.codesystems import requestintent

from fhirclient.codesystems import requestpriority

from fhirclient.codesystems import requeststatus

from fhirclient.models import timing

