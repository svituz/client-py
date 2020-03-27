#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Extension)
#  2020, SMART Health IT.


from fhirclient.models import element

class Extension(element.Element):
    """ Optional Extensions Element.
    
    Optional Extension Element - found in all resources.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ identifies the meaning of the extension.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueBase64Binary = None
        """ Value of extension.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ Value of extension.
        Type `bool`. """
        
        self.valueCanonical = None
        """ Value of extension.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.valueCode = None
        """ Value of extension.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueDate = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Value of extension.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Value of extension.
        Type `float`. """
        
        self.valueId = None
        """ Value of extension.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.valueInstant = None
        """ Value of extension.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Value of extension.
        Type `int`. """
        
        self.valueMarkdown = None
        """ Value of extension.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.valueOid = None
        """ Value of extension.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.valuePositiveInt = None
        """ Value of extension.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.valueString = None
        """ Value of extension.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Value of extension.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUnsignedInt = None
        """ Value of extension.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.valueUri = None
        """ Value of extension.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueUrl = None
        """ Value of extension.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.valueUuid = None
        """ Value of extension.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.valueAddress = None
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ Value of extension.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ Value of extension.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDistance = None
        """ Value of extension.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ Value of extension.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ Value of extension.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueTiming = None
        """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ Value of extension.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ Value of extension.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ Value of extension.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ Value of extension.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueParameterDefinition = None
        """ Value of extension.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ Value of extension.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ Value of extension.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUsageContext = None
        """ Value of extension.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ Value of extension.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueMeta = None
        """ Value of extension.
        Type `Meta` (represented as `dict` in JSON). """
        
        super(Extension, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, True, None), 
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

