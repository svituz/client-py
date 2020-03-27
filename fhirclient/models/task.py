#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Task)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Task(domainresource.DomainResource):
    """ A task to be performed.
    """
    
    resource_type = "Task"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Task Instance Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ Formal definition of task.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.instantiatesUri = None
        """ Formal definition of task.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled by this task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Requisition or grouper id.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Composite task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | requested | received | accepted | +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.businessStatus = None
        """ E.g. "Specimen collected", "IV prepped".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.intent = None
        """ unknown | proposal | plan | order | original-order | reflex-order |
        filler-order | instance-order | option.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Human-readable explanation of task.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.focus = None
        """ What task is acting on.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.for_fhir = None
        """ Beneficiary of the Task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Healthcare event during which this task originated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.executionPeriod = None
        """ Start and end time of execution.
        Type `Period` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ Task Creation Date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.lastModified = None
        """ Task Last Modified Date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.requester = None
        """ Who is asking for task to be done.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ Requested performer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ Responsible individual.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where task occurs.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why task is needed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why task is needed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the task.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ Key events in history of the Task.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.restriction = None
        """ Constraints on fulfillment tasks.
        Type `TaskRestriction` (represented as `dict` in JSON). """
        
        self.input = None
        """ Information used to perform task.
        List of `TaskInput` items (represented as `dict` in JSON). """
        
        self.output = None
        """ Information produced as part of task.
        List of `TaskOutput` items (represented as `dict` in JSON). """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, False, None, False, None), 
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, taskstatus.TaskStatus), 
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False, None), 
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False, None), 
            ("intent", "intent", fhirdatatypes.FHIRCode, False, None, True, None), 
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False, requestpriority.RequestPriority), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("focus", "focus", fhirreference.FHIRReference, False, None, False, None), 
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("executionPeriod", "executionPeriod", period.Period, False, None, False, None), 
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("lastModified", "lastModified", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("requester", "requester", fhirreference.FHIRReference, False, None, False, None), 
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False, None), 
            ("owner", "owner", fhirreference.FHIRReference, False, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False, None), 
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False, None), 
            ("restriction", "restriction", TaskRestriction, False, None, False, None), 
            ("input", "input", TaskInput, True, None, False, None), 
            ("output", "output", TaskOutput, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ Information used to perform task.
    
    Additional information that may be needed in the execution of the task.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Label for the input.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Content to use in performing the task.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ Content to use in performing the task.
        Type `bool`. """
        
        self.valueCanonical = None
        """ Content to use in performing the task.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.valueCode = None
        """ Content to use in performing the task.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueDate = None
        """ Content to use in performing the task.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Content to use in performing the task.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Content to use in performing the task.
        Type `float`. """
        
        self.valueId = None
        """ Content to use in performing the task.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.valueInstant = None
        """ Content to use in performing the task.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Content to use in performing the task.
        Type `int`. """
        
        self.valueMarkdown = None
        """ Content to use in performing the task.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.valueOid = None
        """ Content to use in performing the task.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.valuePositiveInt = None
        """ Content to use in performing the task.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.valueString = None
        """ Content to use in performing the task.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Content to use in performing the task.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUnsignedInt = None
        """ Content to use in performing the task.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.valueUri = None
        """ Content to use in performing the task.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueUrl = None
        """ Content to use in performing the task.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.valueUuid = None
        """ Content to use in performing the task.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.valueAddress = None
        """ Content to use in performing the task.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ Content to use in performing the task.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ Content to use in performing the task.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Content to use in performing the task.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Content to use in performing the task.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Content to use in performing the task.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Content to use in performing the task.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ Content to use in performing the task.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDistance = None
        """ Content to use in performing the task.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ Content to use in performing the task.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ Content to use in performing the task.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Content to use in performing the task.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ Content to use in performing the task.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ Content to use in performing the task.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Content to use in performing the task.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Content to use in performing the task.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Content to use in performing the task.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Content to use in performing the task.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Content to use in performing the task.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Content to use in performing the task.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueTiming = None
        """ Content to use in performing the task.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ Content to use in performing the task.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ Content to use in performing the task.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ Content to use in performing the task.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ Content to use in performing the task.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueParameterDefinition = None
        """ Content to use in performing the task.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ Content to use in performing the task.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ Content to use in performing the task.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUsageContext = None
        """ Content to use in performing the task.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ Content to use in performing the task.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueMeta = None
        """ Content to use in performing the task.
        Type `Meta` (represented as `dict` in JSON). """
        
        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("valueBase64Binary", "valueBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "value", True, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", True, None), 
            ("valueCanonical", "valueCanonical", fhirdatatypes.FHIRCanonical, False, "value", True, None), 
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", True, None), 
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", True, None), 
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", True, None), 
            ("valueDecimal", "valueDecimal", float, False, "value", True, None), 
            ("valueId", "valueId", fhirdatatypes.FHIRId, False, "value", True, None), 
            ("valueInstant", "valueInstant", fhirdatatypes.FHIRInstant, False, "value", True, None), 
            ("valueInteger", "valueInteger", int, False, "value", True, None), 
            ("valueMarkdown", "valueMarkdown", fhirdatatypes.FHIRMarkdown, False, "value", True, None), 
            ("valueOid", "valueOid", fhirdatatypes.FHIROid, False, "value", True, None), 
            ("valuePositiveInt", "valuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "value", True, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True, None), 
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", True, None), 
            ("valueUnsignedInt", "valueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "value", True, None), 
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", True, None), 
            ("valueUrl", "valueUrl", fhirdatatypes.FHIRUrl, False, "value", True, None), 
            ("valueUuid", "valueUuid", fhirdatatypes.FHIRUuid, False, "value", True, None), 
            ("valueAddress", "valueAddress", address.Address, False, "value", True, None), 
            ("valueAge", "valueAge", age.Age, False, "value", True, None), 
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True, None), 
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True, None), 
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True, None), 
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True, None), 
            ("valueCount", "valueCount", count.Count, False, "value", True, None), 
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True, None), 
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True, None), 
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True, None), 
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True, None), 
            ("valueMoney", "valueMoney", money.Money, False, "value", True, None), 
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True, None), 
            ("valueRange", "valueRange", range.Range, False, "value", True, None), 
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True, None), 
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True, None), 
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True, None), 
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True, None), 
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True, None), 
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True, None), 
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True, None), 
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True, None), 
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True, None), 
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True, None), 
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True, None), 
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True, None), 
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True, None), 
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True, None), 
        ])
        return js




class TaskOutput(backboneelement.BackboneElement):
    """ Information produced as part of task.
    
    Outputs produced by the Task.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Label for output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Result of output.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ Result of output.
        Type `bool`. """
        
        self.valueCanonical = None
        """ Result of output.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.valueCode = None
        """ Result of output.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueDate = None
        """ Result of output.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Result of output.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Result of output.
        Type `float`. """
        
        self.valueId = None
        """ Result of output.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.valueInstant = None
        """ Result of output.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Result of output.
        Type `int`. """
        
        self.valueMarkdown = None
        """ Result of output.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.valueOid = None
        """ Result of output.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.valuePositiveInt = None
        """ Result of output.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.valueString = None
        """ Result of output.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Result of output.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUnsignedInt = None
        """ Result of output.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.valueUri = None
        """ Result of output.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueUrl = None
        """ Result of output.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.valueUuid = None
        """ Result of output.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.valueAddress = None
        """ Result of output.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ Result of output.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ Result of output.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Result of output.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Result of output.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Result of output.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Result of output.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ Result of output.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDistance = None
        """ Result of output.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ Result of output.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ Result of output.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Result of output.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ Result of output.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ Result of output.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Result of output.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Result of output.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Result of output.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Result of output.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Result of output.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Result of output.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueTiming = None
        """ Result of output.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ Result of output.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ Result of output.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ Result of output.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ Result of output.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueParameterDefinition = None
        """ Result of output.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ Result of output.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ Result of output.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUsageContext = None
        """ Result of output.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ Result of output.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueMeta = None
        """ Result of output.
        Type `Meta` (represented as `dict` in JSON). """
        
        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("valueBase64Binary", "valueBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "value", True, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", True, None), 
            ("valueCanonical", "valueCanonical", fhirdatatypes.FHIRCanonical, False, "value", True, None), 
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", True, None), 
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", True, None), 
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", True, None), 
            ("valueDecimal", "valueDecimal", float, False, "value", True, None), 
            ("valueId", "valueId", fhirdatatypes.FHIRId, False, "value", True, None), 
            ("valueInstant", "valueInstant", fhirdatatypes.FHIRInstant, False, "value", True, None), 
            ("valueInteger", "valueInteger", int, False, "value", True, None), 
            ("valueMarkdown", "valueMarkdown", fhirdatatypes.FHIRMarkdown, False, "value", True, None), 
            ("valueOid", "valueOid", fhirdatatypes.FHIROid, False, "value", True, None), 
            ("valuePositiveInt", "valuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "value", True, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True, None), 
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", True, None), 
            ("valueUnsignedInt", "valueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "value", True, None), 
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", True, None), 
            ("valueUrl", "valueUrl", fhirdatatypes.FHIRUrl, False, "value", True, None), 
            ("valueUuid", "valueUuid", fhirdatatypes.FHIRUuid, False, "value", True, None), 
            ("valueAddress", "valueAddress", address.Address, False, "value", True, None), 
            ("valueAge", "valueAge", age.Age, False, "value", True, None), 
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True, None), 
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True, None), 
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True, None), 
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True, None), 
            ("valueCount", "valueCount", count.Count, False, "value", True, None), 
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True, None), 
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True, None), 
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True, None), 
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True, None), 
            ("valueMoney", "valueMoney", money.Money, False, "value", True, None), 
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True, None), 
            ("valueRange", "valueRange", range.Range, False, "value", True, None), 
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True, None), 
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True, None), 
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True, None), 
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True, None), 
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True, None), 
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True, None), 
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True, None), 
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True, None), 
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True, None), 
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True, None), 
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True, None), 
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True, None), 
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True, None), 
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True, None), 
        ])
        return js




class TaskRestriction(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.
    
    If the Task.focus is a request resource and the task is seeking fulfillment
    (i.e. is asking for the request to be actioned), this element identifies
    any limitations on what parts of the referenced request should be actioned.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.repetitions = None
        """ How many times to repeat.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.period = None
        """ When fulfillment sought.
        Type `Period` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ For whom is fulfillment sought?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(TaskRestriction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("repetitions", "repetitions", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("period", "period", period.Period, False, None, False, None), 
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js



from fhirclient.models import address

from fhirclient.models import age

from fhirclient.models import annotation

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import contactdetail

from fhirclient.models import contactpoint

from fhirclient.models import contributor

from fhirclient.models import count

from fhirclient.models import datarequirement

from fhirclient.models import distance

from fhirclient.models import dosage

from fhirclient.models import duration

from fhirclient.models import expression

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import humanname

from fhirclient.models import identifier

from fhirclient.models import meta

from fhirclient.models import money

from fhirclient.models import parameterdefinition

from fhirclient.models import period

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.models import ratio

from fhirclient.models import relatedartifact

from fhirclient.codesystems import requestpriority

from fhirclient.models import sampleddata

from fhirclient.models import signature

from fhirclient.codesystems import taskstatus

from fhirclient.models import timing

from fhirclient.models import triggerdefinition

from fhirclient.models import usagecontext

