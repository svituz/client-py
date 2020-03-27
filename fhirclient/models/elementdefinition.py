#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ElementDefinition)
#  2020, SMART Health IT.


from fhirclient.models import backboneelement

class ElementDefinition(backboneelement.BackboneElement):
    """ Definition of an element in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ Path of the element in the hierarchy of elements.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.representation = None
        """ xmlAttr | xmlText | typeAttr | cdaText | xhtml.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.sliceName = None
        """ Name for this particular element (in a set of slices).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.sliceIsConstraining = None
        """ If this slice definition constrains an inherited slice definition
        (or not).
        Type `bool`. """
        
        self.label = None
        """ Name for element to display with or prompt for element.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.code = None
        """ Corresponding codes in terminologies.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.slicing = None
        """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """
        
        self.short = None
        """ Concise definition for space-constrained presentation.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.definition = None
        """ Full formal definition as narrative text.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.comment = None
        """ Comments about the use of this element.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.requirements = None
        """ Why this resource has been created.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.alias = None
        """ Other names.
        List of `FHIRString` items (represented as `str` in JSON). """
        
        self.min = None
        """ Minimum Cardinality.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.base = None
        """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Reference to definition of content for the element.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.type = None
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
        """ Specified value if missing from instance.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.defaultValueBoolean = None
        """ Specified value if missing from instance.
        Type `bool`. """
        
        self.defaultValueCanonical = None
        """ Specified value if missing from instance.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.defaultValueCode = None
        """ Specified value if missing from instance.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.defaultValueDate = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime = None
        """ Specified value if missing from instance.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.defaultValueDecimal = None
        """ Specified value if missing from instance.
        Type `float`. """
        
        self.defaultValueId = None
        """ Specified value if missing from instance.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.defaultValueInstant = None
        """ Specified value if missing from instance.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.defaultValueInteger = None
        """ Specified value if missing from instance.
        Type `int`. """
        
        self.defaultValueMarkdown = None
        """ Specified value if missing from instance.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.defaultValueOid = None
        """ Specified value if missing from instance.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.defaultValuePositiveInt = None
        """ Specified value if missing from instance.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.defaultValueString = None
        """ Specified value if missing from instance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.defaultValueTime = None
        """ Specified value if missing from instance.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.defaultValueUnsignedInt = None
        """ Specified value if missing from instance.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.defaultValueUri = None
        """ Specified value if missing from instance.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.defaultValueUrl = None
        """ Specified value if missing from instance.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.defaultValueUuid = None
        """ Specified value if missing from instance.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.defaultValueAddress = None
        """ Specified value if missing from instance.
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge = None
        """ Specified value if missing from instance.
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation = None
        """ Specified value if missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment = None
        """ Specified value if missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueCodeableConcept = None
        """ Specified value if missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding = None
        """ Specified value if missing from instance.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint = None
        """ Specified value if missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueCount = None
        """ Specified value if missing from instance.
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDistance = None
        """ Specified value if missing from instance.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDuration = None
        """ Specified value if missing from instance.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName = None
        """ Specified value if missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueIdentifier = None
        """ Specified value if missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueMoney = None
        """ Specified value if missing from instance.
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod = None
        """ Specified value if missing from instance.
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValueQuantity = None
        """ Specified value if missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange = None
        """ Specified value if missing from instance.
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio = None
        """ Specified value if missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference = None
        """ Specified value if missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData = None
        """ Specified value if missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature = None
        """ Specified value if missing from instance.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueTiming = None
        """ Specified value if missing from instance.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail = None
        """ Specified value if missing from instance.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContributor = None
        """ Specified value if missing from instance.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement = None
        """ Specified value if missing from instance.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueExpression = None
        """ Specified value if missing from instance.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueParameterDefinition = None
        """ Specified value if missing from instance.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact = None
        """ Specified value if missing from instance.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition = None
        """ Specified value if missing from instance.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUsageContext = None
        """ Specified value if missing from instance.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueDosage = None
        """ Specified value if missing from instance.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueMeta = None
        """ Specified value if missing from instance.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.meaningWhenMissing = None
        """ Implicit meaning when this element is missing.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.orderMeaning = None
        """ What the order of the elements means.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.fixedBase64Binary = None
        """ Value must be exactly this.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.fixedBoolean = None
        """ Value must be exactly this.
        Type `bool`. """
        
        self.fixedCanonical = None
        """ Value must be exactly this.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.fixedCode = None
        """ Value must be exactly this.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.fixedDate = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedDateTime = None
        """ Value must be exactly this.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.fixedDecimal = None
        """ Value must be exactly this.
        Type `float`. """
        
        self.fixedId = None
        """ Value must be exactly this.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.fixedInstant = None
        """ Value must be exactly this.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.fixedInteger = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedMarkdown = None
        """ Value must be exactly this.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.fixedOid = None
        """ Value must be exactly this.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.fixedPositiveInt = None
        """ Value must be exactly this.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.fixedString = None
        """ Value must be exactly this.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.fixedTime = None
        """ Value must be exactly this.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.fixedUnsignedInt = None
        """ Value must be exactly this.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.fixedUri = None
        """ Value must be exactly this.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.fixedUrl = None
        """ Value must be exactly this.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.fixedUuid = None
        """ Value must be exactly this.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.fixedAddress = None
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """
        
        self.fixedAge = None
        """ Value must be exactly this.
        Type `Age` (represented as `dict` in JSON). """
        
        self.fixedAnnotation = None
        """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.fixedAttachment = None
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.fixedCodeableConcept = None
        """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fixedCoding = None
        """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.fixedContactPoint = None
        """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.fixedCount = None
        """ Value must be exactly this.
        Type `Count` (represented as `dict` in JSON). """
        
        self.fixedDistance = None
        """ Value must be exactly this.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.fixedDuration = None
        """ Value must be exactly this.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.fixedHumanName = None
        """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.fixedIdentifier = None
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.fixedMoney = None
        """ Value must be exactly this.
        Type `Money` (represented as `dict` in JSON). """
        
        self.fixedPeriod = None
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """
        
        self.fixedQuantity = None
        """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.fixedRange = None
        """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """
        
        self.fixedRatio = None
        """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.fixedReference = None
        """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fixedSampledData = None
        """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.fixedSignature = None
        """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.fixedTiming = None
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.fixedContactDetail = None
        """ Value must be exactly this.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.fixedContributor = None
        """ Value must be exactly this.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.fixedDataRequirement = None
        """ Value must be exactly this.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.fixedExpression = None
        """ Value must be exactly this.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.fixedParameterDefinition = None
        """ Value must be exactly this.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.fixedRelatedArtifact = None
        """ Value must be exactly this.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.fixedTriggerDefinition = None
        """ Value must be exactly this.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.fixedUsageContext = None
        """ Value must be exactly this.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.fixedDosage = None
        """ Value must be exactly this.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.fixedMeta = None
        """ Value must be exactly this.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.patternBase64Binary = None
        """ Value must have at least these property values.
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.patternBoolean = None
        """ Value must have at least these property values.
        Type `bool`. """
        
        self.patternCanonical = None
        """ Value must have at least these property values.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.patternCode = None
        """ Value must have at least these property values.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.patternDate = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternDateTime = None
        """ Value must have at least these property values.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.patternDecimal = None
        """ Value must have at least these property values.
        Type `float`. """
        
        self.patternId = None
        """ Value must have at least these property values.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.patternInstant = None
        """ Value must have at least these property values.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.patternInteger = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternMarkdown = None
        """ Value must have at least these property values.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.patternOid = None
        """ Value must have at least these property values.
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.patternPositiveInt = None
        """ Value must have at least these property values.
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.patternString = None
        """ Value must have at least these property values.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.patternTime = None
        """ Value must have at least these property values.
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.patternUnsignedInt = None
        """ Value must have at least these property values.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.patternUri = None
        """ Value must have at least these property values.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.patternUrl = None
        """ Value must have at least these property values.
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.patternUuid = None
        """ Value must have at least these property values.
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.patternAddress = None
        """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """
        
        self.patternAge = None
        """ Value must have at least these property values.
        Type `Age` (represented as `dict` in JSON). """
        
        self.patternAnnotation = None
        """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patternAttachment = None
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.patternCodeableConcept = None
        """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patternCoding = None
        """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patternContactPoint = None
        """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.patternCount = None
        """ Value must have at least these property values.
        Type `Count` (represented as `dict` in JSON). """
        
        self.patternDistance = None
        """ Value must have at least these property values.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.patternDuration = None
        """ Value must have at least these property values.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.patternHumanName = None
        """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patternIdentifier = None
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patternMoney = None
        """ Value must have at least these property values.
        Type `Money` (represented as `dict` in JSON). """
        
        self.patternPeriod = None
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """
        
        self.patternQuantity = None
        """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.patternRange = None
        """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """
        
        self.patternRatio = None
        """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.patternReference = None
        """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patternSampledData = None
        """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.patternSignature = None
        """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.patternTiming = None
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.patternContactDetail = None
        """ Value must have at least these property values.
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.patternContributor = None
        """ Value must have at least these property values.
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.patternDataRequirement = None
        """ Value must have at least these property values.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.patternExpression = None
        """ Value must have at least these property values.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.patternParameterDefinition = None
        """ Value must have at least these property values.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.patternRelatedArtifact = None
        """ Value must have at least these property values.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.patternTriggerDefinition = None
        """ Value must have at least these property values.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.patternUsageContext = None
        """ Value must have at least these property values.
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.patternDosage = None
        """ Value must have at least these property values.
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.patternMeta = None
        """ Value must have at least these property values.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.example = None
        """ Example value (as defined for type).
        List of `ElementDefinitionExample` items (represented as `dict` in JSON). """
        
        self.minValueDate = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueDateTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.minValueInstant = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.minValueTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.minValueDecimal = None
        """ Minimum Allowed Value (for some types).
        Type `float`. """
        
        self.minValueInteger = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.minValuePositiveInt = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.minValueUnsignedInt = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.minValueQuantity = None
        """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxValueDate = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueDateTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.maxValueInstant = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.maxValueTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.maxValueDecimal = None
        """ Maximum Allowed Value (for some types).
        Type `float`. """
        
        self.maxValueInteger = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.maxValuePositiveInt = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.maxValueUnsignedInt = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.maxValueQuantity = None
        """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxLength = None
        """ Max length for strings.
        Type `int`. """
        
        self.condition = None
        """ Reference to invariant about presence.
        List of `FHIRId` items (represented as `str` in JSON). """
        
        self.constraint = None
        """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """
        
        self.mustSupport = None
        """ If the element must be supported.
        Type `bool`. """
        
        self.isModifier = None
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        
        self.isModifierReason = None
        """ Reason that this element is marked as a modifier.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.isSummary = None
        """ Include when _summary = true?.
        Type `bool`. """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        
        self.mapping = None
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        
        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, True, None), 
            ("representation", "representation", fhirdatatypes.FHIRCode, True, None, False, propertyrepresentation.PropertyRepresentation), 
            ("sliceName", "sliceName", fhirdatatypes.FHIRString, False, None, False, None), 
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False, None), 
            ("label", "label", fhirdatatypes.FHIRString, False, None, False, None), 
            ("code", "code", coding.Coding, True, None, False, None), 
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False, None), 
            ("short", "short", fhirdatatypes.FHIRString, False, None, False, None), 
            ("definition", "definition", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("comment", "comment", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("requirements", "requirements", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("alias", "alias", fhirdatatypes.FHIRString, True, None, False, None), 
            ("min", "min", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("max", "max", fhirdatatypes.FHIRString, False, None, False, None), 
            ("base", "base", ElementDefinitionBase, False, None, False, None), 
            ("contentReference", "contentReference", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("type", "type", ElementDefinitionType, True, None, False, None), 
            ("defaultValueBase64Binary", "defaultValueBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "defaultValue", False, None), 
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False, None), 
            ("defaultValueCanonical", "defaultValueCanonical", fhirdatatypes.FHIRCanonical, False, "defaultValue", False, None), 
            ("defaultValueCode", "defaultValueCode", fhirdatatypes.FHIRCode, False, "defaultValue", False, None), 
            ("defaultValueDate", "defaultValueDate", fhirdatatypes.FHIRDate, False, "defaultValue", False, None), 
            ("defaultValueDateTime", "defaultValueDateTime", fhirdatatypes.FHIRDateTime, False, "defaultValue", False, None), 
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False, None), 
            ("defaultValueId", "defaultValueId", fhirdatatypes.FHIRId, False, "defaultValue", False, None), 
            ("defaultValueInstant", "defaultValueInstant", fhirdatatypes.FHIRInstant, False, "defaultValue", False, None), 
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False, None), 
            ("defaultValueMarkdown", "defaultValueMarkdown", fhirdatatypes.FHIRMarkdown, False, "defaultValue", False, None), 
            ("defaultValueOid", "defaultValueOid", fhirdatatypes.FHIROid, False, "defaultValue", False, None), 
            ("defaultValuePositiveInt", "defaultValuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "defaultValue", False, None), 
            ("defaultValueString", "defaultValueString", fhirdatatypes.FHIRString, False, "defaultValue", False, None), 
            ("defaultValueTime", "defaultValueTime", fhirdatatypes.FHIRTime, False, "defaultValue", False, None), 
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "defaultValue", False, None), 
            ("defaultValueUri", "defaultValueUri", fhirdatatypes.FHIRUri, False, "defaultValue", False, None), 
            ("defaultValueUrl", "defaultValueUrl", fhirdatatypes.FHIRUrl, False, "defaultValue", False, None), 
            ("defaultValueUuid", "defaultValueUuid", fhirdatatypes.FHIRUuid, False, "defaultValue", False, None), 
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False, None), 
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False, None), 
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False, None), 
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False, None), 
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False, None), 
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False, None), 
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False, None), 
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False, None), 
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False, None), 
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False, None), 
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False, None), 
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False, None), 
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False, None), 
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False, None), 
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False, None), 
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False, None), 
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False, None), 
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False, None), 
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False, None), 
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False, None), 
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False, None), 
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False, None), 
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False, None), 
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False, None), 
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False, None), 
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False, None), 
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False, None), 
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False, None), 
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False, None), 
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False, None), 
            ("defaultValueMeta", "defaultValueMeta", meta.Meta, False, "defaultValue", False, None), 
            ("meaningWhenMissing", "meaningWhenMissing", fhirdatatypes.FHIRMarkdown, False, None, False, None), 
            ("orderMeaning", "orderMeaning", fhirdatatypes.FHIRString, False, None, False, None), 
            ("fixedBase64Binary", "fixedBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "fixed", False, None), 
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False, None), 
            ("fixedCanonical", "fixedCanonical", fhirdatatypes.FHIRCanonical, False, "fixed", False, None), 
            ("fixedCode", "fixedCode", fhirdatatypes.FHIRCode, False, "fixed", False, None), 
            ("fixedDate", "fixedDate", fhirdatatypes.FHIRDate, False, "fixed", False, None), 
            ("fixedDateTime", "fixedDateTime", fhirdatatypes.FHIRDateTime, False, "fixed", False, None), 
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False, None), 
            ("fixedId", "fixedId", fhirdatatypes.FHIRId, False, "fixed", False, None), 
            ("fixedInstant", "fixedInstant", fhirdatatypes.FHIRInstant, False, "fixed", False, None), 
            ("fixedInteger", "fixedInteger", int, False, "fixed", False, None), 
            ("fixedMarkdown", "fixedMarkdown", fhirdatatypes.FHIRMarkdown, False, "fixed", False, None), 
            ("fixedOid", "fixedOid", fhirdatatypes.FHIROid, False, "fixed", False, None), 
            ("fixedPositiveInt", "fixedPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "fixed", False, None), 
            ("fixedString", "fixedString", fhirdatatypes.FHIRString, False, "fixed", False, None), 
            ("fixedTime", "fixedTime", fhirdatatypes.FHIRTime, False, "fixed", False, None), 
            ("fixedUnsignedInt", "fixedUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "fixed", False, None), 
            ("fixedUri", "fixedUri", fhirdatatypes.FHIRUri, False, "fixed", False, None), 
            ("fixedUrl", "fixedUrl", fhirdatatypes.FHIRUrl, False, "fixed", False, None), 
            ("fixedUuid", "fixedUuid", fhirdatatypes.FHIRUuid, False, "fixed", False, None), 
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False, None), 
            ("fixedAge", "fixedAge", age.Age, False, "fixed", False, None), 
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False, None), 
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False, None), 
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False, None), 
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False, None), 
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False, None), 
            ("fixedCount", "fixedCount", count.Count, False, "fixed", False, None), 
            ("fixedDistance", "fixedDistance", distance.Distance, False, "fixed", False, None), 
            ("fixedDuration", "fixedDuration", duration.Duration, False, "fixed", False, None), 
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False, None), 
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False, None), 
            ("fixedMoney", "fixedMoney", money.Money, False, "fixed", False, None), 
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False, None), 
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False, None), 
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False, None), 
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False, None), 
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False, None), 
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False, None), 
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False, None), 
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False, None), 
            ("fixedContactDetail", "fixedContactDetail", contactdetail.ContactDetail, False, "fixed", False, None), 
            ("fixedContributor", "fixedContributor", contributor.Contributor, False, "fixed", False, None), 
            ("fixedDataRequirement", "fixedDataRequirement", datarequirement.DataRequirement, False, "fixed", False, None), 
            ("fixedExpression", "fixedExpression", expression.Expression, False, "fixed", False, None), 
            ("fixedParameterDefinition", "fixedParameterDefinition", parameterdefinition.ParameterDefinition, False, "fixed", False, None), 
            ("fixedRelatedArtifact", "fixedRelatedArtifact", relatedartifact.RelatedArtifact, False, "fixed", False, None), 
            ("fixedTriggerDefinition", "fixedTriggerDefinition", triggerdefinition.TriggerDefinition, False, "fixed", False, None), 
            ("fixedUsageContext", "fixedUsageContext", usagecontext.UsageContext, False, "fixed", False, None), 
            ("fixedDosage", "fixedDosage", dosage.Dosage, False, "fixed", False, None), 
            ("fixedMeta", "fixedMeta", meta.Meta, False, "fixed", False, None), 
            ("patternBase64Binary", "patternBase64Binary", fhirdatatypes.FHIRBase64Binary, False, "pattern", False, None), 
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False, None), 
            ("patternCanonical", "patternCanonical", fhirdatatypes.FHIRCanonical, False, "pattern", False, None), 
            ("patternCode", "patternCode", fhirdatatypes.FHIRCode, False, "pattern", False, None), 
            ("patternDate", "patternDate", fhirdatatypes.FHIRDate, False, "pattern", False, None), 
            ("patternDateTime", "patternDateTime", fhirdatatypes.FHIRDateTime, False, "pattern", False, None), 
            ("patternDecimal", "patternDecimal", float, False, "pattern", False, None), 
            ("patternId", "patternId", fhirdatatypes.FHIRId, False, "pattern", False, None), 
            ("patternInstant", "patternInstant", fhirdatatypes.FHIRInstant, False, "pattern", False, None), 
            ("patternInteger", "patternInteger", int, False, "pattern", False, None), 
            ("patternMarkdown", "patternMarkdown", fhirdatatypes.FHIRMarkdown, False, "pattern", False, None), 
            ("patternOid", "patternOid", fhirdatatypes.FHIROid, False, "pattern", False, None), 
            ("patternPositiveInt", "patternPositiveInt", fhirdatatypes.FHIRPositiveInt, False, "pattern", False, None), 
            ("patternString", "patternString", fhirdatatypes.FHIRString, False, "pattern", False, None), 
            ("patternTime", "patternTime", fhirdatatypes.FHIRTime, False, "pattern", False, None), 
            ("patternUnsignedInt", "patternUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "pattern", False, None), 
            ("patternUri", "patternUri", fhirdatatypes.FHIRUri, False, "pattern", False, None), 
            ("patternUrl", "patternUrl", fhirdatatypes.FHIRUrl, False, "pattern", False, None), 
            ("patternUuid", "patternUuid", fhirdatatypes.FHIRUuid, False, "pattern", False, None), 
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False, None), 
            ("patternAge", "patternAge", age.Age, False, "pattern", False, None), 
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False, None), 
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False, None), 
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False, None), 
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False, None), 
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False, None), 
            ("patternCount", "patternCount", count.Count, False, "pattern", False, None), 
            ("patternDistance", "patternDistance", distance.Distance, False, "pattern", False, None), 
            ("patternDuration", "patternDuration", duration.Duration, False, "pattern", False, None), 
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False, None), 
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False, None), 
            ("patternMoney", "patternMoney", money.Money, False, "pattern", False, None), 
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False, None), 
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False, None), 
            ("patternRange", "patternRange", range.Range, False, "pattern", False, None), 
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False, None), 
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False, None), 
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False, None), 
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False, None), 
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False, None), 
            ("patternContactDetail", "patternContactDetail", contactdetail.ContactDetail, False, "pattern", False, None), 
            ("patternContributor", "patternContributor", contributor.Contributor, False, "pattern", False, None), 
            ("patternDataRequirement", "patternDataRequirement", datarequirement.DataRequirement, False, "pattern", False, None), 
            ("patternExpression", "patternExpression", expression.Expression, False, "pattern", False, None), 
            ("patternParameterDefinition", "patternParameterDefinition", parameterdefinition.ParameterDefinition, False, "pattern", False, None), 
            ("patternRelatedArtifact", "patternRelatedArtifact", relatedartifact.RelatedArtifact, False, "pattern", False, None), 
            ("patternTriggerDefinition", "patternTriggerDefinition", triggerdefinition.TriggerDefinition, False, "pattern", False, None), 
            ("patternUsageContext", "patternUsageContext", usagecontext.UsageContext, False, "pattern", False, None), 
            ("patternDosage", "patternDosage", dosage.Dosage, False, "pattern", False, None), 
            ("patternMeta", "patternMeta", meta.Meta, False, "pattern", False, None), 
            ("example", "example", ElementDefinitionExample, True, None, False, None), 
            ("minValueDate", "minValueDate", fhirdatatypes.FHIRDate, False, "minValue", False, None), 
            ("minValueDateTime", "minValueDateTime", fhirdatatypes.FHIRDateTime, False, "minValue", False, None), 
            ("minValueInstant", "minValueInstant", fhirdatatypes.FHIRInstant, False, "minValue", False, None), 
            ("minValueTime", "minValueTime", fhirdatatypes.FHIRTime, False, "minValue", False, None), 
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False, None), 
            ("minValueInteger", "minValueInteger", int, False, "minValue", False, None), 
            ("minValuePositiveInt", "minValuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "minValue", False, None), 
            ("minValueUnsignedInt", "minValueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "minValue", False, None), 
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False, None), 
            ("maxValueDate", "maxValueDate", fhirdatatypes.FHIRDate, False, "maxValue", False, None), 
            ("maxValueDateTime", "maxValueDateTime", fhirdatatypes.FHIRDateTime, False, "maxValue", False, None), 
            ("maxValueInstant", "maxValueInstant", fhirdatatypes.FHIRInstant, False, "maxValue", False, None), 
            ("maxValueTime", "maxValueTime", fhirdatatypes.FHIRTime, False, "maxValue", False, None), 
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False, None), 
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False, None), 
            ("maxValuePositiveInt", "maxValuePositiveInt", fhirdatatypes.FHIRPositiveInt, False, "maxValue", False, None), 
            ("maxValueUnsignedInt", "maxValueUnsignedInt", fhirdatatypes.FHIRUnsignedInt, False, "maxValue", False, None), 
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False, None), 
            ("maxLength", "maxLength", int, False, None, False, None), 
            ("condition", "condition", fhirdatatypes.FHIRId, True, None, False, None), 
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False, None), 
            ("mustSupport", "mustSupport", bool, False, None, False, None), 
            ("isModifier", "isModifier", bool, False, None, False, None), 
            ("isModifierReason", "isModifierReason", fhirdatatypes.FHIRString, False, None, False, None), 
            ("isSummary", "isSummary", bool, False, None, False, None), 
            ("binding", "binding", ElementDefinitionBinding, False, None, False, None), 
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False, None), 
        ])
        return js



from fhirclient.models import element

class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.
    
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ Path that identifies the base element.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.min = None
        """ Min cardinality of the base element.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.max = None
        """ Max cardinality of the base element.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ElementDefinitionBase, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("path", "path", fhirdatatypes.FHIRString, False, None, True, None), 
            ("min", "min", fhirdatatypes.FHIRUnsignedInt, False, None, True, None), 
            ("max", "max", fhirdatatypes.FHIRString, False, None, True, None), 
        ])
        return js




class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.description = None
        """ Human explanation of the value set.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueSet = None
        """ Source of value set.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", fhirdatatypes.FHIRCode, False, None, True, bindingstrength.BindingStrength), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("valueSet", "valueSet", fhirdatatypes.FHIRCanonical, False, None, False, None), 
        ])
        return js




class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.key = None
        """ Target of 'condition' reference above.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.requirements = None
        """ Why this constraint is necessary or appropriate.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.severity = None
        """ error | warning.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.human = None
        """ Human description of constraint.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.expression = None
        """ FHIRPath expression of constraint.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.xpath = None
        """ XPath expression of constraint.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.source = None
        """ Reference to original source of constraint.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        super(ElementDefinitionConstraint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("key", "key", fhirdatatypes.FHIRId, False, None, True, None), 
            ("requirements", "requirements", fhirdatatypes.FHIRString, False, None, False, None), 
            ("severity", "severity", fhirdatatypes.FHIRCode, False, None, True, constraintseverity.ConstraintSeverity), 
            ("human", "human", fhirdatatypes.FHIRString, False, None, True, None), 
            ("expression", "expression", fhirdatatypes.FHIRString, False, None, False, None), 
            ("xpath", "xpath", fhirdatatypes.FHIRString, False, None, False, None), 
            ("source", "source", fhirdatatypes.FHIRCanonical, False, None, False, None), 
        ])
        return js




