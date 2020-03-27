#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Signature)
#  2020, SMART Health IT.


from fhirclient.models import element

class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..
    
    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        """ When the signature was created.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.who = None
        """ Who signed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ The party represented.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.targetFormat = None
        """ The technical format of the signed resources.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.sigFormat = None
        """ The technical format of the signature.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.data = None
        """ The actual signature content (XML DigSig. JWS, picture, etc.).
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, True, None, True, None), 
            ("when", "when", fhirdatatypes.FHIRInstant, False, None, True, None), 
            ("who", "who", fhirreference.FHIRReference, False, None, True, None), 
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False, None), 
            ("targetFormat", "targetFormat", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("sigFormat", "sigFormat", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("data", "data", fhirdatatypes.FHIRBase64Binary, False, None, False, None), 
        ])
        return js



from fhirclient.models import coding

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

