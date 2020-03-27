#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Library)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Library(domainresource.DomainResource):
    """ Represents a library of quality improvement components.
    
    The Library resource is a general-purpose container for knowledge asset
    definitions. It can be used to describe and expose existing knowledge
    assets such as logic libraries and information model descriptions, as well
    as to describe a collection of knowledge assets.
    """
    
    resource_type = "Library"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this library, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the library.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the library.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this library (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this library (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the library.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.type = None
        """ logic-library | model-definition | asset-collection | module-
        definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectCodeableConcept = None
        """ Type of individual the library content is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ Type of individual the library content is focused on.
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
        """ Natural language description of the library.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for library (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this library is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.usage = None
        """ Describes the clinical usage of the library.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the library was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the library was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the library is expected to be used.
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
        
        self.parameter = None
        """ Parameters defined by the library.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
        self.dataRequirement = None
        """ What data is referenced by this library.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.content = None
        """ Contents of the library, either embedded or referenced.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        super(Library, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Library, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
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
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False, None), 
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False, None), 
            ("content", "content", attachment.Attachment, True, None, False, None), 
        ])
        return js



from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import datarequirement

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import parameterdefinition

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import relatedartifact

from fhirclient.models import usagecontext

