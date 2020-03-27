#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coverage)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    
    resource_type = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for the coverage.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ Coverage category such as medical or accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.policyHolder = None
        """ Owner of the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subscriber = None
        """ Subscriber to the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subscriberId = None
        """ ID assigned to the subscriber.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.beneficiary = None
        """ Plan beneficiary.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dependent = None
        """ Dependent number.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.relationship = None
        """ Beneficiary relationship to the subscriber.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.payor = None
        """ Issuer of the policy.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ Additional coverage classifications.
        List of `CoverageClass` items (represented as `dict` in JSON). """
        
        self.order = None
        """ Relative order of the coverage.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.network = None
        """ Insurer network.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.costToBeneficiary = None
        """ Patient payments for services/products.
        List of `CoverageCostToBeneficiary` items (represented as `dict` in JSON). """
        
        self.subrogation = None
        """ Reimbursement to insurer.
        Type `bool`. """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("policyHolder", "policyHolder", fhirreference.FHIRReference, False, None, False, None), 
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False, None), 
            ("subscriberId", "subscriberId", fhirdatatypes.FHIRString, False, None, False, None), 
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, True, None), 
            ("dependent", "dependent", fhirdatatypes.FHIRString, False, None, False, None), 
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("payor", "payor", fhirreference.FHIRReference, True, None, True, None), 
            ("class_fhir", "class", CoverageClass, True, None, False, None), 
            ("order", "order", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("network", "network", fhirdatatypes.FHIRString, False, None, False, None), 
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False, None), 
            ("subrogation", "subrogation", bool, False, None, False, None), 
            ("contract", "contract", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.
    
    A suite of underwriter specific classifiers.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type of class such as 'group' or 'plan'.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Value associated with the type.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Human readable description of the type and value.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CoverageClass, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, True, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ Patient payments for services/products.
    
    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Cost category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ The amount or percentage due from the beneficiary.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ The amount or percentage due from the beneficiary.
        Type `Money` (represented as `dict` in JSON). """
        
        self.exception = None
        """ Exceptions for patient payments.
        List of `CoverageCostToBeneficiaryException` items (represented as `dict` in JSON). """
        
        super(CoverageCostToBeneficiary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True, None), 
            ("valueMoney", "valueMoney", money.Money, False, "value", True, None), 
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False, None), 
        ])
        return js




class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ Exceptions for patient payments.
    
    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Exception category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.period = None
        """ The effective period of the exception.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CoverageCostToBeneficiaryException, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

from fhirclient.models import money

from fhirclient.models import period

from fhirclient.models import quantity

