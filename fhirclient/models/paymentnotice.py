#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PaymentNotice)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    
    resource_type = "PaymentNotice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for the payment noctice.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payment = None
        """ Payment reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.paymentDate = None
        """ Payment or clearing date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payee = None
        """ Party being paid.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Party being notified.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.amount = None
        """ Monetary amount of the payment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentStatus = None
        """ Issued or cleared Status of the payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("request", "request", fhirreference.FHIRReference, False, None, False, None), 
            ("response", "response", fhirreference.FHIRReference, False, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("provider", "provider", fhirreference.FHIRReference, False, None, False, None), 
            ("payment", "payment", fhirreference.FHIRReference, False, None, True, None), 
            ("paymentDate", "paymentDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("payee", "payee", fhirreference.FHIRReference, False, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, True, None), 
            ("amount", "amount", money.Money, False, None, True, None), 
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

from fhirclient.models import money

