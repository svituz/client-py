#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Meta)
#  2020, SMART Health IT.


from fhirclient.models import element

class Meta(element.Element):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content might not always
    be associated with version changes to the resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.versionId = None
        """ Version specific identifier.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.source = None
        """ Identifies where the resource comes from.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.tag = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(Meta, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("versionId", "versionId", fhirdatatypes.FHIRId, False, None, False, None), 
            ("lastUpdated", "lastUpdated", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("source", "source", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("security", "security", coding.Coding, True, None, False, None), 
            ("tag", "tag", coding.Coding, True, None, False, None), 
        ])
        return js



from fhirclient.models import coding

from fhirclient.models import fhirdatatypes

