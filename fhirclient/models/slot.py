#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Slot)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    
    resource_type = "Slot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ A broad categorization of the service that is to be performed
        during this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.appointmentType = None
        """ The style of appointment or patient that may be booked in the slot
        (not service type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ busy | free | busy-unavailable | busy-tentative | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.start = None
        """ Date/Time that the slot is to begin.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.end = None
        """ Date/Time that the slot is to conclude.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.overbooked = None
        """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """
        
        self.comment = None
        """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(Slot, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False, None), 
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False, None), 
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False, None), 
            ("schedule", "schedule", fhirreference.FHIRReference, False, None, True, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, slotstatus.SlotStatus), 
            ("start", "start", fhirdatatypes.FHIRInstant, False, None, True, None), 
            ("end", "end", fhirdatatypes.FHIRInstant, False, None, True, None), 
            ("overbooked", "overbooked", bool, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import slotstatus

