#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Substance)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """
    
    resource_type = "Substance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ What class/type of substance this is.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ What substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Textual description of the substance, comments.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.instance = None
        """ If this describes a specific package/container of the substance.
        List of `SubstanceInstance` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
        
        super(Substance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, fhirsubstancestatus.FHIRSubstanceStatus), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("instance", "instance", SubstanceInstance, True, None, False, None), 
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.
    
    A substance can be composed of other substances.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.substanceCodeableConcept = None
        """ A component of the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substanceReference = None
        """ A component of the substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SubstanceIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False, None, False, None), 
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", True, None), 
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", True, None), 
        ])
        return js




class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.
    
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.expiry = None
        """ When no longer valid to use.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.quantity = None
        """ Amount of substance in the package.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SubstanceInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("expiry", "expiry", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import fhirsubstancestatus

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.models import ratio

