#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Element)
#  2020, SMART Health IT.


from fhirclient.models import fhirabstractbase

class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.
    
    Base definition for all elements in a resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.id = None
        """ Unique id for inter-element referencing.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.extension = None
        """ Additional content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
        
        super(Element, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension
        from . import fhirdatatypes
        js.extend([
            ("id", "id", fhirdatatypes.FHIRString, False, None, False, None), 
            ("extension", "extension", extension.Extension, True, None, False, None), 
        ])
        return js



