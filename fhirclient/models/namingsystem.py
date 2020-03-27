#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/NamingSystem)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.
    
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    
    resource_type = "NamingSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name for this naming system (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.kind = None
        """ codesystem | identifier | root.
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
        
        self.responsible = None
        """ Who maintains system namespace?.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the naming system.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for naming system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.usage = None
        """ How/where is it used.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.uniqueId = None
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
        
        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, True, namingsystemtype.NamingSystemType), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, True, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("responsible", "responsible", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("usage", "usage", fhirdatatypes.FHIRString, False, None, False, None), 
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.
    
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ oid | uuid | uri | other.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.value = None
        """ The unique identifier.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.preferred = None
        """ Is this the id that should be used for this type.
        Type `bool`. """
        
        self.comment = None
        """ Notes about identifier usage.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.period = None
        """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """
        
        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, namingsystemidentifiertype.NamingSystemIdentifierType), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, True, None), 
            ("preferred", "preferred", bool, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import namingsystemidentifiertype

from fhirclient.codesystems import namingsystemtype

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import usagecontext

