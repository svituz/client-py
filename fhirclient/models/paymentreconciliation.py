#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    
    resource_type = "PaymentReconciliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for a payment reconciliation.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.paymentIssuer = None
        """ Party generating payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        """ Reference to requesting resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestor = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition message.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.paymentDate = None
        """ When payment issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentAmount = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentIdentifier = None
        """ Business identifier for the payment.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Settlement particulars.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.formCode = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.processNote = None
        """ Note concerning processing.
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("period", "period", period.Period, False, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("paymentIssuer", "paymentIssuer", fhirreference.FHIRReference, False, None, False, None), 
            ("request", "request", fhirreference.FHIRReference, False, None, False, None), 
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False, None), 
            ("outcome", "outcome", fhirdatatypes.FHIRCode, False, None, False, claimprocessingcodes.ClaimProcessingCodes), 
            ("disposition", "disposition", fhirdatatypes.FHIRString, False, None, False, None), 
            ("paymentDate", "paymentDate", fhirdatatypes.FHIRDate, False, None, True, None), 
            ("paymentAmount", "paymentAmount", money.Money, False, None, True, None), 
            ("paymentIdentifier", "paymentIdentifier", identifier.Identifier, False, None, False, None), 
            ("detail", "detail", PaymentReconciliationDetail, True, None, False, None), 
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False, None), 
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Settlement particulars.
    
    Distribution of the payment amount for a previously acknowledged payable.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier of the payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.predecessor = None
        """ Business identifier of the prior payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Category of payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request giving rise to the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.submitter = None
        """ Submitter of the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response committing to a payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date of commitment to pay.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.responsible = None
        """ Contact for the response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Recipient of the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.amount = None
        """ Amount allocated to this payable.
        Type `Money` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("predecessor", "predecessor", identifier.Identifier, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("request", "request", fhirreference.FHIRReference, False, None, False, None), 
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False, None), 
            ("response", "response", fhirreference.FHIRReference, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False, None), 
            ("payee", "payee", fhirreference.FHIRReference, False, None, False, None), 
            ("amount", "amount", money.Money, False, None, False, None), 
        ])
        return js




class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Note concerning processing.
    
    A note that describes or explains the processing in a human readable form.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ display | print | printoper.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.text = None
        """ Note explanatory text.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(PaymentReconciliationProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False, notetype.NoteType), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import claimprocessingcodes

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

from fhirclient.models import money

from fhirclient.codesystems import notetype

from fhirclient.models import period

