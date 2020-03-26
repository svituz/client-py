#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2020-03-26.
#  2020, SMART Health IT.


from . import element

class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.
    
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    
    resource_type = "RelatedArtifact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.citation = None
        """ Bibliographic citation for the artifact.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.display = None
        """ Brief description of the related artifact.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.document = None
        """ What document is being referenced.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.label = None
        """ Short label.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.resource = None
        """ What resource is being referenced.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from | depends-on | composed-of.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.url = None
        """ Where the artifact can be accessed.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        super(RelatedArtifact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("citation", "citation", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("display", "display", fhirdatatypes.FHIRString, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("label", "label", fhirdatatypes.FHIRString, False, None, False),
            ("resource", "resource", fhirdatatypes.FHIRCanonical, False, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True),
            ("url", "url", fhirdatatypes.FHIRUrl, False, None, False),
        ])
        return js



import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

