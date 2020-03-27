#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Parameters)
#  2020, SMART Health IT.


from fhirclient.models import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
    """
    
    resource_type = "Parameters"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.parameter = None
        """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(Parameters, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ Operation Parameter.
    
    A parameter passed to or received from the operation.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name from the definition.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueBase64Binary = None
        """ If parameter is a data type.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ If parameter is a data type.
        Type `bool`. """
        
        self.valueCanonical = None
        """ If parameter is a data type.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.valueCode = None
        """ If parameter is a data type.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """
        
        self.valueId = None
        """ If parameter is a data type.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.valueInstant = None
        """ If parameter is a data type.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueMarkdown = None
        """ If parameter is a data type.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.valueOid = None
        """ If parameter is a data type.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.valuePositiveInt = None
        """ If parameter is a data type.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.valueString = None
        """ If parameter is a data type.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ If parameter is a data type.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUnsignedInt = None
        """ If parameter is a data type.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.valueUri = None
        """ If parameter is a data type.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueUrl = None
        """ If parameter is a data type.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.valueUuid = None
        """ If parameter is a data type.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ If parameter is a data type.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ If parameter is a data type.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDistance = None
        """ If parameter is a data type.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ If parameter is a data type.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ If parameter is a data type.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueTiming = None
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ If parameter is a data type.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ If parameter is a data type.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ If parameter is a data type.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ If parameter is a data type.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueParameterDefinition = None
        """ If parameter is a data type.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ If parameter is a data type.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ If parameter is a data type.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUsageContext = None
        """ If parameter is a data type.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ If parameter is a data type.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueMeta = None
        """ If parameter is a data type.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.part = None
        """ Named part of a multi-part parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(ParametersParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", fhirdatatypes.FHIRString, False, None, True, None), 
            ("valueBase64Binary", "valueBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "value", False, None), 
            ("valueBoolean", "valueBoolean", bool, False, "value", False, None), 
            ("valueCanonical", "valueCanonical", fhirdatatypes.FHIRCanonical, False, "value", False, None), 
            ("valueCode", "valueCode", fhirdatatypes.FHIRCode, False, "value", False, None), 
            ("valueDate", "valueDate", fhirdatatypes.FHIRDate, False, "value", False, None), 
            ("valueDateTime", "valueDateTime", fhirdatatypes.FHIRDateTime, False, "value", False, None), 
            ("valueDecimal", "valueDecimal", float, False, "value", False, None), 
            ("valueId", "valueId", fhirdatatypes.FHIRId, False, "value", False, None), 
            ("valueInstant", "valueInstant", fhirdatatypes.FHIRInstant, False, "value", False, None), 
            ("valueInteger", "valueInteger", int, False, "value", False, None), 
            ("valueMarkdown", "valueMarkdown", fhirdatatypes.FHIRMarkdown, False, "value", False, None), 
            ("valueOid", "valueOid", fhirdatatypes.FHIROid, False, "value", False, None), 
            ("valuePositiveInt", "valuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "value", False, None), 
            ("valueString", "valueString", fhirdatatypes.FHIRString, False, "value", False, None), 
            ("valueTime", "valueTime", fhirdatatypes.FHIRTime, False, "value", False, None), 
            ("valueUnsignedInt", "valueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "value", False, None), 
            ("valueUri", "valueUri", fhirdatatypes.FHIRUri, False, "value", False, None), 
            ("valueUrl", "valueUrl", fhirdatatypes.FHIRUrl, False, "value", False, None), 
            ("valueUuid", "valueUuid", fhirdatatypes.FHIRUuid, False, "value", False, None), 
            ("valueAddress", "valueAddress", address.Address, False, "value", False, None), 
            ("valueAge", "valueAge", age.Age, False, "value", False, None), 
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False, None), 
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False, None), 
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False, None), 
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False, None), 
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False, None), 
            ("valueCount", "valueCount", count.Count, False, "value", False, None), 
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False, None), 
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False, None), 
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False, None), 
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False, None), 
            ("valueMoney", "valueMoney", money.Money, False, "value", False, None), 
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False, None), 
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False, None), 
            ("valueRange", "valueRange", range.Range, False, "value", False, None), 
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False, None), 
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False, None), 
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False, None), 
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False, None), 
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False, None), 
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", False, None), 
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", False, None), 
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", False, None), 
            ("valueExpression", "valueExpression", expression.Expression, False, "value", False, None), 
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", False, None), 
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", False, None), 
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", False, None), 
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", False, None), 
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", False, None), 
            ("valueMeta", "valueMeta", meta.Meta, False, "value", False, None), 
            ("resource", "resource", resource.Resource, False, None, False, None), 
            ("part", "part", ParametersParameter, True, None, False, None), 
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

from fhirclient.models import sampleddata

from fhirclient.models import signature

from fhirclient.models import timing

from fhirclient.models import triggerdefinition

from fhirclient.models import usagecontext

