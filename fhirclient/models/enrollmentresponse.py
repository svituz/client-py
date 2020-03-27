#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class EnrollmentResponse(domainresource.DomainResource):
    """ EnrollmentResponse resource.
    
    This resource provides enrollment and plan details from the processing of
    an EnrollmentRequest resource.
    """
    
    resource_type = "EnrollmentResponse"
    
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
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, financialresourcestatuscodes.FinancialResourceStatusCodes), 
            ("request", "request", fhirreference.FHIRReference, False, None, False, None), 
            ("outcome", "outcome", fhirdatatypes.FHIRCode, False, None, False, claimprocessingcodes.ClaimProcessingCodes), 
            ("disposition", "disposition", fhirdatatypes.FHIRString, False, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("organization", "organization", fhirreference.FHIRReference, False, None, False, None), 
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import claimprocessingcodes

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import financialresourcestatuscodes

from fhirclient.models import identifier

