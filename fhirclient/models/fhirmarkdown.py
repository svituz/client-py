#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/markdown) on 2020-03-26.
#  2020, SMART Health IT.


from . import fhirabstractbase

class FHIRMarkdown(fhirabstractbase.FHIRString):
    """ Primitive Type markdown.
    
    A string that may contain Github Flavored Markdown syntax for optional
    processing by a mark down presentation engine
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.value = None
        """ Primitive value for markdown.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(FHIRMarkdown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FHIRMarkdown, self).elementProperties()
        js.extend([
            ("value", "value", FHIRMarkdown, False, None, False),
        ])
        return js



