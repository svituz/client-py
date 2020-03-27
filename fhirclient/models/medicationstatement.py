#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationStatement)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class MedicationStatement(domainresource.DomainResource):
    """ Record of medication being taken by a patient.
    
    A record of a medication that is being consumed by a patient.   A
    MedicationStatement may indicate that the patient may be taking the
    medication now or has taken the medication in the past or will be taking
    the medication in the future.  The source of this information can be the
    patient, significant other (such as a family member or spouse), or a
    clinician.  A common scenario where this information is captured is during
    the history taking process during a patient visit or stay.   The medication
    information may come from sources such as the patient's memory, from a
    prescription bottle,  or from a list of medications the patient, clinician
    or other party maintains.
    
    The primary difference between a medication statement and a medication
    administration is that the medication administration has complete
    administration information and is based on actual administration
    information from the person who administered the medication.  A medication
    statement is often, if not always, less specific.  There is no required
    date/time when the medication was administered, in fact we only know that a
    source has reported the patient is taking this medication, where details
    such as time, quantity, or rate or even medication product may be
    incomplete or missing or less precise.  As stated earlier, the medication
    statement information may come from the patient's memory, from a
    prescription bottle or from a list of medications the patient, clinician or
    other party maintains.  Medication administration is more formal and is not
    missing detailed information.
    """
    
    resource_type = "MedicationStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Fulfils plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | completed | entered-in-error | intended | stopped | on-
        hold | unknown | not-taken.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of medication usage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What medication was taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ What medication was taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who is/was taking  the medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter / Episode associated with MedicationStatement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ The date/time or interval when the medication is/was/will be taken.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ The date/time or interval when the medication is/was/will be taken.
        Type `Period` (represented as `dict` in JSON). """
        
        self.dateAsserted = None
        """ When the statement was asserted?.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.informationSource = None
        """ Person or organization that provided the information about the
        taking of this medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.derivedFrom = None
        """ Additional supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Reason for why the medication is being/was taken.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition or observation that supports why the medication is
        being/was taken.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Further information about the statement.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication is/was taken or should be taken.
        List of `Dosage` items (represented as `dict` in JSON). """
        
        super(MedicationStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationStatement, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, medicationstatuscodes.MedicationStatusCodes), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True, None), 
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("context", "context", fhirreference.FHIRReference, False, None, False, None), 
            ("effectiveDateTime", "effectiveDateTime", fhirdatatypes.FHIRDateTime, False, "effective", False, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False, None), 
            ("dateAsserted", "dateAsserted", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("informationSource", "informationSource", fhirreference.FHIRReference, False, None, False, None), 
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("dosage", "dosage", dosage.Dosage, True, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import dosage

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import medicationstatuscodes

from fhirclient.models import period

