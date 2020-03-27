#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RequestGroup)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class RequestGroup(domainresource.DomainResource):
    """ A group of related requests.
    
    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    
    resource_type = "RequestGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `FHIRUri` items (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Fulfills plan, proposal, or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ What's being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the request group is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ When the request group was authored.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.author = None
        """ Device or practitioner that authored the request group.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why the request group is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why the request group is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.action = None
        """ Proposed actions, if any.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        super(RequestGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False, None), 
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, requeststatus.RequestStatus), 
            ("intent", "intent", fhirdatatypes.FHIRCode, False, None, True, requestintent.RequestIntent), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("action", "action", RequestGroupAction, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class RequestGroupAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.
    
    The actions, if any, produced by the evaluation of the artifact.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.prefix = None
        """ User-visible prefix for the action (e.g. 1. or A.).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ User-visible title.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.description = None
        """ Short description of the action.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Code representing the meaning of the action or sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Whether or not the action is applicable.
        List of `RequestGroupActionCondition` items (represented as `dict` in JSON). """
        
        self.relatedAction = None
        """ Relationship to another action.
        List of `RequestGroupActionRelatedAction` items (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ When the action should take place.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.timingAge = None
        """ When the action should take place.
        Type `Age` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingDuration = None
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingRange = None
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.participant = None
        """ Who should perform the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.groupingBehavior = None
        """ visual-group | logical-group | sentence-group.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.selectionBehavior = None
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.requiredBehavior = None
        """ must | could | must-unless-documented.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.precheckBehavior = None
        """ yes | no.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.cardinalityBehavior = None
        """ single | multiple.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.resource = None
        """ The target of the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.action = None
        """ Sub action.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        super(RequestGroupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("prefix", "prefix", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("textEquivalent", "textEquivalent", fhirdatatypes.FHIRString, False, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("code", "code", codeableconcept.CodeableConcept, True, None, False, None), 
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False, None), 
            ("condition", "condition", RequestGroupActionCondition, True, None, False, None), 
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False, None), 
            ("timingDateTime", "timingDateTime", fhirdatatypes.FHIRDateTime, False, "timing", False, None), 
            ("timingAge", "timingAge", age.Age, False, "timing", False, None), 
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False, None), 
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False, None), 
            ("timingRange", "timingRange", range.Range, False, "timing", False, None), 
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False, None), 
            ("participant", "participant", fhirreference.FHIRReference, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("groupingBehavior", "groupingBehavior", fhirdatatypes.FHIRCode, False, None, False, actiongroupingbehavior.ActionGroupingBehavior), 
            ("selectionBehavior", "selectionBehavior", fhirdatatypes.FHIRCode, False, None, False, actionselectionbehavior.ActionSelectionBehavior), 
            ("requiredBehavior", "requiredBehavior", fhirdatatypes.FHIRCode, False, None, False, actionrequiredbehavior.ActionRequiredBehavior), 
            ("precheckBehavior", "precheckBehavior", fhirdatatypes.FHIRCode, False, None, False, actionprecheckbehavior.ActionPrecheckBehavior), 
            ("cardinalityBehavior", "cardinalityBehavior", fhirdatatypes.FHIRCode, False, None, False, actioncardinalitybehavior.ActionCardinalityBehavior), 
            ("resource", "resource", fhirreference.FHIRReference, False, None, False, None), 
            ("action", "action", RequestGroupAction, True, None, False, None), 
        ])
        return js




class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.kind = None
        """ applicability | start | stop.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `Expression` (represented as `dict` in JSON). """
        
        super(RequestGroupActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, True, actionconditionkind.ActionConditionKind), 
            ("expression", "expression", expression.Expression, False, None, False, None), 
        ])
        return js




class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionId = None
        """ What action this is related to.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.relationship = None
        """ before-start | before | before-end | concurrent-with-start |
        concurrent | concurrent-with-end | after-start | after | after-end.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        
        super(RequestGroupActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", fhirdatatypes.FHIRId, False, None, True, None), 
            ("relationship", "relationship", fhirdatatypes.FHIRCode, False, None, True, actionrelationshiptype.ActionRelationshipType), 
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False, None), 
            ("offsetRange", "offsetRange", range.Range, False, "offset", False, None), 
        ])
        return js



from fhirclient.codesystems import actioncardinalitybehavior

from fhirclient.codesystems import actionconditionkind

from fhirclient.codesystems import actiongroupingbehavior

from fhirclient.codesystems import actionprecheckbehavior

from fhirclient.codesystems import actionrelationshiptype

from fhirclient.codesystems import actionrequiredbehavior

from fhirclient.codesystems import actionselectionbehavior

from fhirclient.models import age

from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import duration

from fhirclient.models import expression

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import range

from fhirclient.models import relatedartifact

from fhirclient.codesystems import requestintent

from fhirclient.codesystems import requestpriority

from fhirclient.codesystems import requeststatus

from fhirclient.models import timing

