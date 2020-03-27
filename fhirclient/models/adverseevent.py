#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AdverseEvent)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class AdverseEvent(domainresource.DomainResource):
    """ Medical care, research study or other healthcare event causing physical
    injury.
    
    Actual or  potential/avoided event causing unintended physical injury
    resulting from or contributed to by medical care, a research study or other
    healthcare setting factors that requires additional monitoring, treatment,
    or hospitalization, or that results in death.
    """
    
    resource_type = "AdverseEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier for the event.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.actuality = None
        """ actual | potential.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ product-problem | product-quality | product-use-error | wrong-dose
        | incorrect-prescribing-information | wrong-technique | wrong-
        route-of-administration | wrong-rate | wrong-duration | wrong-time
        | expired-drug | medical-device-use-error | problem-different-
        manufacturer | unsafe-physical-environment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.event = None
        """ Type of the event itself in relation to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Subject impacted by event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the event occurred.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.detected = None
        """ When the event was detected.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recordedDate = None
        """ When the event was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.resultingCondition = None
        """ Effect on the subject due to this event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Location where adverse event occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.seriousness = None
        """ Seriousness of the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.severity = None
        """ mild | moderate | severe.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ resolved | recovering | ongoing | resolvedWithSequelae | fatal |
        unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recorder = None
        """ Who recorded the adverse event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contributor = None
        """ Who  was involved in the adverse event or the potential adverse
        event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.suspectEntity = None
        """ The suspected agent causing the adverse event.
        List of `AdverseEventSuspectEntity` items (represented as `dict` in JSON). """
        
        self.subjectMedicalHistory = None
        """ AdverseEvent.subjectMedicalHistory.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.referenceDocument = None
        """ AdverseEvent.referenceDocument.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.study = None
        """ AdverseEvent.study.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(AdverseEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("actuality", "actuality", fhirdatatypes.FHIRCode, False, None, True, adverseeventactuality.AdverseEventActuality), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("event", "event", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("detected", "detected", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("recordedDate", "recordedDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("resultingCondition", "resultingCondition", fhirreference.FHIRReference, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("seriousness", "seriousness", codeableconcept.CodeableConcept, False, None, False, None), 
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False, None), 
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False, None), 
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False, None), 
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False, None), 
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False, None), 
            ("subjectMedicalHistory", "subjectMedicalHistory", fhirreference.FHIRReference, True, None, False, None), 
            ("referenceDocument", "referenceDocument", fhirreference.FHIRReference, True, None, False, None), 
            ("study", "study", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ The suspected agent causing the adverse event.
    
    Describes the entity that is suspected to have caused the adverse event.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instance = None
        """ Refers to the specific entity that caused the adverse event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.causality = None
        """ Information on the possible cause of the event.
        List of `AdverseEventSuspectEntityCausality` items (represented as `dict` in JSON). """
        
        super(AdverseEventSuspectEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("instance", "instance", fhirreference.FHIRReference, False, None, True, None), 
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False, None), 
        ])
        return js




class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
    """ Information on the possible cause of the event.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment = None
        """ Assessment of if the entity caused the event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productRelatedness = None
        """ AdverseEvent.suspectEntity.causalityProductRelatedness.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.author = None
        """ AdverseEvent.suspectEntity.causalityAuthor.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.method = None
        """ ProbabilityScale | Bayesian | Checklist.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AdverseEventSuspectEntityCausality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", codeableconcept.CodeableConcept, False, None, False, None), 
            ("productRelatedness", "productRelatedness", fhirdatatypes.FHIRString, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import adverseeventactuality

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

