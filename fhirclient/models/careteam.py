#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CareTeam)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class CareTeam(domainresource.DomainResource):
    """ Planned participants in the coordination and delivery of care for a patient
    or group.
    
    The Care Team includes all the people and organizations who plan to
    participate in the coordination and delivery of care for a patient.
    """
    
    resource_type = "CareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this team.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | active | suspended | inactive | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ Type of team.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Name of the team, such as crisis assessment team.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subject = None
        """ Who care team is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period team covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.participant = None
        """ Members of the team.
        List of `CareTeamParticipant` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why the care team exists.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why the care team exists.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization responsible for the care team.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the care team (that applies to all members).
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the CareTeam.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(CareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, False, careteamstatus.CareTeamStatus), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("participant", "participant", CareTeamParticipant, True, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, True, None, False, None), 
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CareTeamParticipant(backboneelement.BackboneElement):
    """ Members of the team.
    
    Identifies all people and organizations who are expected to be involved in
    the care team.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ Type of involvement.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization of the practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period of participant.
        Type `Period` (represented as `dict` in JSON). """
        
        super(CareTeamParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, True, None, False, None), 
            ("member", "member", fhirreference.FHIRReference, False, None, False, None), 
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.codesystems import careteamstatus

from fhirclient.models import codeableconcept

from fhirclient.models import contactpoint

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

