#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ServiceRequest)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.
    
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    
    resource_type = "ServiceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifiers assigned to this order.
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
        
        self.replaces = None
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requisition = None
        """ Composite Request ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ Classification of service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.doNotPerform = None
        """ True if service/procedure should not be performed.
        Type `bool`. """
        
        self.code = None
        """ What is being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderDetail = None
        """ Additional order information.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.quantityQuantity = None
        """ Service amount.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantityRatio = None
        """ Service amount.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.quantityRange = None
        """ Service amount.
        Type `Range` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Individual or Entity the service is ordered for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter in which the request was created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When service should occur.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When service should occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When service should occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Preconditions for service.
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Preconditions for service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ Date request signed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.requester = None
        """ Who/what is requesting service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Requested performer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.locationCode = None
        """ Requested location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ Requested location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Explanation/Justification for procedure or service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Explanation/Justification for service or service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Procedure Samples.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Location on Body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        """ Patient or consumer-oriented instructions.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False, None), 
            ("requisition", "requisition", identifier.Identifier, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, requeststatus.RequestStatus), 
            ("intent", "intent", fhirdatatypes.FHIRCode, False, None, True, requestintent.RequestIntent), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("doNotPerform", "doNotPerform", bool, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, True, None, False, None), 
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False, None), 
            ("quantityRatio", "quantityRatio", ratio.Ratio, False, "quantity", False, None), 
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False, None), 
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False, None), 
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False, None), 
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("requester", "requester", fhirreference.FHIRReference, False, None, False, None), 
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, True, None, False, None), 
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("locationReference", "locationReference", fhirreference.FHIRReference, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False, None), 
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False, None), 
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False, None), 
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("patientInstruction", "patientInstruction", fhirdatatypes.FHIRString, False, None, False, None), 
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False, None), 
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

from fhirclient.models import ratio

from fhirclient.codesystems import requestintent

from fhirclient.codesystems import requestpriority

from fhirclient.codesystems import requeststatus

from fhirclient.models import timing

