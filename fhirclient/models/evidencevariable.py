#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2020-03-26.
#  2020, SMART Health IT.


from . import domainresource

class EvidenceVariable(domainresource.DomainResource):
    """ A population, intervention, or exposure definition.
    
    The EvidenceVariable resource describes a "PICO" element that knowledge
    (evidence, assertion, recommendation) is about.
    """
    
    resource_type = "EvidenceVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ Canonical identifier for this evidence variable, represented as a
        URI (globally unique).
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Additional identifier for the evidence variable.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the evidence variable.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.name = None
        """ Name for this evidence variable (computer friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.title = None
        """ Name for this evidence variable (human friendly).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.shortTitle = None
        """ Title for use in informal contexts.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.subtitle = None
        """ Subordinate title of the EvidenceVariable.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
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
        """ Natural language description of the evidence variable.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.note = None
        """ Used for footnotes or explanatory notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for evidence variable (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `FHIRMarkdown` (represented as `str` in JSON). """
        
        self.approvalDate = None
        """ When the evidence variable was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastReviewDate = None
        """ When the evidence variable was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ When the evidence variable is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.topic = None
        """ The category of the EvidenceVariable, such as Education, Treatment,
        Assessment, etc..
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
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.type = None
        """ dichotomous | continuous | descriptive.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.characteristic = None
        """ What defines the members of the evidence element.
        List of `EvidenceVariableCharacteristic` items (represented as `dict` in JSON). """
        
        super(EvidenceVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("url", "url", fhirdatatypes.FHIRUri, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("version", "version", fhirdatatypes.FHIRString, False, None, False),
            ("name", "name", fhirdatatypes.FHIRString, False, None, False),
            ("title", "title", fhirdatatypes.FHIRString, False, None, False),
            ("shortTitle", "shortTitle", fhirdatatypes.FHIRString, False, None, False),
            ("subtitle", "subtitle", fhirdatatypes.FHIRString, False, None, False),
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True),
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False),
            ("publisher", "publisher", fhirdatatypes.FHIRString, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("description", "description", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("copyright", "copyright", fhirdatatypes.FHIRMarkdown, False, None, False),
            ("approvalDate", "approvalDate", fhirdatatypes.FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdatatypes.FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, True),
        ])
        return js



from . import backboneelement

class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """ What defines the members of the evidence element.
    
    A characteristic that defines the members of the evidence element. Multiple
    characteristics are applied with "and" semantics.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the characteristic.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.definitionReference = None
        """ What code or expression defines members?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definitionCanonical = None
        """ What code or expression defines members?.
        Type `FHIRCanonical` (represented as `str` in JSON). """
        
        self.definitionCodeableConcept = None
        """ What code or expression defines members?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definitionExpression = None
        """ What code or expression defines members?.
        Type `Expression` (represented as `dict` in JSON). """
        
        self.definitionDataRequirement = None
        """ What code or expression defines members?.
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.definitionTriggerDefinition = None
        """ What code or expression defines members?.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.usageContext = None
        """ What code/value pairs define members?.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Whether the characteristic includes or excludes members.
        Type `bool`. """
        
        self.participantEffectiveDateTime = None
        """ What time period do participants cover.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.participantEffectivePeriod = None
        """ What time period do participants cover.
        Type `Period` (represented as `dict` in JSON). """
        
        self.participantEffectiveDuration = None
        """ What time period do participants cover.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectiveTiming = None
        """ What time period do participants cover.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.timeFromStart = None
        """ Observation time from study start.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.groupMeasure = None
        """ mean | median | mean-of-mean | mean-of-median | median-of-mean |
        median-of-median.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        super(EvidenceVariableCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("description", "description", fhirdatatypes.FHIRString, False, None, False),
            ("definitionReference", "definitionReference", fhirreference.FHIRReference, False, "definition", True),
            ("definitionCanonical", "definitionCanonical", fhirdatatypes.FHIRCanonical, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("definitionTriggerDefinition", "definitionTriggerDefinition", triggerdefinition.TriggerDefinition, False, "definition", True),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdatatypes.FHIRDateTime, False, "participantEffective", False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("timeFromStart", "timeFromStart", duration.Duration, False, None, False),
            ("groupMeasure", "groupMeasure", fhirdatatypes.FHIRCode, False, None, False),
        ])
        return js



import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']

try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']

try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']

try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']

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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']

try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']

try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']

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

