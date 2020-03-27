#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Annotation)
#  2020, SMART Health IT.


from fhirclient.models import element

class Annotation(element.Element):
    """ Text node with attribution.
    
    A  text note which also  contains information about who made the statement
    and when.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorReference = None
        """ Individual responsible for the annotation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authorString = None
        """ Individual responsible for the annotation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.time = None
        """ When the annotation was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.text = None
        """ The annotation  - text content (as markdown).
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False, "author", False, None), 
            ("authorString", "authorString", fhirdatatypes.FHIRString, False, "author", False, None), 
            ("time", "time", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRMarkdown, False, None, True, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

