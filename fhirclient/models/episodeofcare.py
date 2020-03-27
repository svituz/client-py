#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EpisodeOfCare)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class EpisodeOfCare(domainresource.DomainResource):
    """ An association of a Patient with an Organization and  Healthcare
    Provider(s) for a period of time that the Organization assumes some level
    of responsibility.
    
    An association between a patient and an organization / healthcare
    provider(s) during which time encounters may occur. The managing
    organization assumes a level of responsibility for the patient during this
    time.
    """
    
    resource_type = "EpisodeOfCare"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business Identifier(s) relevant for this EpisodeOfCare.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled |
        entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusHistory = None
        """ Past list of status codes (the current status may be included to
        cover the start date of the status).
        List of `EpisodeOfCareStatusHistory` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type/class  - e.g. specialist referral, disease management.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.diagnosis = None
        """ The list of diagnosis relevant to this episode of care.
        List of `EpisodeOfCareDiagnosis` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient who is the focus of this episode of care.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that assumes care.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Interval during responsibility is assumed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.referralRequest = None
        """ Originating Referral Request(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careManager = None
        """ Care manager/care coordinator for the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.team = None
        """ Other practitioners facilitating this episode of care.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.account = None
        """ The set of accounts that may be used for billing for this
        EpisodeOfCare.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(EpisodeOfCare, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCare, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, episodeofcarestatus.EpisodeOfCareStatus), 
            ("statusHistory", "statusHistory", EpisodeOfCareStatusHistory, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, True, None, False, None), 
            ("diagnosis", "diagnosis", EpisodeOfCareDiagnosis, True, None, False, None), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, True, None), 
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("referralRequest", "referralRequest", fhirreference.FHIRReference, True, None, False, None), 
            ("careManager", "careManager", fhirreference.FHIRReference, False, None, False, None), 
            ("team", "team", fhirreference.FHIRReference, True, None, False, None), 
            ("account", "account", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this episode of care.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ Conditions/problems/diagnoses this episode of care is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ Role that this diagnosis has within the episode of care (e.g.
        admission, billing, discharge …).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rank = None
        """ Ranking of the diagnosis (for each role type).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        super(EpisodeOfCareDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareDiagnosis, self).elementProperties()
        js.extend([
            ("condition", "condition", fhirreference.FHIRReference, False, None, True, None), 
            ("role", "role", codeableconcept.CodeableConcept, False, None, False, None), 
            ("rank", "rank", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
        ])
        return js




class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    """ Past list of status codes (the current status may be included to cover the
    start date of the status).
    
    The history of statuses that the EpisodeOfCare has been through (without
    requiring processing the history of the resource).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.status = None
        """ planned | waitlist | active | onhold | finished | cancelled |
        entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.period = None
        """ Duration the EpisodeOfCare was in the specified status.
        Type `Period` (represented as `dict` in JSON). """
        
        super(EpisodeOfCareStatusHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EpisodeOfCareStatusHistory, self).elementProperties()
        js.extend([
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, episodeofcarestatus.EpisodeOfCareStatus), 
            ("period", "period", period.Period, False, None, True, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import episodeofcarestatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

