#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

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
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, False),
            ("disposition", "disposition", fhirdatatypes.FHIRString, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", fhirdatatypes.FHIRCode, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False),
        ])
        return js



import sys
try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']

try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

