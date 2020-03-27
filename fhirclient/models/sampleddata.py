#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SampledData)
#  2020, SMART Health IT.


from fhirclient.models import element

class SampledData(element.Element):
    """ A series of measurements taken by a device.
    
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.origin = None
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.period = None
        """ Number of milliseconds between samples.
        Type `float`. """
        
        self.factor = None
        """ Multiply data by this before adding to origin.
        Type `float`. """
        
        self.lowerLimit = None
        """ Lower limit of detection.
        Type `float`. """
        
        self.upperLimit = None
        """ Upper limit of detection.
        Type `float`. """
        
        self.dimensions = None
        """ Number of sample points at each time point.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.data = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(SampledData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("origin", "origin", quantity.Quantity, False, None, True, None), 
            ("period", "period", float, False, None, True, None), 
            ("factor", "factor", float, False, None, False, None), 
            ("lowerLimit", "lowerLimit", float, False, None, False, None), 
            ("upperLimit", "upperLimit", float, False, None, False, None), 
            ("dimensions", "dimensions", fhirdatatypes.FHIRPositiveInt, False, None, True, None), 
            ("data", "data", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import quantity

