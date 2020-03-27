#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RiskAssessment)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.
    
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    
    resource_type = "RiskAssessment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier for the assessment.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Part of this occurrence.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.method = None
        """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Type of assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who/what does assessment apply to?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Where was assessment performed?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When was assessment made?.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When was assessment made?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.condition = None
        """ Condition assessed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who did assessment?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why the assessment was necessary?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why the assessment was necessary?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.basis = None
        """ Information used in assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.prediction = None
        """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """
        
        self.mitigation = None
        """ How to reduce risk.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.note = None
        """ Comments on the risk assessment.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, False, None, False, None), 
            ("parent", "parent", fhirreference.FHIRReference, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, observationstatus.ObservationStatus), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", False, None), 
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False, None), 
            ("condition", "condition", fhirreference.FHIRReference, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("basis", "basis", fhirreference.FHIRReference, True, None, False, None), 
            ("prediction", "prediction", RiskAssessmentPrediction, True, None, False, None), 
            ("mitigation", "mitigation", fhirdatatypes.FHIRString, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.
    
    Describes the expected outcome for the subject.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcome = None
        """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityDecimal = None
        """ Likelihood of specified outcome.
        Type `float`. """
        
        self.probabilityRange = None
        """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """
        
        self.qualitativeRisk = None
        """ Likelihood of specified outcome as a qualitative value.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.relativeRisk = None
        """ Relative likelihood.
        Type `float`. """
        
        self.whenPeriod = None
        """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """
        
        self.whenRange = None
        """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rationale = None
        """ Explanation of prediction.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False, None), 
            ("probabilityDecimal", "probabilityDecimal", float, False, "probability", False, None), 
            ("probabilityRange", "probabilityRange", range.Range, False, "probability", False, None), 
            ("qualitativeRisk", "qualitativeRisk", codeableconcept.CodeableConcept, False, None, False, None), 
            ("relativeRisk", "relativeRisk", float, False, None, False, None), 
            ("whenPeriod", "whenPeriod", period.Period, False, "when", False, None), 
            ("whenRange", "whenRange", range.Range, False, "when", False, None), 
            ("rationale", "rationale", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import observationstatus

from fhirclient.models import period

from fhirclient.models import range

