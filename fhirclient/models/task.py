#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Task) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

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
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", fhirdatatypes.FHIRCanonical, False, None, False),
            ("instantiatesUri", "instantiatesUri", fhirdatatypes.FHIRUri, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("intent", "intent", fhirdatatypes.FHIRCode, False, None, True),
            ("priority", "priority", fhirdatatypes.FHIRCode, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, False, None, False),
            ("authoredOn", "authoredOn", fhirdatatypes.FHIRDateTime, False, None, False),
            ("lastModified", "lastModified", fhirdatatypes.FHIRDateTime, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
        ])
        return js



from . import backboneelement

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
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", fhirdatatypes.FHIRCanonical, False, "value", True),
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", True),
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", fhirdatatypes.FHIRId, False, "value", True),
            ("valueInstant", "valueInstant", fhirdatatypes.FHIRInstant, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", fhirdatatypes.FHIRMarkdown, False, "value", True),
            ("valueOid", "valueOid", fhirdatatypes.FHIROid, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "value", True),
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True),
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "value", True),
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", True),
            ("valueUrl", "valueUrl", fhirdatatypes.FHIRUrl, False, "value", True),
            ("valueUuid", "valueUuid", fhirdatatypes.FHIRUuid, False, "value", True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
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
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", fhirdatatypes.FHIRCanonical, False, "value", True),
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", True),
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", fhirdatatypes.FHIRId, False, "value", True),
            ("valueInstant", "valueInstant", fhirdatatypes.FHIRInstant, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", fhirdatatypes.FHIRMarkdown, False, "value", True),
            ("valueOid", "valueOid", fhirdatatypes.FHIROid, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "value", True),
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", True),
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "value", True),
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", True),
            ("valueUrl", "valueUrl", fhirdatatypes.FHIRUrl, False, "value", True),
            ("valueUuid", "valueUuid", fhirdatatypes.FHIRUuid, False, "value", True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
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
            ("repetitions", "repetitions", fhirdatatypes.FHIRPositiveInt, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
        ])
        return js



import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']

try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']

try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']

try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']

try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']

try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']

try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']

try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']

try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']

try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']

try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']

try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']

try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']

try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']

try:
    from . import fhirdatatypes
except ImportError:
    fhirdatatypes = sys.modules[__package__ + '.fhirdatatypes']

try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']

try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']

try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + '.meta']

try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']

try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']

try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']

try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']

try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']

try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']

try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']

try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']

try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']

try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']

try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']

try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']

