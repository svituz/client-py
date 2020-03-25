#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MoneyQuantity) on 2020-03-25.
#  2020, SMART Health IT.


from . import element

class Quantity(element.Element):
    """ A measured or measurable amount.
    
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    
    resource_type = "Quantity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded form of the unit.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.comparator = None
        """ < | <= | >= | > - how to understand the value.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.system = None
        """ System that defines coded unit form.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.unit = None
        """ Unit representation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False),
            ("comparator", "comparator", fhirdatatypes.FHIRCode, False, None, False),
            ("system", "system", fhirdatatypes.FHIRUri, False, None, False),
            ("unit", "unit", fhirdatatypes.FHIRString, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

