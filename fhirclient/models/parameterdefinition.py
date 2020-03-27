#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ParameterDefinition)
#  2020, SMART Health IT.


from fhirclient.models import element

class ParameterDefinition(element.Element):
    """ Definition of a parameter to a module.
    
    The parameters to the module. This collection specifies both the input and
    output parameters. Input parameters are provided by the caller as part of
    the $evaluate operation. Output parameters are included in the
    GuidanceResponse.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name used to access the parameter value.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.use = None
        """ in | out.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum cardinality.
        Type `int`. """
        
        self.max = None
        """ Maximum cardinality (a number of *).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.documentation = None
        """ A brief description of the parameter.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ What type of value.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.profile = None
        """ What profile the value is expected to be.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("use", "use", fhirdatatypes.FHIRCode, False, None, True, operationparameteruse.OperationParameterUse), 
            ("min", "min", int, False, None, False, None), 
            ("max", "max", fhirdatatypes.FHIRString, False, None, False, None), 
            ("documentation", "documentation", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, None), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import operationparameteruse

