#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicinalProductAuthorization(domainresource.DomainResource):
    """ The regulatory authorization of a medicinal product.
    """
    
    resource_type = "MedicinalProductAuthorization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier for the marketing authorization, as assigned by
        a regulator.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ The medicinal product that is being authorized.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.country = None
        """ The country in which the marketing authorization has been granted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Jurisdiction within a country.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ The status of the marketing authorization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusDate = None
        """ The date at which the given status has become applicable.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.restoreDate = None
        """ The date when a suspended the marketing or the marketing
        authorization of the product is anticipated to be restored.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.validityPeriod = None
        """ The beginning of the time period in which the marketing
        authorization is in the specific status shall be specified A
        complete date consisting of day, month and year shall be specified
        using the ISO 8601 date format.
        Type `Period` (represented as `dict` in JSON). """
        
        self.dataExclusivityPeriod = None
        """ A period of time after authorization before generic product
        applicatiosn can be submitted.
        Type `Period` (represented as `dict` in JSON). """
        
        self.dateOfFirstAuthorization = None
        """ The date when the first authorization was granted by a Medicines
        Regulatory Agency.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.internationalBirthDate = None
        """ Date of first marketing authorization for a company's new medicinal
        product in any country in the World.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.legalBasis = None
        """ The legal framework against which this authorization is granted.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.jurisdictionalAuthorization = None
        """ Authorization in areas within a country.
        List of `MedicinalProductAuthorizationJurisdictionalAuthorization` items (represented as `dict` in JSON). """
        
        self.holder = None
        """ Marketing Authorization Holder.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.regulator = None
        """ Medicines Regulatory Agency.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ The regulatory procedure for granting or amending a marketing
        authorization.
        Type `MedicinalProductAuthorizationProcedure` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("country", "country", codeableconcept.CodeableConcept, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("status", "status", codeableconcept.CodeableConcept, False, None, False, None), 
            ("statusDate", "statusDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("restoreDate", "restoreDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("validityPeriod", "validityPeriod", period.Period, False, None, False, None), 
            ("dataExclusivityPeriod", "dataExclusivityPeriod", period.Period, False, None, False, None), 
            ("dateOfFirstAuthorization", "dateOfFirstAuthorization", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("internationalBirthDate", "internationalBirthDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("legalBasis", "legalBasis", codeableconcept.CodeableConcept, False, None, False, None), 
            ("jurisdictionalAuthorization", "jurisdictionalAuthorization", MedicinalProductAuthorizationJurisdictionalAuthorization, True, None, False, None), 
            ("holder", "holder", fhirreference.FHIRReference, False, None, False, None), 
            ("regulator", "regulator", fhirreference.FHIRReference, False, None, False, None), 
            ("procedure", "procedure", MedicinalProductAuthorizationProcedure, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicinalProductAuthorizationJurisdictionalAuthorization(backboneelement.BackboneElement):
    """ Authorization in areas within a country.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ The assigned number for the marketing authorization.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.country = None
        """ Country of authorization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Jurisdiction within a country.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply in a jurisdiction or region.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ The start and expected end date of the authorization.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationJurisdictionalAuthorization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("country", "country", codeableconcept.CodeableConcept, False, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False, None), 
            ("validityPeriod", "validityPeriod", period.Period, False, None, False, None), 
        ])
        return js




class MedicinalProductAuthorizationProcedure(backboneelement.BackboneElement):
    """ The regulatory procedure for granting or amending a marketing authorization.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifier for this procedure.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.datePeriod = None
        """ Date of procedure.
        Type `Period` (represented as `dict` in JSON). """
        
        self.dateDateTime = None
        """ Date of procedure.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.application = None
        """ Applcations submitted to obtain a marketing authorization.
        List of `MedicinalProductAuthorizationProcedure` items (represented as `dict` in JSON). """
        
        super(MedicinalProductAuthorizationProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductAuthorizationProcedure, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("datePeriod", "datePeriod", period.Period, False, "date", False, None), 
            ("dateDateTime", "dateDateTime", fhirdatatypes.FHIRDateTime, False, "date", False, None), 
            ("application", "application", MedicinalProductAuthorizationProcedure, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

