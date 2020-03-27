#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Measure)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Measure(domainresource.DomainResource):
    """ A quality measure definition.
    
    The Measure resource provides the definition of a quality measure.
    """
    
    resource_type = "Measure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this measure, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the measure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the measure.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this measure (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this measure (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the measure.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.subjectCodeableConcept = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ E.g. Patient, Practitioner, RelatedPerson, Organization, Location,
        Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        """ Natural language description of the measure.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for measure (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this measure is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.usage = None
        """ Describes the clinical usage of the measure.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the measure was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the measure was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the measure is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ The category of the measure, such as Education, Treatment,
        Assessment, etc..
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
        
        self.library = None
        """ Logic used by the measure.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.disclaimer = None
        """ Disclaimer for use of the measure or its referenced content.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.scoring = None
        """ proportion | ratio | continuous-variable | cohort.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.compositeScoring = None
        """ opportunity | all-or-nothing | linear | weighted.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ process | outcome | structure | patient-reported-outcome |
        composite.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.riskAdjustment = None
        """ How risk adjustment is applied for this measure.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.rateAggregation = None
        """ How is rate aggregation performed for this measure.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.rationale = None
        """ Detailed description of why the measure exists.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.clinicalRecommendationStatement = None
        """ Summary of clinical guidelines.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.improvementNotation = None
        """ increase | decrease.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Defined terms used in the measure documentation.
        List of `FHIRMarkdown` items (represented as `str` in JSON). """
        
        self.guidance = None
        """ Additional guidance for implementers.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.group = None
        """ Population criteria group.
        List of `MeasureGroup` items (represented as `dict` in JSON). """
        
        self.supplementalData = None
        """ What other data should be reported with the measure.
        List of `MeasureSupplementalData` items (represented as `dict` in JSON). """
        
        super(Measure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False, None), 
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("usage", "usage", fhirdatatypes.FHIRString, False, None, False, None), 
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
            ("library", "library", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("disclaimer", "disclaimer", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False, None), 
            ("compositeScoring", "compositeScoring", codeableconcept.CodeableConcept, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("riskAdjustment", "riskAdjustment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("rateAggregation", "rateAggregation", fhirdatatypes.FHIRString, False, None, False, None), 
            ("rationale", "rationale", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False, None), 
            ("definition", "definition", fhirdatatypes.FHIRMarkdown, True, None, False, None), 
            ("guidance", "guidance", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("group", "group", MeasureGroup, True, None, False, None), 
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MeasureGroup(backboneelement.BackboneElement):
    """ Population criteria group.
    
    A group of population criteria for the measure.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Summary description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.population = None
        """ Population criteria.
        List of `MeasureGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ Stratifier criteria for the measure.
        List of `MeasureGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("population", "population", MeasureGroupPopulation, True, None, False, None), 
            ("stratifier", "stratifier", MeasureGroupStratifier, True, None, False, None), 
        ])
        return js




class MeasureGroupPopulation(backboneelement.BackboneElement):
    """ Population criteria.
    
    A population criteria for the measure.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ initial-population | numerator | numerator-exclusion | denominator
        | denominator-exclusion | denominator-exception | measure-
        population | measure-population-exclusion | measure-observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ The human readable description of this population criteria.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.criteria = None
        """ The criteria that defines this population.
        Type `Expression` (represented as `dict` in JSON). """
        
        super(MeasureGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("criteria", "criteria", expression.Expression, False, None, True, None), 
        ])
        return js




class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ Stratifier criteria for the measure.
    
    The stratifier criteria for the measure report, specified as either the
    name of a valid CQL expression defined within a referenced library or a
    valid FHIR Resource Path.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the stratifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ The human readable description of this stratifier.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.criteria = None
        """ How the measure should be stratified.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.component = None
        """ Stratifier criteria component for the measure.
        List of `MeasureGroupStratifierComponent` items (represented as `dict` in JSON). """
        
        super(MeasureGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("criteria", "criteria", expression.Expression, False, None, False, None), 
            ("component", "component", MeasureGroupStratifierComponent, True, None, False, None), 
        ])
        return js




class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    """ Stratifier criteria component for the measure.
    
    A component of the stratifier criteria for the measure report, specified as
    either the name of a valid CQL expression defined within a referenced
    library or a valid FHIR Resource Path.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the stratifier component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ The human readable description of this stratifier component.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.criteria = None
        """ Component of how the measure should be stratified.
        Type `Expression` (represented as `dict` in JSON). """
        
        super(MeasureGroupStratifierComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifierComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("criteria", "criteria", expression.Expression, False, None, True, None), 
        ])
        return js




class MeasureSupplementalData(backboneelement.BackboneElement):
    """ What other data should be reported with the measure.
    
    The supplemental data criteria for the measure report, specified as either
    the name of a valid CQL expression within a referenced library, or a valid
    FHIR Resource Path.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Meaning of the supplemental data.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usage = None
        """ supplemental-data | risk-adjustment-factor.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ The human readable description of this supplemental data.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.criteria = None
        """ Expression describing additional data to be reported.
        Type `Expression` (represented as `dict` in JSON). """
        
        super(MeasureSupplementalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("usage", "usage", codeableconcept.CodeableConcept, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("criteria", "criteria", expression.Expression, False, None, True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import expression

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import relatedartifact

from fhirclient.models import usagecontext

