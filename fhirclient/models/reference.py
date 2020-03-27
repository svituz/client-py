#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Reference)
#  2020, SMART Health IT.


from fhirclient.models import element

class Reference(element.Element):
    """ A reference from one resource to another.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Literal reference, Relative, internal or absolute URL.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ Type the reference refers to (e.g. "Patient").
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Logical reference, when literal reference is not known.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.display = None
        """ Text alternative for the resource.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(Reference, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("display", "display", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import identifier

