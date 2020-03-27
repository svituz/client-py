#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Provenance)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Provenance(domainresource.DomainResource):
    """ Who, What, When for a set of resources.
    
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g. Document
    Completion - has the artifact been legally authenticated), all of which may
    impact security, privacy, and trust policies.
    """
    
    resource_type = "Provenance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.target = None
        """ Target Reference(s) (usually version specific).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.occurredPeriod = None
        """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurredDateTime = None
        """ When the activity occurred.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recorded = None
        """ When the activity was recorded / updated.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.policy = None
        """ Policy or plan the activity was defined by.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.location = None
        """ Where the activity occurred, if relevant.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason the activity is occurring.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.activity = None
        """ Activity that occurred.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.agent = None
        """ Actor involved.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        """ An entity used in this activity.
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """
        
        self.signature = None
        """ Signature on target.
        List of `Signature` items (represented as `dict` in JSON). """
        
        super(Provenance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("target", "target", fhirreference.FHIRReference, True, None, True, None), 
            ("occurredPeriod", "occurredPeriod", period.Period, False, "occurred", False, None), 
            ("occurredDateTime", "occurredDateTime", fhirdatatypes.FHIRDateTime, False, "occurred", False, None), 
            ("recorded", "recorded", fhirdatatypes.FHIRInstant, False, None, True, None), 
            ("policy", "policy", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("activity", "activity", codeableconcept.CodeableConcept, False, None, False, None), 
            ("agent", "agent", ProvenanceAgent, True, None, True, None), 
            ("entity", "entity", ProvenanceEntity, True, None, False, None), 
            ("signature", "signature", signature.Signature, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ProvenanceAgent(backboneelement.BackboneElement):
    """ Actor involved.
    
    An actor taking a role in an activity  for which it can be assigned some
    degree of responsibility for the activity taking place.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ How the agent participated.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.role = None
        """ What the agents role was.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.who = None
        """ Who participated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Who the agent is representing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProvenanceAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("role", "role", codeableconcept.CodeableConcept, True, None, False, None), 
            ("who", "who", fhirreference.FHIRReference, False, None, True, None), 
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js




class ProvenanceEntity(backboneelement.BackboneElement):
    """ An entity used in this activity.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ derivation | revision | quotation | source | removal.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.what = None
        """ Identity of entity.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.agent = None
        """ Entity is attributed to this agent.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        super(ProvenanceEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("role", "role", fhirdatatypes.FHIRCode, False, None, True, provenanceentityrole.ProvenanceEntityRole), 
            ("what", "what", fhirreference.FHIRReference, False, None, True, None), 
            ("agent", "agent", ProvenanceAgent, True, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import period

from fhirclient.codesystems import provenanceentityrole

from fhirclient.models import signature

