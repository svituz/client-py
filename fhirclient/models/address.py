#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Address)
#  2020, SMART Health IT.


from . import element

class Address(element.Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).
    
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.use = None
        """ home | work | temp | old | billing - purpose of this address.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ postal | physical | both.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.text = None
        """ Text representation of the address.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.line = None
        """ Street name, number, direction & P.O. Box etc..
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.city = None
        """ Name of city, town etc..
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.district = None
        """ District name (aka county).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.state = None
        """ Sub-unit of country (abbreviations ok).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.postalCode = None
        """ Postal code for area.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.country = None
        """ Country (e.g. can be ISO 3166 2 or 3 letter code).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.period = None
        """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        super(Address, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("use", "use", fhirdatatypes.FHIRCode, False, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False),
            ("text", "text", fhirdatatypes.FHIRString, False, None, False),
            ("line", "line", fhirdatatypes.FHIRString, True, None, False),
            ("city", "city", fhirdatatypes.FHIRString, False, None, False),
            ("district", "district", fhirdatatypes.FHIRString, False, None, False),
            ("state", "state", fhirdatatypes.FHIRString, False, None, False),
            ("postalCode", "postalCode", fhirdatatypes.FHIRString, False, None, False),
            ("country", "country", fhirdatatypes.FHIRString, False, None, False),
            ("period", "period", period.Period, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']

