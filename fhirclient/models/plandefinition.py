#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PlanDefinition)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class PlanDefinition(domainresource.DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient or context.
    
    This resource allows for the definition of various types of plans as a
    sharable, consumable, and executable artifact. The resource is general
    enough to support the description of a broad range of clinical artifacts
    such as clinical decision support rules, order sets and protocols.
    """
    
    resource_type = "PlanDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this plan definition, represented as a URI
        (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the plan definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the plan definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this plan definition (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this plan definition (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the plan definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.type = None
        """ order-set | clinical-protocol | eca-rule | workflow-definition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.subjectCodeableConcept = None
        """ Type of individual the plan definition is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ Type of individual the plan definition is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Natural language description of the plan definition.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for plan definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ Why this plan definition is defined.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.usage = None
        """ Describes the clinical usage of the plan.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the plan definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the plan definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the plan definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ E.g. Education, Treatment, Assessment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.relatedArtifact = None
        """ Additional documentation, citations.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.library = None
        """ Logic used by the plan definition.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.goal = None
        """ What the plan is trying to accomplish.
        List of `PlanDefinitionGoal` items (represented as `dict` in JSON). """
        
        self.action = None
        """ Action defined by the plan.
        List of `PlanDefinitionAction` items (represented as `dict` in JSON). """
        
        super(PlanDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("version", "version", fhirdatatypes.FHIRString, False, None, False, None), 
            ("name", "name", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, publicationstatus.PublicationStatus), 
            ("experimental", "experimental", bool, False, None, False, None), 
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False, None), 
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False, None), 
            ("contact", "contact", contactdetail.ContactDetail, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False, None), 
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False, None), 
            ("purpose", "purpose", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("usage", "usage", fhirdatatypes.FHIRString, False, None, False, None), 
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("approvalDate", "approvalDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("lastReviewDate", "lastReviewDate", fhirdatatypes.FHIRDate, False, None, False, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False, None), 
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False, None), 
            ("author", "author", contactdetail.ContactDetail, True, None, False, None), 
            ("editor", "editor", contactdetail.ContactDetail, True, None, False, None), 
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False, None), 
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False, None), 
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False, None), 
            ("library", "library", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("goal", "goal", PlanDefinitionGoal, True, None, False, None), 
            ("action", "action", PlanDefinitionAction, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class PlanDefinitionAction(backboneelement.BackboneElement):
    """ Action defined by the plan.
    
    An action or group of actions to be taken as part of the plan.
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
        """ Brief description of the action.
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
        
        self.reason = None
        """ Why the action should be performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.goalId = None
        """ What goals this action supports.
        List of `FHIRId` items (represented as `str` in JSON). """
        
        self.subjectCodeableConcept = None
        """ Type of individual the action is focused on.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ Type of individual the action is focused on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.trigger = None
        """ When the action should be triggered.
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Whether or not the action is applicable.
        List of `PlanDefinitionActionCondition` items (represented as `dict` in JSON). """
        
        self.input = None
        """ Input data requirements.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.output = None
        """ Output data definition.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.relatedAction = None
        """ Relationship to another action.
        List of `PlanDefinitionActionRelatedAction` items (represented as `dict` in JSON). """
        
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
        """ Who should participate in the action.
        List of `PlanDefinitionActionParticipant` items (represented as `dict` in JSON). """
        
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
        
        self.definitionCanonical = None
        """ Description of the activity to be performed.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.definitionUri = None
        """ Description of the activity to be performed.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.transform = None
        """ Transform to apply the template.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.dynamicValue = None
        """ Dynamic aspects of the definition.
        List of `PlanDefinitionActionDynamicValue` items (represented as `dict` in JSON). """
        
        self.action = None
        """ A sub-action.
        List of `PlanDefinitionAction` items (represented as `dict` in JSON). """
        
        super(PlanDefinitionAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionAction, self).elementProperties()
        js.extend([
            ("prefix", "prefix", fhirdatatypes.FHIRString, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("textEquivalent", "textEquivalent", fhirdatatypes.FHIRString, False, None, False, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("code", "code", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False, None), 
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False, None), 
            ("goalId", "goalId", fhirdatatypes.FHIRId, True, None, False, None), 
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False, None), 
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False, None), 
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False, None), 
            ("condition", "condition", PlanDefinitionActionCondition, True, None, False, None), 
            ("input", "input", datarequirement.DataRequirement, True, None, False, None), 
            ("output", "output", datarequirement.DataRequirement, True, None, False, None), 
            ("relatedAction", "relatedAction", PlanDefinitionActionRelatedAction, True, None, False, None), 
            ("timingDateTime", "timingDateTime", fhirdatatypes.FHIRDateTime, False, "timing", False, None), 
            ("timingAge", "timingAge", age.Age, False, "timing", False, None), 
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False, None), 
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False, None), 
            ("timingRange", "timingRange", range.Range, False, "timing", False, None), 
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False, None), 
            ("participant", "participant", PlanDefinitionActionParticipant, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("groupingBehavior", "groupingBehavior", fhirdatatypes.FHIRCode, False, None, False, actiongroupingbehavior.ActionGroupingBehavior), 
            ("selectionBehavior", "selectionBehavior", fhirdatatypes.FHIRCode, False, None, False, actionselectionbehavior.ActionSelectionBehavior), 
            ("requiredBehavior", "requiredBehavior", fhirdatatypes.FHIRCode, False, None, False, actionrequiredbehavior.ActionRequiredBehavior), 
            ("precheckBehavior", "precheckBehavior", fhirdatatypes.FHIRCode, False, None, False, actionprecheckbehavior.ActionPrecheckBehavior), 
            ("cardinalityBehavior", "cardinalityBehavior", fhirdatatypes.FHIRCode, False, None, False, actioncardinalitybehavior.ActionCardinalityBehavior), 
            ("definitionCanonical", "definitionCanonical", fhirdatatypes.FHIRCanonical, False, "definition", False, None), 
            ("definitionUri", "definitionUri", fhirdatatypes.FHIRUri, False, "definition", False, None), 
            ("transform", "transform", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDynamicValue, True, None, False, None), 
            ("action", "action", PlanDefinitionAction, True, None, False, None), 
        ])
        return js




class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    
    An expression that describes applicability criteria or start/stop
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
        
        super(PlanDefinitionActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionCondition, self).elementProperties()
        js.extend([
            ("kind", "kind", fhirdatatypes.FHIRCode, False, None, True, actionconditionkind.ActionConditionKind), 
            ("expression", "expression", expression.Expression, False, None, False, None), 
        ])
        return js




class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ The path to the element to be set dynamically.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expression = None
        """ An expression that provides the dynamic value for the customization.
        Type `Expression` (represented as `dict` in JSON). """
        
        super(PlanDefinitionActionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDynamicValue, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, False, None), 
            ("expression", "expression", expression.Expression, False, None, False, None), 
        ])
        return js




class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.
    
    Indicates who should participate in performing the action described.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ patient | practitioner | related-person | device.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.role = None
        """ E.g. Nurse, Surgeon, Parent.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PlanDefinitionActionParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionParticipant, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, actionparticipanttype.ActionParticipantType), 
            ("role", "role", codeableconcept.CodeableConcept, False, None, False, None), 
        ])
        return js




