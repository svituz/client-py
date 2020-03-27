#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Attachment)
#  2020, SMART Health IT.


from . import element

class Attachment(element.Element):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ Mime type of the content, with charset etc..
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.language = None
        """ Human language of the content (BCP-47).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.data = None
        """ Data inline, base64ed.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.url = None
        """ Uri where the data can be found.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.size = None
        """ Number of bytes of content (if url provided).
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.hash = None
        """ Hash of the data (sha-1, base64ed).
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.title = None
        """ Label to display in place of the data.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.creation = None
        """ Date attachment was first created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(Attachment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", fhirdatatypes.FHIRCode, False, None, False),
            ("language", "language", fhirdatatypes.FHIRCode, False, None, False),
            ("data", "data", fhirdatatypes.FHIRBase64Binary, False, None, False),
            ("url", "url", fhirdatatypes.FHIRUrl, False, None, False),
            ("size", "size", fhirdatatypes.FHIRUnsignedInt, False, None, False),
            ("hash", "hash", fhirdatatypes.FHIRBase64Binary, False, None, False),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("creation", "creation", fhirdatatypes.FHIRDateTime, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