class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).
    
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.label = None
        """ Describes the purpose of this example.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueBase64Binary = None
        """ Value of Example (one of allowed types).
        Type `FHIRBase64Binary` (represented as `str` in JSON). """
        
        self.valueBoolean = None
        """ Value of Example (one of allowed types).
        Type `bool`. """
        
        self.valueCanonical = None
        """ Value of Example (one of allowed types).
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.valueCode = None
        """ Value of Example (one of allowed types).
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.valueDate = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Value of Example (one of allowed types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Value of Example (one of allowed types).
        Type `float`. """
        
        self.valueId = None
        """ Value of Example (one of allowed types).
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.valueInstant = None
        """ Value of Example (one of allowed types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        
        self.valueMarkdown = None
        """ Value of Example (one of allowed types).
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.valueOid = None
        """ Value of Example (one of allowed types).
        Type `FHIROid` (represented as `str` in JSON). """
        
        self.valuePositiveInt = None
        """ Value of Example (one of allowed types).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.valueString = None
        """ Value of Example (one of allowed types).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.valueTime = None
        """ Value of Example (one of allowed types).
        Type `FHIRTime` (represented as `str` in JSON). """
        
        self.valueUnsignedInt = None
        """ Value of Example (one of allowed types).
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.valueUri = None
        """ Value of Example (one of allowed types).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.valueUrl = None
        """ Value of Example (one of allowed types).
        Type `FHIRUrl` (represented as `str` in JSON). """
        
        self.valueUuid = None
        """ Value of Example (one of allowed types).
        Type `FHIRUuid` (represented as `str` in JSON). """
        
        self.valueAddress = None
        """ Value of Example (one of allowed types).
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ Value of Example (one of allowed types).
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ Value of Example (one of allowed types).
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Value of Example (one of allowed types).
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ Value of Example (one of allowed types).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Value of Example (one of allowed types).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Value of Example (one of allowed types).
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ Value of Example (one of allowed types).
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDistance = None
        """ Value of Example (one of allowed types).
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ Value of Example (one of allowed types).
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ Value of Example (one of allowed types).
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueIdentifier = None
        """ Value of Example (one of allowed types).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ Value of Example (one of allowed types).
        Type `Money` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ Value of Example (one of allowed types).
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value of Example (one of allowed types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value of Example (one of allowed types).
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Value of Example (one of allowed types).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Value of Example (one of allowed types).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Value of Example (one of allowed types).
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Value of Example (one of allowed types).
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueTiming = None
        """ Value of Example (one of allowed types).
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ Value of Example (one of allowed types).
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ Value of Example (one of allowed types).
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ Value of Example (one of allowed types).
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ Value of Example (one of allowed types).
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueParameterDefinition = None
        """ Value of Example (one of allowed types).
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ Value of Example (one of allowed types).
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ Value of Example (one of allowed types).
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUsageContext = None
        """ Value of Example (one of allowed types).
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ Value of Example (one of allowed types).
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueMeta = None
        """ Value of Example (one of allowed types).
        Type `Meta` (represented as `dict` in JSON). """
        
        super(ElementDefinitionExample, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", fhirdatatypes.FHIRString, False, None, True, None), 
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




class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identity = None
        """ Reference to mapping declaration.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.language = None
        """ Computable language of mapping.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.map = None
        """ Details of the mapping.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.comment = None
        """ Comments about the mapping or its use.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", fhirdatatypes.FHIRId, False, None, True, None), 
            ("language", "language", fhirdatatypes.FHIRCode, False, None, False, None), 
            ("map", "map", fhirdatatypes.FHIRString, False, None, True, None), 
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.
    
    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.discriminator = None
        """ Element values that are used to distinguish the slices.
        List of `ElementDefinitionSlicingDiscriminator` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Text description of how slicing works (or not).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.ordered = None
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self.rules = None
        """ closed | open | openAtEnd.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("ordered", "ordered", bool, False, None, False, None), 
            ("rules", "rules", fhirdatatypes.FHIRCode, False, None, True, slicingrules.SlicingRules), 
        ])
        return js




class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.
    
    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ value | exists | pattern | type | profile.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.path = None
        """ Path to element value.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ElementDefinitionSlicingDiscriminator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, True, discriminatortype.DiscriminatorType), 
            ("path", "path", fhirdatatypes.FHIRString, False, None, True, None), 
        ])
        return js




