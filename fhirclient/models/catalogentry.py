#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CatalogEntry)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class CatalogEntry(domainresource.DomainResource):
    """ An entry in a catalog.
    
    Catalog entries are wrappers that contextualize items included in a
    catalog.
    """
    
    resource_type = "CatalogEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier of the catalog item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of item - medication, device, service, protocol or other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderable = None
        """ Whether the entry represents an orderable item.
        Type `bool`. """
        
        self.referencedItem = None
        """ The item that is being defined.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.additionalIdentifier = None
        """ Any additional identifier(s) for the catalog item, in the same
        granularity or concept.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.classification = None
        """ Classification (category or class) of the item entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.validityPeriod = None
        """ The time period in which this catalog entry is expected to be
        active.
        Type `Period` (represented as `dict` in JSON). """
        
        self.validTo = None
        """ The date until which this catalog entry is expected to be active.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.lastUpdated = None
        """ When was this catalog last updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.additionalCharacteristic = None
        """ Additional characteristics of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalClassification = None
        """ Additional classification of the catalog entry.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relatedEntry = None
        """ An item that this catalog entry is related to.
        List of `CatalogEntryRelatedEntry` items (represented as `dict` in JSON). """
        
        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("orderable", "orderable", bool, False, None, True, None), 
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True, None), 
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False, None), 
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, publicationstatus.PublicationStatus), 
            ("validityPeriod", "validityPeriod", period.Period, False, None, False, None), 
            ("validTo", "validTo", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("lastUpdated", "lastUpdated", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False, None), 
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False, None), 
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ An item that this catalog entry is related to.
    
    Used for example, to point to a substance, or to a device used to
    administer a medication.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relationtype = None
        """ triggers | is-replaced-by.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.item = None
        """ The reference to the related item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("relationtype", "relationtype", fhirdatatypes.FHIRCode, False, None, True, catalogentryrelationtype.CatalogEntryRelationType), 
            ("item", "item", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.codesystems import catalogentryrelationtype

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

