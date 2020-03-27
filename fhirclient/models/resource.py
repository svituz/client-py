#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Resource)
#  2020, SMART Health IT.


from fhirclient.models import fhirabstractresource

class Resource(fhirabstractresource.FHIRAbstractResource):
    """ Base Resource.
    
    This is the base resource type for everything.
    """
    
    resource_type = "Resource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.id = None
        """ Logical id of this artifact.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.meta = None
        """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.implicitRules = None
        """ A set of rules under which this content was created.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.language = None
        """ Language of the resource content.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(Resource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend([
            ("id", "id", fhirdatatypes.FHIRString, False, None, False, None), 
            ("meta", "meta", meta.Meta, False, None, False, None), 
            ("implicitRules", "implicitRules", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("language", "language", fhirdatatypes.FHIRCode, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import meta

