#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PractitionerRole)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class PractitionerRole(domainresource.DomainResource):
    """ Roles/organizations the practitioner is associated with.
    
    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    
    resource_type = "PractitionerRole"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifiers that are specific to a role/location.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether this practitioner role record is in active use.
        Type `bool`. """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ Practitioner that is able to provide the defined services for the
        organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization where the roles are available.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.code = None
        """ Roles which this practitioner may perform.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details that are specific to the role/location/service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `PractitionerRoleAvailableTime` items (represented as `dict` in JSON). """
        
        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `PractitionerRoleNotAvailable` items (represented as `dict` in JSON). """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        practitioner with this role.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(PractitionerRole, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("practitioner", "practitioner", fhirreference.FHIRReference, False, None, False, None), 
            ("organization", "organization", fhirreference.FHIRReference, False, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, True, None, False, None), 
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, True, None, False, None), 
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, True, None, False, None), 
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, True, None, False, None), 
            ("availabilityExceptions", "availabilityExceptions", fhirdatatypes.FHIRString, False, None, False, None), 
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.allDay = None
        """ Always available? e.g. 24 hour service.
        Type `bool`. """
        
        self.availableStartTime = None
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.availableEndTime = None
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        super(PractitionerRoleAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("daysOfWeek", "daysOfWeek", fhirdatatypes.FHIRCode, True, None, False, daysofweek.DaysOfWeek), 
            ("allDay", "allDay", bool, False, None, False, None), 
            ("availableStartTime", "availableStartTime", fhirdatatypes.FHIRTime, False, None, False, None), 
            ("availableEndTime", "availableEndTime", fhirdatatypes.FHIRTime, False, None, False, None), 
        ])
        return js




class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Reason presented to the user explaining why time not available.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.during = None
        """ Service not available from this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerRoleNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, True, None), 
            ("during", "during", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.codesystems import daysofweek

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

