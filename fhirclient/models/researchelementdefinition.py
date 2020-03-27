#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ResearchElementDefinition(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The ResearchElementDefinition resource describes a "PICO" element that
    knowledge (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "ResearchElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this research element definition,
        represented as a URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the research element definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the research element definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this research element definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this research element definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the ResearchElementDefinition.
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
        """ Natural language description of the research element definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.comment = None
        """ Used for footnotes or explanatory notes.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for research element definition (if
        applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this research element definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.usage = None
        """ Describes the clinical usage of the ResearchElementDefinition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the research element definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the research element definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the research element definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ The category of the ResearchElementDefinition, such as Education,
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
        
        self.library = None
        """ Logic used by the ResearchElementDefinition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.type = None
        """ population | exposure | outcome.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.variableType = None
        """ dichotomous | continuous | descriptive.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.characteristic = None
        """ What defines the members of the research element.
        List of `ResearchElementDefinitionCharacteristic` items (represented as `dict` in JSON). """
        
        super(ResearchElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchElementDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("shortTitle", "shortTitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False, None), 
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, True, None, False, None), 
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
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, researchelementtype.ResearchElementType), 
            ("variableType", "variableType", fhirdatatypes.FHIRCode, False, None, False, evidencevariabletype.EvidenceVariableType), 
            ("characteristic", "characteristic", ResearchElementDefinitionCharacteristic, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ResearchElementDefinitionCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the research element.
    
    A characteristic that defines the members of the research element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.definitionDataRequirement = None
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.usageContext = None
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        
        self.unitOfMeasure = None
        """ What unit is the outcome described in?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.studyEffectiveDescription = None
        """ What time period does the study cover.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.studyEffectiveDateTime = None
        """ What time period does the study cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.studyEffectivePeriod = None
        """ What time period does the study cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.studyEffectiveDuration = None
        """ What time period does the study cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.studyEffectiveTiming = None
        """ What time period does the study cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.studyEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.studyEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.participantEffectiveDescription = None
        """ What time period do participants cover.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.participantEffectiveDateTime = None
        """ What time period do participants cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.participantEffectivePeriod = None
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.participantEffectiveDuration = None
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveTiming = None
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.participantEffectiveTimeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveGroupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(ResearchElementDefinitionCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchElementDefinitionCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True, None), 
            ("definitionCanonical", "definitionCanonical", fhirdatatypes.FHIRCanonical, False, "definition", True, None), 
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True, None), 
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True, None), 
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False, None), 
            ("exclude", "exclude", bool, False, None, False, None), 
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False, None), 
            ("studyEffectiveDescription", "studyEffectiveDescription", fhirdatatypes.FHIRString, False, None, False, None), 
            ("studyEffectiveDateTime", "studyEffectiveDateTime", fhirdatatypes.FHIRDateTime, False, "studyEffective", False, None), 
            ("studyEffectivePeriod", "studyEffectivePeriod", period.Period, False, "studyEffective", False, None), 
            ("studyEffectiveDuration", "studyEffectiveDuration", duration.Duration, False, "studyEffective", False, None), 
            ("studyEffectiveTiming", "studyEffectiveTiming", timing.Timing, False, "studyEffective", False, None), 
            ("studyEffectiveTimeFromStart", "studyEffectiveTimeFromStart", duration.Duration, False, None, False, None), 
            ("studyEffectiveGroupMeasure", "studyEffectiveGroupMeasure", fhirdatatypes.FHIRCode, False, None, False, groupmeasure.GroupMeasure), 
            ("participantEffectiveDescription", "participantEffectiveDescription", fhirdatatypes.FHIRString, False, None, False, None), 
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdatatypes.FHIRDateTime, False, "participantEffective", False, None), 
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False, None), 
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False, None), 
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False, None), 
            ("participantEffectiveTimeFromStart", "participantEffectiveTimeFromStart", duration.Duration, False, None, False, None), 
            ("participantEffectiveGroupMeasure", "participantEffectiveGroupMeasure", fhirdatatypes.FHIRCode, False, None, False, groupmeasure.GroupMeasure), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import datarequirement

from fhirclient.models import duration

from fhirclient.codesystems import evidencevariabletype

from fhirclient.models import expression

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import groupmeasure

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import relatedartifact

from fhirclient.codesystems import researchelementtype

from fhirclient.models import timing

from fhirclient.models import usagecontext

