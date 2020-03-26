#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2020-03-26.
#  2020, SMART Health IT.


from . import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.
    
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    
    resource_type = "ParameterDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ A brief description of the parameter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.max = None
        """ Maximum cardinality (a number of *).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum cardinality.
        Type `int`. """
        
        self.name = None
        """ Name used to access the parameter value.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ What profile the value is expected to be.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.type = None
        """ What type of value.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.use = None
        """ in | out.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("documentation", "documentation", fhirdatatypes.FHIRString, False, None, False),
            ("max", "max", fhirdatatypes.FHIRString, False, None, False),
            ("min", "min", int, False, None, False),
            ("name", "name", fhirdatatypes.FHIRCode, False, None, False),
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("use", "use", fhirdatatypes.FHIRCode, False, None, True),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

