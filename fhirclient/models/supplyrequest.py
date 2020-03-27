#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SupplyRequest)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.
    
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    
    resource_type = "SupplyRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for SupplyRequest.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.itemCodeableConcept = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The requested amount of the item indicated.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ Ordered item details.
        List of `SupplyRequestParameter` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the request should be fulfilled.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When the request should be fulfilled.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When the request should be fulfilled.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ When the request was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.requester = None
        """ Individual making the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supplier = None
        """ Who is intended to fulfill the request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ The reason why the supply item was requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ The reason why the supply item was requested.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.deliverFrom = None
        """ The origin of the supply.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deliverTo = None
        """ The destination of the supply.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, supplyrequeststatus.SupplyRequestStatus), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True, None), 
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, True, None), 
            ("parameter", "parameter", SupplyRequestParameter, True, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False, None), 
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("requester", "requester", fhirreference.FHIRReference, False, None, False, None), 
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("deliverFrom", "deliverFrom", fhirreference.FHIRReference, False, None, False, None), 
            ("deliverTo", "deliverTo", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class SupplyRequestParameter(backboneelement.BackboneElement):
    """ Ordered item details.
    
    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Item detail.
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
        
        super(SupplyRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False, None), 
            ("valueRange", "valueRange", range.Range, False, "value", False, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.codesystems import requestpriority

from fhirclient.codesystems import supplyrequeststatus

from fhirclient.models import timing

