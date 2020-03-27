#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HealthcareService)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    
    resource_type = "HealthcareService"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether this HealthcareService record is in active use.
        Type `bool`. """
        
        self.providedBy = None
        """ Organization that provides this service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        """ Broad category of service being performed or delivered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of service that may be delivered or performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specialties handled by the HealthcareService.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Location(s) where service may be provided.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Description of service as presented to a consumer while searching.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.comment = None
        """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.extraDetails = None
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.photo = None
        """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.coverageArea = None
        """ Location(s) service is intended for/available to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.serviceProvisionCode = None
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.eligibility = None
        """ Specific eligibility requirements required to use the service.
        List of `HealthcareServiceEligibility` items (represented as `dict` in JSON). """
        
        self.program = None
        """ Programs that this service is applicable to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.communication = None
        """ The language that this service is offered in.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.referralMethod = None
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.appointmentRequired = None
        """ If an appointment is required for access to this service.
        Type `bool`. """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.endpoint = None
        """ Technical endpoints providing access to electronic services
        operated for the healthcare service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, True, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("extraDetails", "extraDetails", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("photo", "photo", attachment.Attachment, False, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False, None), 
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False, None), 
            ("program", "program", codeableconcept.CodeableConcept, True, None, False, None), 
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False, None), 
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False, None), 
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False, None), 
            ("appointmentRequired", "appointmentRequired", bool, False, None, False, None), 
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False, None), 
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False, None), 
            ("availabilityExceptions", "availabilityExceptions", fhirdatatypes.FHIRString, False, None, False, None), 
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
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
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("daysOfWeek", "daysOfWeek", fhirdatatypes.FHIRCode, True, None, False, daysofweek.DaysOfWeek), 
            ("allDay", "allDay", bool, False, None, False, None), 
            ("availableStartTime", "availableStartTime", fhirdatatypes.FHIRTime, False, None, False, None), 
            ("availableEndTime", "availableEndTime", fhirdatatypes.FHIRTime, False, None, False, None), 
        ])
        return js




class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.
    
    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded value for the eligibility.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Describes the eligibility conditions for the service.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        super(HealthcareServiceEligibility, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
        ])
        return js




class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
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
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, True, None), 
            ("during", "during", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.codesystems import daysofweek

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

