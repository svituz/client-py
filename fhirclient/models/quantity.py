#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MoneyQuantity) on 2019-05-07.
#  2019, SMART Health IT.
from fhirclient.datatypes.primitive import FHIRCode, FHIRString, FHIRUri
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
        Type `str`. """
        
        self.comparator = None
        """ < | <= | >= | > - how to understand the value.
        Type `str`. """
        
        self.system = None
        """ System that defines coded unit form.
        Type `str`. """
        
        self.unit = None
        """ Unit representation.
        Type `str`. """
        
        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        super(Quantity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("code", "code", FHIRCode, False, None, False),
            ("comparator", "comparator", FHIRCode, False, None, False),
            ("system", "system", FHIRUri, False, None, False),
            ("unit", "unit", FHIRString, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


