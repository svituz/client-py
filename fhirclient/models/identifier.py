#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Identifier)
#  2020, SMART Health IT.


from fhirclient.models import element

class Identifier(element.Element):
    """ An identifier intended for computation.
    
    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.use = None
        """ usual | official | temp | secondary | old (If known).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.system = None
        """ The namespace for the identifier value.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.value = None
        """ The value that is unique.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.assigner = None
        """ Organization that issued id (may be just text).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Identifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("use", "use", fhirdatatypes.FHIRCode, False, None, False, identifieruse.IdentifierUse), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("system", "system", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("value", "value", fhirdatatypes.FHIRString, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("assigner", "assigner", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import identifieruse

from fhirclient.models import period

