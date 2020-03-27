#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Immunization)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    
    Describes the event of a patient being administered a vaccine or a record
    of an immunization as reported by a patient, a clinician or another party.
    """
    
    resource_type = "Immunization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ completed | entered-in-error | not-done.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason not done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who was immunized.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter immunization was part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ Vaccine administration date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.occurrenceString = None
        """ Vaccine administration date.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.recorded = None
        """ When the immunization was first captured in the subject's record.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.primarySource = None
        """ Indicates context the data was recorded in.
        Type `bool`. """
        
        self.reportOrigin = None
        """ Indicates the source of a secondarily reported record.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where immunization occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Vaccine lot number.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseQuantity = None
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who performed event.
        List of `ImmunizationPerformer` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional immunization notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why immunization occurred.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.isSubpotent = None
        """ Dose potency.
        Type `bool`. """
        
        self.subpotentReason = None
        """ Reason for being subpotent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.education = None
        """ Educational material presented to patient.
        List of `ImmunizationEducation` items (represented as `dict` in JSON). """
        
        self.programEligibility = None
        """ Patient eligibility for a vaccination program.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.fundingSource = None
        """ Funding source for the vaccine.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.protocolApplied = None
        """ Protocol followed by the provider.
        List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON). """
        
        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, eventstatus.EventStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", True, None), 
            ("occurrenceString", "occurrenceString", fhirdatatypes.FHIRString, False, "occurrence", True, None), 
            ("recorded", "recorded", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("primarySource", "primarySource", bool, False, None, False, None), 
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False, None), 
            ("lotNumber", "lotNumber", fhirdatatypes.FHIRString, False, None, False, None), 
            ("expirationDate", "expirationDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("site", "site", codeableconcept.CodeableConcept, False, None, False, None), 
            ("route", "route", codeableconcept.CodeableConcept, False, None, False, None), 
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False, None), 
            ("performer", "performer", ImmunizationPerformer, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("isSubpotent", "isSubpotent", bool, False, None, False, None), 
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("education", "education", ImmunizationEducation, True, None, False, None), 
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False, None), 
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False, None), 
            ("reaction", "reaction", ImmunizationReaction, True, None, False, None), 
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ImmunizationEducation(backboneelement.BackboneElement):
    """ Educational material presented to patient.
    
    Educational material presented to the patient (or guardian) at the time of
    vaccine administration.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentType = None
        """ Educational material document identifier.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.reference = None
        """ Educational material reference pointer.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.publicationDate = None
        """ Educational material publication date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.presentationDate = None
        """ Educational material presentation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        super(ImmunizationEducation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", fhirdatatypes.FHIRString, False, None, False, None), 
            ("reference", "reference", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("publicationDate", "publicationDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("presentationDate", "presentationDate", fhirdatatypes.FHIRDateTime, False, None, False, None), 
        ])
        return js




class ImmunizationPerformer(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who performed the immunization event.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.function = None
        """ What type of performance was done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Individual or organization who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImmunizationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js




class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ Protocol followed by the provider.
    
    The protocol (set of recommendations) being followed by the provider who
    administered the dose.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.series = None
        """ Name of vaccine series.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.authority = None
        """ Who is responsible for publishing the recommendations.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.targetDisease = None
        """ Vaccine preventatable disease being targetted.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.doseNumberPositiveInt = None
        """ Dose number within series.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.doseNumberString = None
        """ Dose number within series.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.seriesDosesPositiveInt = None
        """ Recommended number of doses for immunity.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.seriesDosesString = None
        """ Recommended number of doses for immunity.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ImmunizationProtocolApplied, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("series", "series", fhirdatatypes.FHIRString, False, None, False, None), 
            ("authority", "authority", fhirreference.FHIRReference, False, None, False, None), 
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False, None), 
            ("doseNumberPositiveInt", "doseNumberPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "doseNumber", True, None), 
            ("doseNumberString", "doseNumberString", fhirdatatypes.FHIRString, False, "doseNumber", True, None), 
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "seriesDoses", False, None), 
            ("seriesDosesString", "seriesDosesString", fhirdatatypes.FHIRString, False, "seriesDoses", False, None), 
        ])
        return js




class ImmunizationReaction(backboneelement.BackboneElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When reaction started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reported = None
        """ Indicates self-reported reaction.
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("detail", "detail", fhirreference.FHIRReference, False, None, False, None), 
            ("reported", "reported", bool, False, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.codesystems import eventstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import quantity

