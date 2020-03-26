#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Expression) on 2020-03-26.
#  2020, SMART Health IT.


from . import element

class Expression(element.Element):
    """ An expression that can be used to generate a value.
    
    A expression that is evaluated in a specified context and returns a value.
    The context of use of the expression must specify the context in which the
    expression is evaluated, and how the result of the expression is used.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the condition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Short name assigned to expression for reuse.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.language = None
        """ text/cql | text/fhirpath | application/x-fhir-query | etc..
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.expression = None
        """ Expression in specified language.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.reference = None
        """ Where the expression is found.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        super(Expression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Expression, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("name", "name", fhirdatatypes.FHIRId, False, None, False),
            ("language", "language", fhirdatatypes.FHIRCode, False, None, True),
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False),
            ("reference", "reference", fhirdatatypes.FHIRUri, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

