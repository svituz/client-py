#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DocumentManifest)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DocumentManifest(domainresource.DomainResource):
    """ A list that defines a set of documents.
    
    A collection of documents compiled for a purpose together with metadata
    that applies to the collection.
    """
    
    resource_type = "DocumentManifest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.masterIdentifier = None
        """ Unique Identifier for the set of documents.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Other identifiers for the manifest.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ current | superseded | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ Kind of document set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ The subject of the set of documents.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.created = None
        """ When this document manifest created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.author = None
        """ Who and/or what authored the DocumentManifest.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Intended to get notified about this set of documents.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.source = None
        """ The source system/application/software.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.description = None
        """ Human-readable description (title).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.content = None
        """ Items in manifest.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.related = None
        """ Related things.
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """
        
        super(DocumentManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, documentreferencestatus.DocumentReferenceStatus), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, True, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False, None), 
            ("source", "source", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("content", "content", fhirreference.FHIRReference, True, None, True, None), 
            ("related", "related", DocumentManifestRelated, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DocumentManifestRelated(backboneelement.BackboneElement):
    """ Related things.
    
    Related identifiers or resources associated with the DocumentManifest.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifiers of things that are related.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.ref = None
        """ Related Resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DocumentManifestRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("ref", "ref", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import documentreferencestatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

