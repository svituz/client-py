#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CarePlan)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.
    
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    
    resource_type = "CarePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Fulfills CarePlan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        """ CarePlan replaced by this CarePlan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced CarePlan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.intent = None
        """ proposal | plan | order | option.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Human-friendly name for the care plan.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Summary of nature of plan.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subject = None
        """ Who the care plan is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.created = None
        """ Date record was first recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.author = None
        """ Who is the designated responsible party.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contributor = None
        """ Who provided the content of the care plan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ Who's involved in plan?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.addresses = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingInfo = None
        """ Information considered as part of plan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.goal = None
        """ Desired outcome of plan.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the plan.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(CarePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, requeststatus.RequestStatus), 
            ("intent", "intent", fhirdatatypes.FHIRCode, False, None, True, requestintent.RequestIntent), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("created", "created", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False, None), 
            ("careTeam", "careTeam", fhirreference.FHIRReference, True, None, False, None), 
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False, None), 
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False, None), 
            ("goal", "goal", fhirreference.FHIRReference, True, None, False, None), 
            ("activity", "activity", CarePlanActivity, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.
    
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcomeCodeableConcept = None
        """ Results of the activity.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ Appointment, Encounter, Procedure, etc..
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.progress = None
        """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.detail = None
        """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """
        
        super(CarePlanActivity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("outcomeCodeableConcept", "outcomeCodeableConcept", codeableconcept.CodeableConcept, True, None, False, None), 
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False, None), 
            ("progress", "progress", annotation.Annotation, True, None, False, None), 
            ("reference", "reference", fhirreference.FHIRReference, False, None, False, None), 
            ("detail", "detail", CarePlanActivityDetail, False, None, False, None), 
        ])
        return js




class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.
    
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.kind = None
        """ Appointment | CommunicationRequest | DeviceRequest |
        MedicationRequest | NutritionOrder | Task | ServiceRequest |
        VisionPrescription.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why activity should be done or why activity was prohibited.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why activity is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled | stopped | unknown | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doNotPerform = None
        """ If true, activity is prohibiting action.
        Type `bool`. """
        
        self.scheduledTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.scheduledPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledString = None
        """ When activity is to occur.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        """ What is to be administered/supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.dailyAmount = None
        """ How to consume/day?.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Extra info describing activity to perform.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, False, resourcetype.ResourceType), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("goal", "goal", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, careplanactivitystatus.CarePlanActivityStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("doNotPerform", "doNotPerform", bool, False, None, False, None), 
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False, None), 
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False, None), 
            ("scheduledString", "scheduledString", fhirdatatypes.FHIRString, False, "scheduled", False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, True, None, False, None), 
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False, None), 
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False, None), 
            ("dailyAmount", "dailyAmount", quantity.Quantity, False, None, False, None), 
            ("quantity", "quantity", quantity.Quantity, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.codesystems import careplanactivitystatus

from fhirclient.models import codeableconcept

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.codesystems import requestintent

from fhirclient.codesystems import requeststatus

from fhirclient.codesystems import resourcetype

from fhirclient.models import timing

