#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Range) on 2020-03-26.
#  2020, SMART Health IT.


from . import element

class Range(element.Element):
    """ Set of values bounded by low and high.
    
    A set of ordered Quantities defined by a low and high limit.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.low = None
        """ Low limit.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.high = None
        """ High limit.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Range, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend([
            ("low", "low", quantity.Quantity, False, None, False),
            ("high", "high", quantity.Quantity, False, None, False),
        ])
        return js



import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

