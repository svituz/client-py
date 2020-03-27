#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ChargeItem)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ChargeItem(domainresource.DomainResource):
    """ Item containing charge code(s) associated with the provision of healthcare
    provider products.
    
    The resource ChargeItem describes the provision of healthcare provider
    products for a certain patient, therefore referring not only to the
    product, but containing in addition details of the provision, like date,
    time, amounts and participating organizations and persons. Main Usage of
    the ChargeItem is to enable the billing process and internal cost
    allocation.
    """
    
    resource_type = "ChargeItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.definitionUri = None
        """ Defining information about the code of this charge item.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.definitionCanonical = None
        """ Resource defining the code of this ChargeItem.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.status = None
        """ planned | billable | not-billable | aborted | billed | entered-in-
        error | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.partOf = None
        """ Part of referenced ChargeItem.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        """ A code that identifies the charge, like a billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Individual service was done for/to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the charged service was applied.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When the charged service was applied.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When the charged service was applied.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who performed charged service.
        List of `ChargeItemPerformer` items (represented as `dict` in JSON). """
        
        self.performingOrganization = None
        """ Organization providing the charged service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestingOrganization = None
        """ Organization requesting the charged service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.costCenter = None
        """ Organization that has ownership of the (potential, future) revenue.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Quantity of which the charge item has been serviced.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.bodysite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.factorOverride = None
        """ Factor overriding the associated rules.
        Type `float`. """
        
        self.priceOverride = None
        """ Price overriding the associated rules.
        Type `Money` (represented as `dict` in JSON). """
        
        self.overrideReason = None
        """ Reason for overriding the list price/factor.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.enterer = None
        """ Individual who was entering.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.enteredDate = None
        """ Date the charge item was entered.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.reason = None
        """ Why was the charged  service rendered?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.service = None
        """ Which rendered service is being charged?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.productReference = None
        """ Product charged.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ Product charged.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.account = None
        """ Account to place this charge.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the ChargeItem.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Further information supporting this charge.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ChargeItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("definitionUri", "definitionUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("definitionCanonical", "definitionCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, chargeitemstatus.ChargeItemStatus), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("context", "context", fhirreference.FHIRReference, False, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False, None), 
            ("performer", "performer", ChargeItemPerformer, True, None, False, None), 
            ("performingOrganization", "performingOrganization", fhirreference.FHIRReference, False, None, False, None), 
            ("requestingOrganization", "requestingOrganization", fhirreference.FHIRReference, False, None, False, None), 
            ("costCenter", "costCenter", fhirreference.FHIRReference, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("bodysite", "bodysite", codeableconcept.CodeableConcept, True, None, False, None), 
            ("factorOverride", "factorOverride", float, False, None, False, None), 
            ("priceOverride", "priceOverride", money.Money, False, None, False, None), 
            ("overrideReason", "overrideReason", fhirdatatypes.FHIRString, False, None, False, None), 
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False, None), 
            ("enteredDate", "enteredDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("service", "service", fhirreference.FHIRReference, True, None, False, None), 
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False, None), 
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False, None), 
            ("account", "account", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ChargeItemPerformer(backboneelement.BackboneElement):
    """ Who performed charged service.
    
    Indicates who or what performed or participated in the charged service.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.function = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ChargeItemPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemPerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.codesystems import chargeitemstatus

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import money

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import timing

