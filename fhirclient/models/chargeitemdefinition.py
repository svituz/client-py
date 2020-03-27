#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ChargeItemDefinition(domainresource.DomainResource):
    """ Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.
    
    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """
    
    resource_type = "ChargeItemDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this charge item definition, represented
        as a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the charge item definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the charge item definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this charge item definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.derivedFromUri = None
        """ Underlying externally-defined charge item definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.partOf = None
        """ A larger definition of which this particular definition is a
        component or step.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.replaces = None
        """ Completed or terminated request(s) whose function is taken by this
        new request.
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
        """ Natural language description of the charge item definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for charge item definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the charge item definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the charge item definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the charge item definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.code = None
        """ Billing codes or product types this definition applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.instance = None
        """ Instances this definition applies to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.applicability = None
        """ Whether or not the billing code is applicable.
        List of `ChargeItemDefinitionApplicability` items (represented as `dict` in JSON). """
        
        self.propertyGroup = None
        """ Group of properties which are applicable under the same conditions.
        List of `ChargeItemDefinitionPropertyGroup` items (represented as `dict` in JSON). """
        
        super(ChargeItemDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("derivedFromUri", "derivedFromUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("partOf", "partOf", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("replaces", "replaces", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("approvalDate", "approvalDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("lastReviewDate", "lastReviewDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("instance", "instance", fhirreference.FHIRReference, True, None, False, None), 
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False, None), 
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """ Whether or not the billing code is applicable.
    
    Expressions that describe applicability criteria for the billing code.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the condition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.language = None
        """ Language of the expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ChargeItemDefinitionApplicability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("language", "language", fhirdatatypes.FHIRString, False, None, False, None), 
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """ Group of properties which are applicable under the same conditions.
    
    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ Conditions under which the priceComponent is applicable.
        List of `ChargeItemDefinitionApplicability` items (represented as `dict` in JSON). """
        
        self.priceComponent = None
        """ Components of total line item price.
        List of `ChargeItemDefinitionPropertyGroupPriceComponent` items (represented as `dict` in JSON). """
        
        super(ChargeItemDefinitionPropertyGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False, None), 
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False, None), 
        ])
        return js




class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Factor used for calculating this component.
        Type `float`. """
        
        self.amount = None
        """ Monetary amount associated with this component.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ChargeItemDefinitionPropertyGroupPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, invoicepricecomponenttype.InvoicePriceComponentType), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("amount", "amount", money.Money, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import invoicepricecomponenttype

from fhirclient.models import money

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import usagecontext