class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
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
        """ What action is this related to.
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
        
        super(PlanDefinitionActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", fhirdatatypes.FHIRId, False, None, True, None), 
            ("relationship", "relationship", fhirdatatypes.FHIRCode, False, None, True, actionrelationshiptype.ActionRelationshipType), 
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False, None), 
            ("offsetRange", "offsetRange", range.Range, False, "offset", False, None), 
        ])
        return js




class PlanDefinitionGoal(backboneelement.BackboneElement):
    """ What the plan is trying to accomplish.
    
    Goals that describe what the activities within the plan are intended to
    achieve. For example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ E.g. Treatment, dietary, behavioral.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Code or text describing the goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priority = None
        """ high-priority | medium-priority | low-priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.addresses = None
        """ What does the goal address.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.documentation = None
        """ Supporting documentation for the goal.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.target = None
        """ Target outcome for the goal.
        List of `PlanDefinitionGoalTarget` items (represented as `dict` in JSON). """
        
        super(PlanDefinitionGoal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionGoal, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", codeableconcept.CodeableConcept, False, None, True, None), 
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False, None), 
            ("start", "start", codeableconcept.CodeableConcept, False, None, False, None), 
            ("addresses", "addresses", codeableconcept.CodeableConcept, True, None, False, None), 
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False, None), 
            ("target", "target", PlanDefinitionGoalTarget, True, None, False, None), 
        ])
        return js




class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.
    
    Indicates what should be done and within what timeframe.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.measure = None
        """ The parameter whose value is to be tracked.
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
        
        self.due = None
        """ Reach goal within.
        Type `Duration` (represented as `dict` in JSON). """
        
        super(PlanDefinitionGoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionGoalTarget, self).elementProperties()
        js.extend([
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False, None), 
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False, None), 
            ("detailRange", "detailRange", range.Range, False, "detail", False, None), 
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False, None), 
            ("due", "due", duration.Duration, False, None, False, None), 
        ])
        return js



from fhirclient.codesystems import actioncardinalitybehavior

from fhirclient.codesystems import actionconditionkind

from fhirclient.codesystems import actiongroupingbehavior

from fhirclient.codesystems import actionparticipanttype

from fhirclient.codesystems import actionprecheckbehavior

from fhirclient.codesystems import actionrelationshiptype

from fhirclient.codesystems import actionrequiredbehavior

from fhirclient.codesystems import actionselectionbehavior

from fhirclient.models import age

from fhirclient.models import codeableconcept

from fhirclient.models import contactdetail

from fhirclient.models import datarequirement

from fhirclient.models import duration

from fhirclient.models import expression

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.codesystems import publicationstatus

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.models import relatedartifact

from fhirclient.codesystems import requestpriority

from fhirclient.models import timing

from fhirclient.models import triggerdefinition

from fhirclient.models import usagecontext

