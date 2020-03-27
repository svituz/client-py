#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Appointment)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    
    resource_type = "Appointment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow | entered-in-error | checked-in | waitlist.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.cancelationReason = None
        """ The coded reason for the appointment being cancelled.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ A broad categorization of the service that is to be performed
        during this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ The specific service that is to be performed during this
        appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.appointmentType = None
        """ The style of appointment or patient that has been booked in the
        slot (not service type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Coded reason this appointment is scheduled.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason the appointment is to take place (resource).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ Used to make informed decisions if needing to re-prioritize.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.description = None
        """ Shown on a subject line in a meeting request, or appointment list.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.supportingInformation = None
        """ Additional information to support the appointment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.start = None
        """ When appointment is to take place.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.end = None
        """ When appointment is to conclude.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.minutesDuration = None
        """ Can be less than start/end (e.g. estimate).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.slot = None
        """ The slots that this appointment is filling.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.created = None
        """ The date that this appointment was initially created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.comment = None
        """ Additional comments.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.patientInstruction = None
        """ Detailed information and instructions for the patient.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ The service request this appointment is allocated to assess.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ Participants involved in appointment.
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """
        
        self.requestedPeriod = None
        """ Potential date/time interval(s) requested to allocate the
        appointment within.
        List of `Period` items (represented as `dict` in JSON). """
        
        super(Appointment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, appointmentstatus.AppointmentStatus), 
            ("cancelationReason", "cancelationReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False, None), 
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False, None), 
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False, None), 
            ("start", "start", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("end", "end", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("minutesDuration", "minutesDuration", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("slot", "slot", fhirreference.FHIRReference, True, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("patientInstruction", "patientInstruction", fhirdatatypes.FHIRString, False, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("participant", "participant", AppointmentParticipant, True, None, True, None), 
            ("requestedPeriod", "requestedPeriod", period.Period, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.
    
    List of participants involved in the appointment.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Person, Location/HealthcareService or Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.required = None
        """ required | optional | information-only.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.status = None
        """ accepted | declined | tentative | needs-action.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.period = None
        """ Participation period of the actor.
        Type `Period` (represented as `dict` in JSON). """
        
        super(AppointmentParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, False, None), 
            ("required", "required", fhirdatatypes.FHIRCode, False, None, False, participantrequired.ParticipantRequired), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, participationstatus.ParticipationStatus), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import appointmentstatus

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import participantrequired

from fhirclient.codesystems import participationstatus

from fhirclient.models import period

