#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Money) on 2020-03-26.
#  2020, SMART Health IT.


from . import element

class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """
    
    resource_type = "Money"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.currency = None
        """ ISO 4217 Currency Code.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        super(Money, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("currency", "currency", fhirdatatypes.FHIRCode, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

