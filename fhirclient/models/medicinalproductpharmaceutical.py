#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicinalProductPharmaceutical(domainresource.DomainResource):
    """ A pharmaceutical product described in terms of its composition and dose
    form.
    """
    
    resource_type = "MedicinalProductPharmaceutical"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ An identifier for the pharmaceutical medicinal product.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.administrableDoseForm = None
        """ The administrable dose form, after necessary reconstitution.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitOfPresentation = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.device = None
        """ Accompanying device.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.characteristics = None
        """ Characteristics e.g. a products onset of action.
        List of `MedicinalProductPharmaceuticalCharacteristics` items (represented as `dict` in JSON). """
        
        self.routeOfAdministration = None
        """ The path by which the pharmaceutical product is taken into or makes
        contact with the body.
        List of `MedicinalProductPharmaceuticalRouteOfAdministration` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceutical, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceutical, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("administrableDoseForm", "administrableDoseForm", codeableconcept.CodeableConcept, False, None, True, None), 
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False, None), 
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False, None), 
            ("device", "device", fhirreference.FHIRReference, True, None, False, None), 
            ("characteristics", "characteristics", MedicinalProductPharmaceuticalCharacteristics, True, None, False, None), 
            ("routeOfAdministration", "routeOfAdministration", MedicinalProductPharmaceuticalRouteOfAdministration, True, None, True, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicinalProductPharmaceuticalCharacteristics(backboneelement.BackboneElement):
    """ Characteristics e.g. a products onset of action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ A coded characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ The status of characteristic e.g. assigned or pending.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalCharacteristics, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("status", "status", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js




class MedicinalProductPharmaceuticalRouteOfAdministration(backboneelement.BackboneElement):
    """ The path by which the pharmaceutical product is taken into or makes contact
    with the body.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded expression for the route.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.firstDose = None
        """ The first dose (dose quantity) administered in humans can be
        specified, for a product under investigation, using a numerical
        value and its unit of measurement.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxSingleDose = None
        """ The maximum single dose that can be administered as per the
        protocol of a clinical trial can be specified using a numerical
        value and its unit of measurement.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerDay = None
        """ The maximum dose per day (maximum dose quantity to be administered
        in any one 24-h period) that can be administered as per the
        protocol referenced in the clinical trial authorisation.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerTreatmentPeriod = None
        """ The maximum dose per treatment period that can be administered as
        per the protocol referenced in the clinical trial authorisation.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.maxTreatmentPeriod = None
        """ The maximum treatment period during which an Investigational
        Medicinal Product can be administered as per the protocol
        referenced in the clinical trial authorisation.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.targetSpecies = None
        """ A species for which this route applies.
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministration, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("firstDose", "firstDose", quantity.Quantity, False, None, False, None), 
            ("maxSingleDose", "maxSingleDose", quantity.Quantity, False, None, False, None), 
            ("maxDosePerDay", "maxDosePerDay", quantity.Quantity, False, None, False, None), 
            ("maxDosePerTreatmentPeriod", "maxDosePerTreatmentPeriod", ratio.Ratio, False, None, False, None), 
            ("maxTreatmentPeriod", "maxTreatmentPeriod", duration.Duration, False, None, False, None), 
            ("targetSpecies", "targetSpecies", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, True, None, False, None), 
        ])
        return js




class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    """ A species for which this route applies.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded expression for the species.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.withdrawalPeriod = None
        """ A species specific time during which consumption of animal product
        is not appropriate.
        List of `MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpecies, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("withdrawalPeriod", "withdrawalPeriod", MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, True, None, False, None), 
        ])
        return js




class MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    """ A species specific time during which consumption of animal product is not
    appropriate.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.tissue = None
        """ Coded expression for the type of tissue for which the withdrawal
        period applues, e.g. meat, milk.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ A value for the time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Extra information about the withdrawal period.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPharmaceuticalRouteOfAdministrationTargetSpeciesWithdrawalPeriod, self).elementProperties()
        js.extend([
            ("tissue", "tissue", codeableconcept.CodeableConcept, False, None, True, None), 
            ("value", "value", quantity.Quantity, False, None, True, None), 
            ("supportingInformation", "supportingInformation", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import duration

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.models import ratio

