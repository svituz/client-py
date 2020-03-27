#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_type = "AppointmentResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.appointment = None
        """ Appointment this response relates to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.start = None
        """ Time from appointment, or requested new start time.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.end = None
        """ Time from appointment, or requested new end time.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.participantType = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Person, Location, HealthcareService, or Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.participantStatus = None
        """ accepted | declined | tentative | needs-action.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.comment = None
        """ Additional comments.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("appointment", "appointment", fhirreference.FHIRReference, False, None, True, None), 
            ("start", "start", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("end", "end", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("participantType", "participantType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, False, None), 
            ("participantStatus", "participantStatus", fhirdatatypes.FHIRCode, False, None, True, participationstatus.ParticipationStatus), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import participationstatus

