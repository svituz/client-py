#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time set of recommendations (i.e. forecasting)
    according to a published schedule with optional supporting justification.
    """
    
    resource_type = "ImmunizationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who this profile is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date recommendation(s) created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recommendation = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("authority", "authority", fhirreference.FHIRReference, False, None, False, None), 
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.vaccineCode = None
        """ Vaccine  or vaccine group recommendation applies to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.targetDisease = None
        """ Disease to be immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contraindicatedVaccineCode = None
        """ Vaccine which is contraindicated to fulfill the recommendation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.forecastStatus = None
        """ Vaccine recommendation status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.forecastReason = None
        """ Vaccine administration status reason.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateCriterion = None
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Protocol details.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.series = None
        """ Name of vaccination series.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.doseNumberPositiveInt = None
        """ Recommended dose number within series.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.doseNumberString = None
        """ Recommended dose number within series.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.supportingImmunization = None
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingPatientInformation = None
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, False, None), 
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True, None), 
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("series", "series", fhirdatatypes.FHIRString, False, None, False, None), 
            ("doseNumberPositiveInt", "doseNumberPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "doseNumber", False, None), 
            ("doseNumberString", "doseNumberString", fhirdatatypes.FHIRString, False, "doseNumber", False, None), 
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "seriesDoses", False, None), 
            ("seriesDosesString", "seriesDosesString", fhirdatatypes.FHIRString, False, "seriesDoses", False, None), 
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False, None), 
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Recommended date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("value", "value", fhirdatatypes.FHIRDateTime, False, None, True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

