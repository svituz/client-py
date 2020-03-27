#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ContactDetail)
#  2020, SMART Health IT.


from fhirclient.models import element

class ContactDetail(element.Element):
    """ Contact information.
    
    Specifies contact information for a person or organization.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of an individual to contact.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.telecom = None
        """ Contact details for individual or organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ContactDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContactDetail, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
        ])
        return js



from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

