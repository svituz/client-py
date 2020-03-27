#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_type = "MedicationAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiates = None
        """ Instantiates protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | not-done | on-hold | completed | entered-in-error |
        stopped | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of medication usage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What was administered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who received medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or Episode of Care administered as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Additional information to support administration.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Start and end time of administration.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who performed the medication administration and what they did.
        List of `MedicationAdministrationPerformer` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition or observation that supports why the medication was
        administered.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Request administration performed against.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the administration.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiates", "instantiates", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, medicationadministrationstatuscodes.MedicationAdministrationStatusCodes), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True, None), 
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("context", "context", fhirreference.FHIRReference, False, None, False, None), 
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False, None), 
            ("effectiveDateTime", "effectiveDateTime", fhirdatatypes.FHIRDateTime, False, "effective", True, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", True, None), 
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("request", "request", fhirreference.FHIRReference, False, None, False, None), 
            ("device", "device", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False, None), 
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.site = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dose = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Dose quantity per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("site", "site", codeableconcept.CodeableConcept, False, None, False, None), 
            ("route", "route", codeableconcept.CodeableConcept, False, None, False, None), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
            ("dose", "dose", quantity.Quantity, False, None, False, None), 
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False, None), 
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False, None), 
        ])
        return js




class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """ Who performed the medication administration and what they did.
    
    Indicates who or what performed the medication administration and how they
    were involved.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Who performed the medication administration.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MedicationAdministrationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import medicationadministrationstatuscodes

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import ratio

