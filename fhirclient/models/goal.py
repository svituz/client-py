#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Goal)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.
    
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    
    resource_type = "Goal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lifecycleStatus = None
        """ proposed | planned | accepted | active | on-hold | completed |
        cancelled | entered-in-error | rejected.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.achievementStatus = None
        """ in-progress | improving | worsening | no-change | achieved |
        sustaining | not-achieved | no-progress | not-attainable.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. Treatment, dietary, behavioral, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ high-priority | medium-priority | low-priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Code or text describing goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who this goal is intended for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.startDate = None
        """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.startCodeableConcept = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Target outcome for the goal.
        List of `GoalTarget` items (represented as `dict` in JSON). """
        
        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expressedBy = None
        """ Who's responsible for creating Goal?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.addresses = None
        """ Issues addressed by this goal.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the goal.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcomeCode = None
        """ What result was achieved regarding the goal?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ Observation that resulted from goal.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Goal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("lifecycleStatus", "lifecycleStatus", fhirdatatypes.FHIRCode, False, None, True, goallifecyclestatus.GoalLifecycleStatus), 
            ("achievementStatus", "achievementStatus", codeableconcept.CodeableConcept, False, None, False, None), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", codeableconcept.CodeableConcept, False, None, True, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("startDate", "startDate", fhirdatatypes.FHIRDate, False, "start", False, None), 
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False, "start", False, None), 
            ("target", "target", GoalTarget, True, None, False, None), 
            ("statusDate", "statusDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("statusReason", "statusReason", fhirdatatypes.FHIRString, False, None, False, None), 
            ("expressedBy", "expressedBy", fhirreference.FHIRReference, False, None, False, None), 
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("outcomeCode", "outcomeCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class GoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.
    
    Indicates what should be done by when.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.measure = None
        """ The parameter whose value is being tracked.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailQuantity = None
        """ The target value to be achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.detailRange = None
        """ The target value to be achieved.
        Type `Range` (represented as `dict` in JSON). """
        
        self.detailCodeableConcept = None
        """ The target value to be achieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailString = None
        """ The target value to be achieved.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.detailBoolean = None
        """ The target value to be achieved.
        Type `bool`. """
        
        self.detailInteger = None
        """ The target value to be achieved.
        Type `int`. """
        
        self.detailRatio = None
        """ The target value to be achieved.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.dueDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dueDuration = None
        """ Reach goal on or before.
        Type `Duration` (represented as `dict` in JSON). """
        
        super(GoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False, None), 
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False, None), 
            ("detailRange", "detailRange", range.Range, False, "detail", False, None), 
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False, None), 
            ("detailString", "detailString", fhirdatatypes.FHIRString, False, "detail", False, None), 
            ("detailBoolean", "detailBoolean", bool, False, "detail", False, None), 
            ("detailInteger", "detailInteger", int, False, "detail", False, None), 
            ("detailRatio", "detailRatio", ratio.Ratio, False, "detail", False, None), 
            ("dueDate", "dueDate", fhirdatatypes.FHIRDate, False, "due", False, None), 
            ("dueDuration", "dueDuration", duration.Duration, False, "due", False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import duration

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.codesystems import goallifecyclestatus

from fhirclient.models import identifier

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.models import ratio

