#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Money)
#  2020, SMART Health IT.


from fhirclient.models import element

class Money(element.Element):
    """ An amount of economic utility in some recognized currency.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        self.currency = None
        """ ISO 4217 Currency Code.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(Money, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("value", "value", float, False, None, False, None), 
            ("currency", "currency", fhirdatatypes.FHIRCode, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

