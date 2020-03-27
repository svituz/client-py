#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EventDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class EventDefinition(domainresource.DomainResource):
    """ A description of when an event can occur.
    
    The EventDefinition resource provides a reusable description of when a
    particular event can occur.
    """
    
    resource_type = "EventDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this event definition, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the event definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the event definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this event definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this event definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the event definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.subjectCodeableConcept = None
        """ Type of individual the event definition is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ Type of individual the event definition is focused on.
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
        """ Natural language description of the event definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for event definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this event definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.usage = None
        """ Describes the clinical usage of the event definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the event definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the event definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the event definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ E.g. Education, Treatment, Assessment, etc..
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
        
        self.trigger = None
        """ "when" the event occurs (multiple = 'or').
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        super(EventDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EventDefinition, self).elementProperties()
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
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import relatedartifact

from fhirclient.models import triggerdefinition

from fhirclient.models import usagecontext