class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Data type or Resource (reference to definition).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.profile = None
        """ Profiles (StructureDefinition or IG) - one must apply.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.targetProfile = None
        """ Profile (StructureDefinition or IG) on the Reference/canonical
        target - one must apply.
        List of `FHIRCanonical` items (represented as `str` in JSON). """
        
        self.aggregation = None
        """ contained | referenced | bundled - how aggregated.
        List of `FHIRCode` items (represented as `str` in JSON). """
        
        self.versioning = None
        """ either | independent | specific.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("code", "code", fhirdatatypes.FHIRUri, False, None, True, None), 
            ("profile", "profile", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("targetProfile", "targetProfile", fhirdatatypes.FHIRCanonical, True, None, False, None), 
            ("aggregation", "aggregation", fhirdatatypes.FHIRCode, True, None, False, aggregationmode.AggregationMode), 
            ("versioning", "versioning", fhirdatatypes.FHIRCode, False, None, False, referenceversionrules.ReferenceVersionRules), 
        ])
        return js



from fhirclient.models import address

from fhirclient.models import age

from fhirclient.codesystems import aggregationmode

from fhirclient.models import annotation

from fhirclient.models import attachment

from fhirclient.codesystems import bindingstrength

from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.codesystems import constraintseverity

from fhirclient.models import contactdetail

from fhirclient.models import contactpoint

from fhirclient.models import contributor

from fhirclient.models import count

from fhirclient.models import datarequirement

from fhirclient.codesystems import discriminatortype

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

from fhirclient.codesystems import propertyrepresentation

from fhirclient.models import quantity

from fhirclient.models import range

from fhirclient.models import ratio

from fhirclient.codesystems import referenceversionrules

from fhirclient.models import relatedartifact

from fhirclient.models import sampleddata

from fhirclient.models import signature

from fhirclient.codesystems import slicingrules

from fhirclient.models import timing

from fhirclient.models import triggerdefinition

from fhirclient.models import usagecontext

