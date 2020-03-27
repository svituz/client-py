#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HumanName)
#  2020, SMART Health IT.


from fhirclient.models import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.
    
    A human's name with the ability to identify parts and usage.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.use = None
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.text = None
        """ Text representation of the full name.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.family = None
        """ Family name (often called 'Surname').
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.given = None
        """ Given names (not always 'first'). Includes middle names.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.prefix = None
        """ Parts that come before the name.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.suffix = None
        """ Parts that come after the name.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.period = None
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("use", "use", fhirdatatypes.FHIRCode, False, None, False, nameuse.NameUse), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("family", "family", fhirdatatypes.FHIRString, False, None, False, None), 
            ("given", "given", fhirdatatypes.FHIRString, True, None, False, None), 
            ("prefix", "prefix", fhirdatatypes.FHIRString, True, None, False, None), 
            ("suffix", "suffix", fhirdatatypes.FHIRString, True, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import nameuse

from fhirclient.models import period

