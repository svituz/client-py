#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/List)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class List(domainresource.DomainResource):
    """ A list is a curated collection of resources.
    """
    
    resource_type = "List"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ current | retired | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.mode = None
        """ working | snapshot | changes.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.title = None
        """ Descriptive name for the list.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.code = None
        """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ If all resources have the same subject.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Context in which list created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the list was prepared.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.source = None
        """ Who and/or what defined the list contents (aka Author).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.orderedBy = None
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the list.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.entry = None
        """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """
        
        self.emptyReason = None
        """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(List, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, liststatus.ListStatus), 
            ("mode", "mode", fhirdatatypes.FHIRCode, False, None, True, listmode.ListMode), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, False, None, False, None), 
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("entry", "entry", ListEntry, True, None, False, None), 
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ Entries in the list.
    
    Entries in this list.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.flag = None
        """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.deleted = None
        """ If this item is actually marked as deleted.
        Type `bool`. """
        
        self.date = None
        """ When item added to list.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.item = None
        """ Actual entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False, None), 
            ("deleted", "deleted", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("item", "item", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import listmode

from fhirclient.codesystems import liststatus

