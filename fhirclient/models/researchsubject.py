#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ResearchSubject)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ResearchSubject(domainresource.DomainResource):
    """ Physical entity which is the primary unit of interest in the study.
    
    A physical entity which is the primary unit of operational and/or
    administrative interest in a study.
    """
    
    resource_type = "ResearchSubject"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier for research subject in a study.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ candidate | eligible | follow-up | ineligible | not-registered |
        off-study | on-study | on-study-intervention | on-study-observation
        | pending-on-study | potential-candidate | screening | withdrawn.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.period = None
        """ Start and end of participation.
        Type `Period` (represented as `dict` in JSON). """
        
        self.study = None
        """ Study subject is part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.individual = None
        """ Who is part of study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.assignedArm = None
        """ What path should be followed.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.actualArm = None
        """ What path was followed.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.consent = None
        """ Agreement to participate in study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ResearchSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, researchsubjectstatus.ResearchSubjectStatus), 
            ("period", "period", period.Period, False, None, False, None), 
            ("study", "study", fhirreference.FHIRReference, False, None, True, None), 
            ("individual", "individual", fhirreference.FHIRReference, False, None, True, None), 
            ("assignedArm", "assignedArm", fhirdatatypes.FHIRString, False, None, False, None), 
            ("actualArm", "actualArm", fhirdatatypes.FHIRString, False, None, False, None), 
            ("consent", "consent", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import researchsubjectstatus

