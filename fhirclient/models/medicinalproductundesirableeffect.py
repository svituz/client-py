#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicinalProductUndesirableEffect(domainresource.DomainResource):
    """ MedicinalProductUndesirableEffect.
    
    Describe the undesirable effects of the medicinal product.
    """
    
    resource_type = "MedicinalProductUndesirableEffect"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.subject = None
        """ The medication for which this is an indication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.symptomConditionEffect = None
        """ The symptom, condition or undesirable effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.classification = None
        """ Classification of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequencyOfOccurrence = None
        """ The frequency of occurrence of the effect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.population = None
        """ The population group to which this applies.
        List of `Population` items (represented as `dict` in JSON). """
        
        super(MedicinalProductUndesirableEffect, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductUndesirableEffect, self).elementProperties()
        js.extend([
            ("subject", "subject", fhirreference.FHIRReference, True, None, False, None), 
            ("symptomConditionEffect", "symptomConditionEffect", codeableconcept.CodeableConcept, False, None, False, None), 
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False, None), 
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False, None), 
            ("population", "population", population.Population, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirreference

from fhirclient.models import population

