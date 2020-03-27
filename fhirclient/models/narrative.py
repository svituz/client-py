#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Narrative)
#  2020, SMART Health IT.


from fhirclient.models import element

class Narrative(element.Element):
    """ Human-readable summary of the resource (essential clinical and business
    information).
    
    A human-readable summary of the resource conveying the essential clinical
    and business information for the resource.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.status = None
        """ generated | extensions | additional | empty.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.div = None
        """ Limited xhtml content.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(Narrative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, narrativestatus.NarrativeStatus), 
            ("div", "div", fhirdatatypes.FHIRString, False, None, True, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.codesystems import narrativestatus

