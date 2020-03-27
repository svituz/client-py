#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class CoverageEligibilityResponse(domainresource.DomainResource):
    """ CoverageEligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    
    resource_type = "CoverageEligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.purpose = None
        """ auth-requirements | benefits | discovery | validation.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.patient = None
        """ Intended recipient of products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Estimated date or dates of service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Estimated date or dates of service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.created = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.requestor = None
        """ Party responsible for the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        """ Eligibility request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.insurer = None
        """ Coverage issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Patient insurance information.
        List of `CoverageEligibilityResponseInsurance` items (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ Preauthorization reference.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.form = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.error = None
        """ Processing errors.
        List of `CoverageEligibilityResponseError` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("purpose", "purpose", fhirdatatypes.FHIRCode, True, None, True, eligibilityresponsepurpose.EligibilityResponsePurpose), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("servicedDate", "servicedDate", fhirdatatypes.FHIRDate, False, "serviced", False, None), 
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False, None), 
            ("request", "request", fhirreference.FHIRReference, False, None, True, None), 
            ("outcome", "outcome", fhirdatatypes.FHIRCode, False, None, True, claimprocessingcodes.ClaimProcessingCodes), 
            ("disposition", "disposition", fhirdatatypes.FHIRString, False, None, False, None), 
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True, None), 
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False, None), 
            ("preAuthRef", "preAuthRef", fhirdatatypes.FHIRString, False, None, False, None), 
            ("form", "form", codeableconcept.CodeableConcept, False, None, False, None), 
            ("error", "error", CoverageEligibilityResponseError, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Errors encountered during the processing of the request.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
        ])
        return js




class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.inforce = None
        """ Coverage inforce indicator.
        Type `bool`. """
        
        self.benefitPeriod = None
        """ When the benefits are applicable.
        Type `Period` (represented as `dict` in JSON). """
        
        self.item = None
        """ Benefits and authorization details.
        List of `CoverageEligibilityResponseInsuranceItem` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True, None), 
            ("inforce", "inforce", bool, False, None, False, None), 
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False, None), 
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False, None), 
        ])
        return js




class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """ Benefits and authorization details.
    
    Benefits and optionally current balances, and authorization details by
    category or service.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.provider = None
        """ Performing practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """
        
        self.name = None
        """ Short name for the benefit.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Description of the benefit or services covered.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.benefit = None
        """ Benefit Summary.
        List of `CoverageEligibilityResponseInsuranceItemBenefit` items (represented as `dict` in JSON). """
        
        self.authorizationRequired = None
        """ Authorization required flag.
        Type `bool`. """
        
        self.authorizationSupporting = None
        """ Type of required supporting materials.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.authorizationUrl = None
        """ Preauthorization requirements endpoint.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        super(CoverageEligibilityResponseInsuranceItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False, None), 
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False, None), 
            ("provider", "provider", fhirreference.FHIRReference, False, None, False, None), 
            ("excluded", "excluded", bool, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("network", "network", codeableconcept.CodeableConcept, False, None, False, None), 
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False, None), 
            ("term", "term", codeableconcept.CodeableConcept, False, None, False, None), 
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False, None), 
            ("authorizationRequired", "authorizationRequired", bool, False, None, False, None), 
            ("authorizationSupporting", "authorizationSupporting", codeableconcept.CodeableConcept, True, None, False, None), 
            ("authorizationUrl", "authorizationUrl", fhirdatatypes.FHIRUri, False, None, False, None), 
        ])
        return js




class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits used to date.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.allowedUnsignedInt = None
        """ Benefits allowed.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.allowedString = None
        """ Benefits allowed.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.allowedMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.usedUnsignedInt = None
        """ Benefits used.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.usedString = None
        """ Benefits used.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.usedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsuranceItemBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("allowedUnsignedInt", "allowedUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "allowed", False, None), 
            ("allowedString", "allowedString", fhirdatatypes.FHIRString, False, "allowed", False, None), 
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False, None), 
            ("usedUnsignedInt", "usedUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "used", False, None), 
            ("usedString", "usedString", fhirdatatypes.FHIRString, False, "used", False, None), 
            ("usedMoney", "usedMoney", money.Money, False, "used", False, None), 
        ])
        return js



from fhirclient.codesystems import claimprocessingcodes

from fhirclient.models import codeableconcept

from fhirclient.codesystems import eligibilityresponsepurpose

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

from fhirclient.models import money

from fhirclient.models import period

