#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ContactPoint)
#  2020, SMART Health IT.


from fhirclient.models import element

class ContactPoint(element.Element):
    """ Details of a Technology mediated contact point (phone, fax, email, etc.).
    
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.system = None
        """ phone | fax | email | pager | url | sms | other.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.value = None
        """ The actual contact point details.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.use = None
        """ home | work | temp | old | mobile - purpose of this contact point.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.rank = None
        """ Specify preferred order of use (1 = highest).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.period = None
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        super(ContactPoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("system", "system", fhirdatatypes.FHIRCode, False, None, False, contactpointsystem.ContactPointSystem), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, False, None), 
            ("use", "use", fhirdatatypes.FHIRCode, False, None, False, contactpointuse.ContactPointUse), 
            ("rank", "rank", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import contactpointsystem

from fhirclient.codesystems import contactpointuse

from fhirclient.models import fhirdatatypes

from fhirclient.models import period

