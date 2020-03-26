#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/canonical) on 2020-03-26.
#  2020, SMART Health IT.


from . import fhirabstractbase

class FHIRCanonical(fhirabstractbase.FHIRUri):
    """ Primitive Type canonical.
    
    A URI that is a reference to a canonical URL on a FHIR resource
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.value = None
        """ Primitive value for canonical.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(FHIRCanonical, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FHIRCanonical, self).elementProperties()
        js.extend([
            ("value", "value", FHIRCanonical, False, None, False),
        ])
        return js



