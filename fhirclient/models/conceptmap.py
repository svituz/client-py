#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ConceptMap)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ConceptMap(domainresource.DomainResource):
    """ A map from one set of concepts to one or more other concepts.
    
    A statement of relationships from one set of concepts to one or more other
    concepts - either concepts in code systems, or data element/data element
    concepts, or classes in class models.
    """
    
    resource_type = "ConceptMap"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this concept map, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the concept map.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the concept map.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this concept map (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this concept map (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
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
        """ Natural language description of the concept map.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for concept map (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this concept map is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.sourceUri = None
        """ The source value set that contains the concepts that are being
        mapped.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.sourceCanonical = None
        """ The source value set that contains the concepts that are being
        mapped.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.targetUri = None
        """ The target value set which provides context for the mappings.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.targetCanonical = None
        """ The target value set which provides context for the mappings.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.group = None
        """ Same source and target systems.
        List of `ConceptMapGroup` items (represented as `dict` in JSON). """
        
        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("sourceUri", "sourceUri", fhirdatatypes.FHIRUri, False, "source", False, None), 
            ("sourceCanonical", "sourceCanonical", fhirdatatypes.FHIRCanonical, False, "source", False, None), 
            ("targetUri", "targetUri", fhirdatatypes.FHIRUri, False, "target", False, None), 
            ("targetCanonical", "targetCanonical", fhirdatatypes.FHIRCanonical, False, "target", False, None), 
            ("group", "group", ConceptMapGroup, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ConceptMapGroup(backboneelement.BackboneElement):
    """ Same source and target systems.
    
    A group of mappings that all have the same source and target system.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ Source system where concepts to be mapped are defined.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.sourceVersion = None
        """ Specific version of the  code system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.target = None
        """ Target system that the concepts are to be mapped to.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.targetVersion = None
        """ Specific version of the  code system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.element = None
        """ Mappings for a concept from the source set.
        List of `ConceptMapGroupElement` items (represented as `dict` in JSON). """
        
        self.unmapped = None
        """ What to do when there is no mapping for the source concept.
        Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON). """
        
        super(ConceptMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("source", "source", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("sourceVersion", "sourceVersion", fhirdatatypes.FHIRString, False, None, False, None), 
            ("target", "target", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("targetVersion", "targetVersion", fhirdatatypes.FHIRString, False, None, False, None), 
            ("element", "element", ConceptMapGroupElement, True, None, True, None), 
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False, None), 
        ])
        return js




class ConceptMapGroupElement(backboneelement.BackboneElement):
    """ Mappings for a concept from the source set.
    
    Mappings for an individual concept in the source to one or more concepts in
    the target.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Identifies element being mapped.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.display = None
        """ Display for the code.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.target = None
        """ Concept in target system for element.
        List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("display", "display", fhirdatatypes.FHIRString, False, None, False, None), 
            ("target", "target", ConceptMapGroupElementTarget, True, None, False, None), 
        ])
        return js




class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """ Concept in target system for element.
    
    A concept from the target value set that this concept maps to.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Code that identifies the target element.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.display = None
        """ Display for the code.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.equivalence = None
        """ relatedto | equivalent | equal | wider | subsumes | narrower |
        specializes | inexact | unmatched | disjoint.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.comment = None
        """ Description of status/issues in mapping.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.dependsOn = None
        """ Other elements required for this mapping (from context).
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        self.product = None
        """ Other concepts that this mapping also produces.
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElementTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("display", "display", fhirdatatypes.FHIRString, False, None, False, None), 
            ("equivalence", "equivalence", fhirdatatypes.FHIRCode, False, None, True, conceptmapequivalence.ConceptMapEquivalence), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False, None), 
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False, None), 
        ])
        return js




class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """ Other elements required for this mapping (from context).
    
    A set of additional dependencies for this mapping to hold. This mapping is
    only applicable if the specified element can be resolved, and it has the
    specified value.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.property = None
        """ Reference to property mapping depends on.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.system = None
        """ Code System (if necessary).
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.value = None
        """ Value of the referenced element.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.display = None
        """ Display for the code (if value is a code).
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ConceptMapGroupElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("property", "property", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("system", "system", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, True, None), 
            ("display", "display", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ What to do when there is no mapping for the source concept.
    
    What to do when there is no mapping for the source concept. "Unmapped" does
    not include codes that are unmatched, and the unmapped element is ignored
    in a code is specified to have equivalence = unmatched.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ provided | fixed | other-map.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Fixed code when mode = fixed.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.display = None
        """ Display for the code.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.url = None
        """ canonical reference to an additional ConceptMap to use for mapping
        if the source concept is unmapped.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(ConceptMapGroupUnmapped, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("mode", "mode", fhirdatatypes.FHIRCode, False, None, True, conceptmapgroupunmappedmode.ConceptMapGroupUnmappedMode), 
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("display", "display", fhirdatatypes.FHIRString, False, None, False, None), 
            ("url", "url", fhirdatatypes.FHIRCanonical, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import conceptmapequivalence

from fhirclient.codesystems import conceptmapgroupunmappedmode

from fhirclient.models import contactdetail

from fhirclient.models import fhirdatatypes

from fhirclient.models import identifier

from fhirclient.codesystems import publicationstatus

from fhirclient.models import usagecontext

