#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EvidenceVariable)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class EvidenceVariable(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "EvidenceVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this evidence variable, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the evidence variable.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the evidence variable.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this evidence variable (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this evidence variable (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the EvidenceVariable.
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
        """ Natural language description of the evidence variable.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for evidence variable (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the evidence variable was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the evidence variable was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the evidence variable is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ The category of the EvidenceVariable, such as Education, Treatment,
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
        
        self.type = None
        """ dichotomous | continuous | descriptive.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.characteristic = None
        """ What defines the members of the evidence element.
        List of `EvidenceVariableCharacteristic` items (represented as `dict` in JSON). """
        
        super(EvidenceVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("shortTitle", "shortTitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False, None), 
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
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False, evidencevariabletype.EvidenceVariableType), 
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the evidence element.
    
    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the characteristic.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.definitionReference = None
        """ What code or expression defines members?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.definitionDataRequirement = None
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.definitionTriggerDefinition = None
        """ What code or expression defines members?.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.usageContext = None
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        
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
        
        self.timeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.groupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(EvidenceVariableCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("definitionReference", "definitionReference", fhirreference.FHIRReference, False, "definition", True, None), 
            ("definitionCanonical", "definitionCanonical", fhirdatatypes.FHIRCanonical, False, "definition", True, None), 
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True, None), 
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True, None), 
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True, None), 
            ("definitionTriggerDefinition", "definitionTriggerDefinition", triggerdefinition.TriggerDefinition, False, "definition", True, None), 
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False, None), 
            ("exclude", "exclude", bool, False, None, False, None), 
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdatatypes.FHIRDateTime, False, "participantEffective", False, None), 
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False, None), 
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False, None), 
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False, None), 
            ("timeFromStart", "timeFromStart", duration.Duration, False, None, False, None), 
            ("groupMeasure", "groupMeasure", fhirdatatypes.FHIRCode, False, None, False, groupmeasure.GroupMeasure), 
        ])
        return js



from fhirclient.models import annotation

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

from fhirclient.models import timing

from fhirclient.models import triggerdefinition

from fhirclient.models import usagecontext

