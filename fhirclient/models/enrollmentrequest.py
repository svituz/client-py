#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enroll in coverage.
    
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    
    resource_type = "EnrollmentRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.insurer = None
        """ Target.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.candidate = None
        """ The subject to be enrolled.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False, None), 
            ("provider", "provider", fhirreference.FHIRReference, False, None, False, None), 
            ("candidate", "candidate", fhirreference.FHIRReference, False, None, False, None), 
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

