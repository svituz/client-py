#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ Allergy or Intolerance (generally: Risk of adverse reaction to a substance).
    
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    
    resource_type = "AllergyIntolerance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.clinicalStatus = None
        """ active | inactive | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.verificationStatus = None
        """ unconfirmed | confirmed | refuted | entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ allergy | intolerance - Underlying mechanism (if known).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ food | medication | environment | biologic.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.criticality = None
        """ low | high | unable-to-assess.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Code that identifies the allergy or intolerance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who the sensitivity is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter when the allergy or intolerance was asserted.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onsetDateTime = None
        """ When allergy or intolerance was identified.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.onsetAge = None
        """ When allergy or intolerance was identified.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetPeriod = None
        """ When allergy or intolerance was identified.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ When allergy or intolerance was identified.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ When allergy or intolerance was identified.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.recordedDate = None
        """ Date first version of the resource instance was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recorder = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.asserter = None
        """ Source of the information about the allergy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lastOccurrence = None
        """ Date(/time) of last known occurrence of a reaction.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.note = None
        """ Additional text not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """
        
        super(AllergyIntolerance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False, None), 
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False, None), 
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False, allergyintolerancetype.AllergyIntoleranceType), 
            ("category", "category", fhirdatatypes.FHIRCode, True, None, False, allergyintolerancecategory.AllergyIntoleranceCategory), 
            ("criticality", "criticality", fhirdatatypes.FHIRCode, False, None, False, allergyintolerancecriticality.AllergyIntoleranceCriticality), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("onsetDateTime", "onsetDateTime", fhirdatatypes.FHIRDateTime, False, "onset", False, None), 
            ("onsetAge", "onsetAge", age.Age, False, "onset", False, None), 
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False, None), 
            ("onsetRange", "onsetRange", range.Range, False, "onset", False, None), 
            ("onsetString", "onsetString", fhirdatatypes.FHIRString, False, "onset", False, None), 
            ("recordedDate", "recordedDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False, None), 
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False, None), 
            ("lastOccurrence", "lastOccurrence", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ Adverse Reaction Events linked to exposure to substance.
    
    Details about each adverse reaction event linked to exposure to the
    identified substance.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.substance = None
        """ Specific substance or pharmaceutical product considered to be
        responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manifestation = None
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of the event as a whole.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.onset = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.severity = None
        """ mild | moderate | severe (of event as a whole).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.exposureRoute = None
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Text about event not captured in other fields.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(AllergyIntoleranceReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False, None), 
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("onset", "onset", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("severity", "severity", fhirdatatypes.FHIRCode, False, None, False, allergyintoleranceseverity.AllergyIntoleranceSeverity), 
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import age

from fhirclient.codesystems import allergyintolerancecategory

from fhirclient.codesystems import allergyintolerancecriticality

from fhirclient.codesystems import allergyintoleranceseverity

from fhirclient.codesystems import allergyintolerancetype

from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import range

