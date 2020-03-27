#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ObservationDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.
    
    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """
    
    resource_type = "ObservationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Category of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier for this ObservationDefinition instance.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.permittedDataType = None
        """ Quantity | CodeableConcept | string | boolean | integer | Range |
        Ratio | SampledData | time | dateTime | Period.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.multipleResultsAllowed = None
        """ Multiple results allowed.
        Type `bool`. """
        
        self.method = None
        """ Method used to produce the observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.preferredReportName = None
        """ Preferred report name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.quantitativeDetails = None
        """ Characteristics of quantitative results.
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """
        
        self.qualifiedInterval = None
        """ Qualified range for continuous and ordinal observation results.
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """
        
        self.validCodedValueSet = None
        """ Value set of valid coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.normalCodedValueSet = None
        """ Value set of normal coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.abnormalCodedValueSet = None
        """ Value set of abnormal coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.criticalCodedValueSet = None
        """ Value set of critical coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("permittedDataType", "permittedDataType", fhirdatatypes.FHIRCode, True, None, False, observationdatatype.ObservationDataType), 
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False, None), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
            ("preferredReportName", "preferredReportName", fhirdatatypes.FHIRString, False, None, False, None), 
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False, None), 
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False, None), 
            ("validCodedValueSet", "validCodedValueSet", fhirreference.FHIRReference, False, None, False, None), 
            ("normalCodedValueSet", "normalCodedValueSet", fhirreference.FHIRReference, False, None, False, None), 
            ("abnormalCodedValueSet", "abnormalCodedValueSet", fhirreference.FHIRReference, False, None, False, None), 
            ("criticalCodedValueSet", "criticalCodedValueSet", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.
    
    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ reference | critical | absolute.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.range = None
        """ The interval itself, for continuous or ordinal observations.
        Type `Range` (represented as `dict` in JSON). """
        
        self.context = None
        """ Range context qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.appliesTo = None
        """ Targetted population of the range.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.age = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.gestationalAge = None
        """ Applicable gestational age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """
        
        self.condition = None
        """ Condition associated with the reference range.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ObservationDefinitionQualifiedInterval, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("category", "category", fhirdatatypes.FHIRCode, False, None, False, observationrangecategory.ObservationRangeCategory), 
            ("range", "range", range.Range, False, None, False, None), 
            ("context", "context", codeableconcept.CodeableConcept, False, None, False, None), 
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False, None), 
            ("gender", "gender", fhirdatatypes.FHIRCode, False, None, False, administrativegender.AdministrativeGender), 
            ("age", "age", range.Range, False, None, False, None), 
            ("gestationalAge", "gestationalAge", range.Range, False, None, False, None), 
            ("condition", "condition", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.
    
    Characteristics for quantitative results of this observation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.customaryUnit = None
        """ Customary unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ SI unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.conversionFactor = None
        """ SI to Customary unit conversion factor.
        Type `float`. """
        
        self.decimalPrecision = None
        """ Decimal precision of observation quantitative results.
        Type `int`. """
        
        super(ObservationDefinitionQuantitativeDetails, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("customaryUnit", "customaryUnit", codeableconcept.CodeableConcept, False, None, False, None), 
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False, None), 
            ("conversionFactor", "conversionFactor", float, False, None, False, None), 
            ("decimalPrecision", "decimalPrecision", int, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import administrativegender

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import observationdatatype

from fhirclient.codesystems import observationrangecategory

from fhirclient.models import range

