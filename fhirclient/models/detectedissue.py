#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DetectedIssue)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.
    
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    
    resource_type = "DetectedIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique id for the detected issue.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | preliminary | final | amended +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.code = None
        """ Issue Category, e.g. drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.severity = None
        """ high | moderate | low.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.patient = None
        """ Associated patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifiedDateTime = None
        """ When identified.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifiedPeriod = None
        """ When identified.
        Type `Period` (represented as `dict` in JSON). """
        
        self.author = None
        """ The provider or device that identified the issue.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.implicated = None
        """ Problem resource.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.evidence = None
        """ Supporting evidence.
        List of `DetectedIssueEvidence` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Description and context.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.reference = None
        """ Authority for issue.
        Type `FHIRUri` (represented as `str` in JSON). """
        
        self.mitigation = None
        """ Step taken to address.
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """
        
        super(DetectedIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, observationstatus.ObservationStatus), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, False, None), 
            ("severity", "severity", fhirdatatypes.FHIRCode, False, None, False, detectedissueseverity.DetectedIssueSeverity), 
            ("patient", "patient", fhirreference.FHIRReference, False, None, False, None), 
            ("identifiedDateTime", "identifiedDateTime", fhirdatatypes.FHIRDateTime, False, "identified", False, None), 
            ("identifiedPeriod", "identifiedPeriod", period.Period, False, "identified", False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
            ("implicated", "implicated", fhirreference.FHIRReference, True, None, False, None), 
            ("evidence", "evidence", DetectedIssueEvidence, True, None, False, None), 
            ("detail", "detail", fhirdatatypes.FHIRString, False, None, False, None), 
            ("reference", "reference", fhirdatatypes.FHIRUri, False, None, False, None), 
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DetectedIssueEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    
    Supporting evidence or manifestations that provide the basis for
    identifying the detected issue such as a GuidanceResponse or MeasureReport.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Manifestation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(DetectedIssueEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False, None), 
            ("detail", "detail", fhirreference.FHIRReference, True, None, False, None), 
        ])
        return js




class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.
    
    Indicates an action that has been taken or is committed to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date committed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.author = None
        """ Who is committing?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DetectedIssueMitigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, True, None), 
            ("date", "date", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("author", "author", fhirreference.FHIRReference, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import detectedissueseverity

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import observationstatus

from fhirclient.models import period

