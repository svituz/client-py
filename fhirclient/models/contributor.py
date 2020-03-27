#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Contributor)
#  2020, SMART Health IT.


from fhirclient.models import element

class Contributor(element.Element):
    """ Contributor information.
    
    A contributor to the content of a knowledge asset, including authors,
    editors, reviewers, and endorsers.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ author | editor | reviewer | endorser.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.name = None
        """ Who contributed the content.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details of the contributor.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        super(Contributor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, contributortype.ContributorType), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
        ])
        return js



from fhirclient.models import contactdetail

from fhirclient.codesystems import contributortype

from fhirclient.models import fhirdatatypes

