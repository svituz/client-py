#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health conditions for a person related to the patient relevant
    in the context of care for the patient.
    """
    
    resource_type = "FamilyMemberHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.status = None
        """ partial | completed | entered-in-error | health-unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.dataAbsentReason = None
        """ subject-unknown | withheld | unable-to-obtain | deferred.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient history is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ When history was recorded or last updated.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.name = None
        """ The family member described.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.relationship = None
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sex = None
        """ male | female | other | unknown.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bornPeriod = None
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
        
        self.bornDate = None
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.bornString = None
        """ (approximate) date of birth.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.ageAge = None
        """ (approximate) age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.ageRange = None
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.ageString = None
        """ (approximate) age.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.estimatedAge = None
        """ Age is estimated?.
        Type `bool`. """
        
        self.deceasedBoolean = None
        """ Dead? How old/when?.
        Type `bool`. """
        
        self.deceasedAge = None
        """ Dead? How old/when?.
        Type `Age` (represented as `dict` in JSON). """
        
        self.deceasedRange = None
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedDate = None
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedString = None
        """ Dead? How old/when?.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.reasonCode = None
        """ Why was family member history performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why was family member history performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ General note about related person.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        
        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, familyhistorystatus.FamilyHistoryStatus), 
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, True, None), 
            ("sex", "sex", codeableconcept.CodeableConcept, False, None, False, None), 
            ("bornPeriod", "bornPeriod", period.Period, False, "born", False, None), 
            ("bornDate", "bornDate", fhirdatatypes.FHIRDate, False, "born", False, None), 
            ("bornString", "bornString", fhirdatatypes.FHIRString, False, "born", False, None), 
            ("ageAge", "ageAge", age.Age, False, "age", False, None), 
            ("ageRange", "ageRange", range.Range, False, "age", False, None), 
            ("ageString", "ageString", fhirdatatypes.FHIRString, False, "age", False, None), 
            ("estimatedAge", "estimatedAge", bool, False, None, False, None), 
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False, None), 
            ("deceasedAge", "deceasedAge", age.Age, False, "deceased", False, None), 
            ("deceasedRange", "deceasedRange", range.Range, False, "deceased", False, None), 
            ("deceasedDate", "deceasedDate", fhirdatatypes.FHIRDate, False, "deceased", False, None), 
            ("deceasedString", "deceasedString", fhirdatatypes.FHIRString, False, "deceased", False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contributedToDeath = None
        """ Whether the condition contributed to the cause of death.
        Type `bool`. """
        
        self.onsetAge = None
        """ When condition first manifested.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetPeriod = None
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ When condition first manifested.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.note = None
        """ Extra information about condition.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False, None), 
            ("contributedToDeath", "contributedToDeath", bool, False, None, False, None), 
            ("onsetAge", "onsetAge", age.Age, False, "onset", False, None), 
            ("onsetRange", "onsetRange", range.Range, False, "onset", False, None), 
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False, None), 
            ("onsetString", "onsetString", fhirdatatypes.FHIRString, False, "onset", False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import age

from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.codesystems import familyhistorystatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import range

