#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/UsageContext)
#  2020, SMART Health IT.


from fhirclient.models import element

class UsageContext(element.Element):
    """ Describes the context of use for a conformance or knowledge resource.
    
    Specifies clinical/business/etc. metadata that can be used to retrieve,
    index and/or categorize an artifact. This metadata can either be specific
    to the applicable population (e.g., age category, DRG) or the specific
    context of care (e.g., venue, care setting, provider of care).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Type of context being specified.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Value that defines the context.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value that defines the context.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value that defines the context.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value that defines the context.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, True, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True, None), 
            ("valueRange", "valueRange", range.Range, False, "value", True, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import fhirreference

from fhirclient.models import quantity

from fhirclient.models import range

