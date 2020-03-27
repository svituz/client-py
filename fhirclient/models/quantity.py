#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MoneyQuantity)
#  2020, SMART Health IT.


from fhirclient.models import element

class Quantity(element.Element):
    """ A measured or measurable amount.
    
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
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
        
        self.comparator = None
        """ < | <= | >= | > - how to understand the value.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.unit = None
        """ Unit representation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.system = None
        """ System that defines coded unit form.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.code = None
        """ Coded form of the unit.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("value", "value", float, False, None, False, None), 
            ("comparator", "comparator", fhirdatatypes.FHIRCode, False, None, False, quantitycomparator.QuantityComparator), 
            ("unit", "unit", fhirdatatypes.FHIRString, False, None, False, None), 
            ("system", "system", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import quantitycomparator

