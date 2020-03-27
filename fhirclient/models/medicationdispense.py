#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationDispense)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.
    
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """
    
    resource_type = "MedicationDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Event that dispense is part of.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | cancelled | on-hold | completed |
        entered-in-error | stopped | declined | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReasonCodeableConcept = None
        """ Why a dispense was not performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusReasonReference = None
        """ Why a dispense was not performed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of medication dispense.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What medication was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the dispense is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Information that supports the dispensing of the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who performed event.
        List of `MedicationDispensePerformer` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the dispense occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.daysSupply = None
        """ Amount of medication expressed as a timing amount.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.whenPrepared = None
        """ When product was packaged and reviewed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.whenHandedOver = None
        """ When product was given out.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Who collected the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the dispense.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ How the medication is to be used by the patient or administered by
        the caregiver.
        List of `Dosage` items (represented as `dict` in JSON). """
        
        self.substitution = None
        """ Whether a substitution was performed on the dispense.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """
        
        self.detectedIssue = None
        """ Clinical issue with action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ A list of relevant lifecycle events.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicationDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, medicationdispensestatuscodes.MedicationDispenseStatusCodes), 
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", codeableconcept.CodeableConcept, False, "statusReason", False, None), 
            ("statusReasonReference", "statusReasonReference", fhirreference.FHIRReference, False, "statusReason", False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True, None), 
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("context", "context", fhirreference.FHIRReference, False, None, False, None), 
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False, None), 
            ("performer", "performer", MedicationDispensePerformer, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("daysSupply", "daysSupply", quantity.Quantity, False, None, False, None), 
            ("whenPrepared", "whenPrepared", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("whenHandedOver", "whenHandedOver", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("destination", "destination", fhirreference.FHIRReference, False, None, False, None), 
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False, None), 
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False, None), 
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False, None), 
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class MedicationDispensePerformer(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who or what performed the event.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.function = None
        """ Who performed the dispense and what they did.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MedicationDispensePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js




class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Whether a substitution was performed on the dispense.
    
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.wasSubstituted = None
        """ Whether a substitution was or was not performed on the dispense.
        Type `bool`. """
        
        self.type = None
        """ Code signifying whether a different drug was dispensed from what
        was prescribed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.responsibleParty = None
        """ Who is responsible for the substitution.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicationDispenseSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("wasSubstituted", "wasSubstituted", bool, False, None, True, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import dosage

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import medicationdispensestatuscodes

from fhirclient.models import quantity

