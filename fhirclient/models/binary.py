#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Binary)
#  2020, SMART Health IT.


from fhirclient.models import resource

class Binary(resource.Resource):
    """ Pure binary content defined by a format other than FHIR.
    
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """
    
    resource_type = "Binary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ MimeType of the binary content.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.securityContext = None
        """ Identifies another resource to use as proxy when enforcing access
        control.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.data = None
        """ The actual content.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        super(Binary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Binary, self).elementProperties()
        js.extend([
            ("contentType", "contentType", fhirdatatypes.FHIRCode, False, None, True, None), 
            ("securityContext", "securityContext", fhirreference.FHIRReference, False, None, False, None), 
            ("data", "data", fhirdatatypes.FHIRBase64Binary, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

