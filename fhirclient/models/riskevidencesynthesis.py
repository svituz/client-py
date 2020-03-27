#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ A quantified estimate of risk based on a body of evidence.
    
    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """
    
    resource_type = "RiskEvidenceSynthesis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this risk evidence synthesis, represented
        as a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the risk evidence synthesis.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the risk evidence synthesis.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this risk evidence synthesis (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this risk evidence synthesis (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the risk evidence synthesis.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for risk evidence synthesis (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the risk evidence synthesis was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the risk evidence synthesis was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the risk evidence synthesis is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ The category of the EffectEvidenceSynthesis, such as Education,
        Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.synthesisType = None
        """ Type of synthesis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.studyType = None
        """ Type of study.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.population = None
        """ What population?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exposure = None
        """ What exposure?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ What outcome?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sampleSize = None
        """ What sample size was involved?.
        Type `RiskEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """
        
        self.riskEstimate = None
        """ What was the estimated risk.
        Type `RiskEvidenceSynthesisRiskEstimate` (represented as `dict` in JSON). """
        
        self.certainty = None
        """ How certain is the risk.
        List of `RiskEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("approvalDate", "approvalDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("lastReviewDate", "lastReviewDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False, None), 
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False, None), 
            ("author", "author", contactdetail.ContactDetail, True, None, False, None), 
            ("editor", "editor", contactdetail.ContactDetail, True, None, False, None), 
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False, None), 
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False, None), 
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False, None), 
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("population", "population", fhirreference.FHIRReference, False, None, True, None), 
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, False, None), 
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True, None), 
            ("sampleSize", "sampleSize", RiskEvidenceSynthesisSampleSize, False, None, False, None), 
            ("riskEstimate", "riskEstimate", RiskEvidenceSynthesisRiskEstimate, False, None, False, None), 
            ("certainty", "certainty", RiskEvidenceSynthesisCertainty, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ How certain is the risk.
    
    A description of the certainty of the risk estimate.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.rating = None
        """ Certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.certaintySubcomponent = None
        """ A component that contributes to the overall certainty.
        List of `RiskEvidenceSynthesisCertaintyCertaintySubcomponent` items (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisCertainty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("certaintySubcomponent", "certaintySubcomponent", RiskEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False, None), 
        ])
        return js




class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(backboneelement.BackboneElement):
    """ A component that contributes to the overall certainty.
    
    A description of a component of the overall certainty.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type of subcomponent of certainty rating.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rating = None
        """ Subcomponent certainty rating.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js




class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ What was the estimated risk.
    
    The estimated risk of the outcome.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of risk estimate.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ Type of risk estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Point estimate.
        Type `float`. """
        
        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.denominatorCount = None
        """ Sample size for group measured.
        Type `int`. """
        
        self.numeratorCount = None
        """ Number with the outcome.
        Type `int`. """
        
        self.precisionEstimate = None
        """ How precise the estimate is.
        List of `RiskEvidenceSynthesisRiskEstimatePrecisionEstimate` items (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisRiskEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("value", "value", float, False, None, False, None), 
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False, None), 
            ("denominatorCount", "denominatorCount", int, False, None, False, None), 
            ("numeratorCount", "numeratorCount", int, False, None, False, None), 
            ("precisionEstimate", "precisionEstimate", RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, True, None, False, None), 
        ])
        return js




class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(backboneelement.BackboneElement):
    """ How precise the estimate is.
    
    A description of the precision of the estimate for the effect.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Type of precision estimate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.level = None
        """ Level of confidence interval.
        Type `float`. """
        
        self.from_fhir = None
        """ Lower bound.
        Type `float`. """
        
        self.to = None
        """ Upper bound.
        Type `float`. """
        
        super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("level", "level", float, False, None, False, None), 
            ("from_fhir", "from", float, False, None, False, None), 
            ("to", "to", float, False, None, False, None), 
        ])
        return js




class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ What sample size was involved?.
    
    A description of the size of the sample involved in the synthesis.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of sample size.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.numberOfStudies = None
        """ How many studies?.
        Type `int`. """
        
        self.numberOfParticipants = None
        """ How many participants?.
        Type `int`. """
        
        super(RiskEvidenceSynthesisSampleSize, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("numberOfStudies", "numberOfStudies", int, False, None, False, None), 
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import relatedartifact

from fhirclient.models import usagecontext

