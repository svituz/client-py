#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Account)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.
    
    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """
    
    resource_type = "Account"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error | on-hold | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.name = None
        """ Human-readable label.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subject = None
        """ The entity that caused the expenses.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.servicePeriod = None
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
        List of `AccountCoverage` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ Entity managing the Account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description = None
        """ Explanation of purpose/use.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.guarantor = None
        """ The parties ultimately responsible for balancing the Account.
        List of `AccountGuarantor` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Reference to a parent Account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Account, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, accountstatus.AccountStatus), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, True, None, False, None), 
            ("servicePeriod", "servicePeriod", period.Period, False, None, False, None), 
            ("coverage", "coverage", AccountCoverage, True, None, False, None), 
            ("owner", "owner", fhirreference.FHIRReference, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("guarantor", "guarantor", AccountGuarantor, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ The party(s), such as insurances, that may contribute to the
        payment of this account.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ The priority of the coverage in the context of this account.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True, None), 
            ("priority", "priority", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
        ])
        return js




class AccountGuarantor(backboneelement.BackboneElement):
    """ The parties ultimately responsible for balancing the Account.
    
    The parties responsible for balancing the account if other payment options
    fall short.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        """ Responsible entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onHold = None
        """ Credit or other hold applied.
        Type `bool`. """
        
        self.period = None
        """ Guarantee account during.
        Type `Period` (represented as `dict` in JSON). """
        
        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True, None), 
            ("onHold", "onHold", bool, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import accountstatus

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

