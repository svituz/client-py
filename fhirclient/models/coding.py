#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coding) on 2020-03-25.
#  2020, SMART Health IT.


from . import element

class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_type = "Coding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Symbol in syntax defined by the system.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.display = None
        """ Representation defined by the system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.system = None
        """ Identity of the terminology system.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.userSelected = None
        """ If this coding was chosen directly by the user.
        Type `bool`. """
        
        self.version = None
        """ Version of the system - if relevant.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(Coding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRCode, False, None, False),
            ("display", "display", fhirdatatypes.FHIRString, False, None, False),
            ("system", "system", fhirdatatypes.FHIRUri, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

