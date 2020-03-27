#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicinalProductIngredient(domainresource.DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    
    resource_type = "MedicinalProductIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifier for the ingredient.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.role = None
        """ Ingredient role e.g. Active ingredient, excipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.allergenicIndicator = None
        """ If the ingredient is a known or suspected allergen.
        Type `bool`. """
        
        self.manufacturer = None
        """ Manufacturer of this Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specifiedSubstance = None
        """ A specified substance that comprises this ingredient.
        List of `MedicinalProductIngredientSpecifiedSubstance` items (represented as `dict` in JSON). """
        
        self.substance = None
        """ The ingredient substance.
        Type `MedicinalProductIngredientSubstance` (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False, None), 
            ("role", "role", codeableconcept.CodeableConcept, False, None, True, None), 
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False, None), 
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False, None), 
            ("specifiedSubstance", "specifiedSubstance", MedicinalProductIngredientSpecifiedSubstance, True, None, False, None), 
            ("substance", "substance", MedicinalProductIngredientSubstance, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ The specified substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.group = None
        """ The group of specified substance, e.g. group 1 to 4.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ Confidentiality level of the specified substance as the ingredient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.strength = None
        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSpecifiedSubstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("group", "group", codeableconcept.CodeableConcept, False, None, True, None), 
            ("confidentiality", "confidentiality", codeableconcept.CodeableConcept, False, None, False, None), 
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False, None), 
        ])
        return js




class MedicinalProductIngredientSpecifiedSubstanceStrength(backboneelement.BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.presentation = None
        """ The quantity of substance in the unit of presentation, or in the
        volume (or mass) of the single pharmaceutical product or
        manufactured item.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.presentationLowLimit = None
        """ A lower limit for the quantity of substance in the unit of
        presentation. For use when there is a range of strengths, this is
        the lower limit, with the presentation attribute becoming the upper
        limit.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.concentration = None
        """ The strength per unitary volume (or mass).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.concentrationLowLimit = None
        """ A lower limit for the strength per unitary volume (or mass), for
        when there is a range. The concentration attribute then becomes the
        upper limit.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.measurementPoint = None
        """ For when strength is measured at a particular point or distance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.country = None
        """ The country or countries for which the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.referenceStrength = None
        """ Strength expressed in terms of a reference substance.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("presentation", "presentation", ratio.Ratio, False, None, True, None), 
            ("presentationLowLimit", "presentationLowLimit", ratio.Ratio, False, None, False, None), 
            ("concentration", "concentration", ratio.Ratio, False, None, False, None), 
            ("concentrationLowLimit", "concentrationLowLimit", ratio.Ratio, False, None, False, None), 
            ("measurementPoint", "measurementPoint", fhirdatatypes.FHIRString, False, None, False, None), 
            ("country", "country", codeableconcept.CodeableConcept, True, None, False, None), 
            ("referenceStrength", "referenceStrength", MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, True, None, False, None), 
        ])
        return js




class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.substance = None
        """ Relevant reference substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.strength = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.strengthLowLimit = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.measurementPoint = None
        """ For when strength is measured at a particular point or distance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.country = None
        """ The country or countries for which the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False, None), 
            ("strength", "strength", ratio.Ratio, False, None, True, None), 
            ("strengthLowLimit", "strengthLowLimit", ratio.Ratio, False, None, False, None), 
            ("measurementPoint", "measurementPoint", fhirdatatypes.FHIRString, False, None, False, None), 
            ("country", "country", codeableconcept.CodeableConcept, True, None, False, None), 
        ])
        return js




class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """ The ingredient substance.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ The ingredient substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.strength = None
        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSubstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import ratio

