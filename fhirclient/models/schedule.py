#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Schedule)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Schedule(domainresource.DomainResource):
    """ A container for slots of time that may be available for booking
    appointments.
    """
    
    resource_type = "Schedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.active = None
        """ Whether this schedule is in active use.
        Type `bool`. """
        
        self.serviceCategory = None
        """ High-level category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ Specific service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Type of specialty needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ Resource(s) that availability information is being provided for.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.planningHorizon = None
        """ Period of time covered by schedule.
        Type `Period` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Comments on availability.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(Schedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("active", "active", bool, False, None, False, None), 
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False, None), 
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, True, None, True, None), 
            ("planningHorizon", "planningHorizon", period.Period, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

