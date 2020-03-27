#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicinalProductInteraction(domainresource.DomainResource):
    """ MedicinalProductInteraction.
    
    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    
    resource_type = "MedicinalProductInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.subject = None
        """ The medication for which this is a described interaction.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.description = None
        """ The interaction described.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.interactant = None
        """ The specific medication, food or laboratory test that interacts.
        List of `MedicinalProductInteractionInteractant` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The type of the interaction e.g. drug-drug interaction, drug-food
        interaction, drug-lab test interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.effect = None
        """ The effect of the interaction, for example "reduced gastric
        absorption of primary medication".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.incidence = None
        """ The incidence of the interaction, e.g. theoretical, observed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.management = None
        """ Actions for managing the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("subject", "subject", fhirreference.FHIRReference, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("interactant", "interactant", MedicinalProductInteractionInteractant, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("effect", "effect", codeableconcept.CodeableConcept, False, None, False, None), 
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False, None), 
            ("management", "management", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicinalProductInteractionInteractant(backboneelement.BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.itemReference = None
        """ The specific medication, food or laboratory test that interacts.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.itemCodeableConcept = None
        """ The specific medication, food or laboratory test that interacts.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductInteractionInteractant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True, None), 
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

