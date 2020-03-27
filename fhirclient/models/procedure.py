#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Procedure)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Procedure(domainresource.DomainResource):
    """ An action that is being or was performed on a patient.
    
    An action that is or was performed on or for a patient. This can be a
    physical intervention like an operation, or less invasive like long term
    services, counseling, or hypnotherapy.
    """
    
    resource_type = "Procedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Identifiers for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.basedOn = None
        """ A request for this procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ Classification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the procedure was performed on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performedDateTime = None
        """ When the procedure was performed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.performedPeriod = None
        """ When the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.performedString = None
        """ When the procedure was performed.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.performedAge = None
        """ When the procedure was performed.
        Type `Age` (represented as `dict` in JSON). """
        
        self.performedRange = None
        """ When the procedure was performed.
        Type `Range` (represented as `dict` in JSON). """
        
        self.recorder = None
        """ Who recorded the procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.asserter = None
        """ Person who asserts this procedure.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the procedure happened.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Coded reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ The justification that the procedure was performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target body sites.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ The result of procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report resulting from the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complicationDetail = None
        """ A condition that is a result of the procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional information about the procedure.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.focalDevice = None
        """ Manipulated, implanted, or removed device.
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.usedReference = None
        """ Items used during procedure.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.usedCode = None
        """ Coded items used during the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, eventstatus.EventStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("performedDateTime", "performedDateTime", fhirdatatypes.FHIRDateTime, False, "performed", False, None), 
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False, None), 
            ("performedString", "performedString", fhirdatatypes.FHIRString, False, "performed", False, None), 
            ("performedAge", "performedAge", age.Age, False, "performed", False, None), 
            ("performedRange", "performedRange", range.Range, False, "performed", False, None), 
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False, None), 
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False, None), 
            ("performer", "performer", ProcedurePerformer, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False, None), 
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False, None), 
            ("report", "report", fhirreference.FHIRReference, True, None, False, None), 
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False, None), 
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False, None), 
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False, None), 
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False, None), 
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ Manipulated, implanted, or removed device.
    
    A device that is implanted, removed or otherwise manipulated (calibration,
    battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as
    a focal portion of the Procedure.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Kind of change to device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated = None
        """ Device that was changed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False, None), 
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js




class ProcedurePerformer(backboneelement.BackboneElement):
    """ The people who performed the procedure.
    
    Limited to "real" people rather than equipment.
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
        """ The reference to the practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization the device or practitioner was acting for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import age

from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.codesystems import eventstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import range

