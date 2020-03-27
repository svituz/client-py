#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Medication)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    
    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    
    resource_type = "Medication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier for this medication.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.form = None
        """ powder | tablets | capsule +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amount = None
        """ Amount of drug in package.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationIngredient` items (represented as `dict` in JSON). """
        
        self.batch = None
        """ Details about packaged medications.
        Type `MedicationBatch` (represented as `dict` in JSON). """
        
        super(Medication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, medicationstatuscodes.MedicationStatusCodes), 
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False, None), 
            ("form", "form", codeableconcept.CodeableConcept, False, None, False, None), 
            ("amount", "amount", ratio.Ratio, False, None, False, None), 
            ("ingredient", "ingredient", MedicationIngredient, True, None, False, None), 
            ("batch", "batch", MedicationBatch, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicationBatch(backboneelement.BackboneElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.lotNumber = None
        """ Identifier assigned to batch.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expirationDate = None
        """ When batch will expire.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(MedicationBatch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("lotNumber", "lotNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("expirationDate", "expirationDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
        ])
        return js




class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.itemCodeableConcept = None
        """ The actual ingredient or content.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ The actual ingredient or content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.isActive = None
        """ Active ingredient indicator.
        Type `bool`. """
        
        self.strength = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True, None), 
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True, None), 
            ("isActive", "isActive", bool, False, None, False, None), 
            ("strength", "strength", ratio.Ratio, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import medicationstatuscodes

from fhirclient.models import ratio

