#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Invoice)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Invoice(domainresource.DomainResource):
    """ Invoice containing ChargeItems from an Account.
    
    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """
    
    resource_type = "Invoice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | issued | balanced | cancelled | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.cancelledReason = None
        """ Reason for cancellation of this Invoice.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ Type of Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Recipient(s) of goods and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Recipient of this invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ Invoice date / posting date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.participant = None
        """ Participant in creation of this Invoice.
        List of `InvoiceParticipant` items (represented as `dict` in JSON). """
        
        self.issuer = None
        """ Issuing Organization of Invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.account = None
        """ Account that is being balanced.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lineItem = None
        """ Line items of this Invoice.
        List of `InvoiceLineItem` items (represented as `dict` in JSON). """
        
        self.totalPriceComponent = None
        """ Components of Invoice total.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.totalNet = None
        """ Net total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalGross = None
        """ Gross total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentTerms = None
        """ Payment details.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.note = None
        """ Comments made about the invoice.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(Invoice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, invoicestatus.InvoiceStatus), 
            ("cancelledReason", "cancelledReason", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("participant", "participant", InvoiceParticipant, True, None, False, None), 
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False, None), 
            ("account", "account", fhirreference.FHIRReference, False, None, False, None), 
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False, None), 
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False, None), 
            ("totalNet", "totalNet", money.Money, False, None, False, None), 
            ("totalGross", "totalGross", money.Money, False, None, False, None), 
            ("paymentTerms", "paymentTerms", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class InvoiceLineItem(backboneelement.BackboneElement):
    """ Line items of this Invoice.
    
    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ Sequence number of line item.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.chargeItemReference = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.chargeItemCodeableConcept = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priceComponent = None
        """ Components of total line item price.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        super(InvoiceLineItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("sequence", "sequence", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("chargeItemReference", "chargeItemReference", fhirreference.FHIRReference, False, "chargeItem", True, None), 
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", codeableconcept.CodeableConcept, False, "chargeItem", True, None), 
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False, None), 
        ])
        return js




class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
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
        
        super(InvoiceLineItemPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, invoicepricecomponenttype.InvoicePriceComponentType), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("amount", "amount", money.Money, False, None, False, None), 
        ])
        return js




class InvoiceParticipant(backboneelement.BackboneElement):
    """ Participant in creation of this Invoice.
    
    Indicates who or what performed or participated in the charged service.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ Type of involvement in creation of this Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Individual who was involved.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(InvoiceParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import invoicepricecomponenttype

from fhirclient.codesystems import invoicestatus

from fhirclient.models import money

