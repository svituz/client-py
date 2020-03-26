#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

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
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatatypes.FHIRDateTime, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", fhirdatatypes.FHIRString, False, "occurrence", True),
            ("recorded", "recorded", fhirdatatypes.FHIRDateTime, False, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", fhirdatatypes.FHIRString, False, None, False),
            ("expirationDate", "expirationDate", fhirdatatypes.FHIRDate, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False),
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
        ])
        return js



from . import backboneelement

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
            ("documentType", "documentType", fhirdatatypes.FHIRString, False, None, False),
            ("reference", "reference", fhirdatatypes.FHIRUri, False, None, False),
            ("publicationDate", "publicationDate", fhirdatatypes.FHIRDateTime, False, None, False),
            ("presentationDate", "presentationDate", fhirdatatypes.FHIRDateTime, False, None, False),
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
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
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
            ("series", "series", fhirdatatypes.FHIRString, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "doseNumber", True),
            ("doseNumberString", "doseNumberString", fhirdatatypes.FHIRString, False, "doseNumber", True),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", fhirdatatypes.FHIRString, False, "seriesDoses", False),
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
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
        ])
        return js



import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']

try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']

try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

