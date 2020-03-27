#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Dosage)
#  2020, SMART Health IT.


from fhirclient.models import backboneelement

class Dosage(backboneelement.BackboneElement):
    """ How the medication is/was taken or should be taken.
    
    Indicates how the medication is/was taken or should be taken by the
    patient.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequence = None
        """ The order of the dosage instructions.
        Type `int`. """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.additionalInstruction = None
        """ Supplemental instruction or warnings to the patient - e.g. "with
        meals", "may cause drowsiness".
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        """ Patient or consumer oriented instructions.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseAndRate = None
        """ Amount of medication administered.
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.maxDosePerAdministration = None
        """ Upper limit on medication per administration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerLifetime = None
        """ Upper limit on medication per lifetime of the patient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("sequence", "sequence", int, False, None, False, None), 
            ("text", "text", fhirdatatypes.FHIRString, False, None, False, None), 
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("patientInstruction", "patientInstruction", fhirdatatypes.FHIRString, False, None, False, None), 
            ("timing", "timing", timing.Timing, False, None, False, None), 
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False, None), 
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False, None), 
            ("site", "site", codeableconcept.CodeableConcept, False, None, False, None), 
            ("route", "route", codeableconcept.CodeableConcept, False, None, False, None), 
            ("method", "method", codeableconcept.CodeableConcept, False, None, False, None), 
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False, None), 
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False, None), 
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False, None), 
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False, None), 
        ])
        return js



from fhirclient.models import element

class DosageDoseAndRate(element.Element):
    """ Amount of medication administered.
    
    The amount of medication administered.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The kind of dose or rate specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Amount of medication per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("doseRange", "doseRange", range.Range, False, "dose", False, None), 
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False, None), 
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False, None), 
            ("rateRange", "rateRange", range.Range, False, "rate", False, None), 
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.models import ratio

from fhirclient.models import timing

