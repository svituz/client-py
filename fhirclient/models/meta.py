#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Meta) on 2020-03-26.
#  2020, SMART Health IT.


from . import element

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
            ("versionId", "versionId", fhirdatatypes.FHIRId, False, None, False),
            ("lastUpdated", "lastUpdated", fhirdatatypes.FHIRInstant, False, None, False),
            ("source", "source", fhirdatatypes.FHIRUri, False, None, False),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, True, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
        ])
        return js



import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

