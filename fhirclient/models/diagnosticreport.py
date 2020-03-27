#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    
    resource_type = "DiagnosticReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Business identifier for report.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ What was requested.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | partial | preliminary | final +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ Service category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ The subject of the report - usually, but not always, the patient.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Health care event when test ordered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Clinically relevant time/time-period for report.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Clinically relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
        
        self.issued = None
        """ DateTime this version was made.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.performer = None
        """ Responsible Diagnostic Service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.resultsInterpreter = None
        """ Primary result interpreter.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimens this report is based on.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.result = None
        """ Observations.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.media = None
        """ Key images associated with this report.
        List of `DiagnosticReportMedia` items (represented as `dict` in JSON). """
        
        self.conclusion = None
        """ Clinical conclusion (interpretation) of test results.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.conclusionCode = None
        """ Codes for the clinical conclusion of test results.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.presentedForm = None
        """ Entire report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, diagnosticreportstatus.DiagnosticReportStatus), 
            ("category", "category", codeableconcept.CodeableConcept, True, None, False, None), 
            ("code", "code", codeableconcept.CodeableConcept, False, None, True, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("effectiveDateTime", "effectiveDateTime", fhirdatatypes.FHIRDateTime, False, "effective", False, None), 
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False, None), 
            ("issued", "issued", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("performer", "performer", fhirreference.FHIRReference, True, None, False, None), 
            ("resultsInterpreter", "resultsInterpreter", fhirreference.FHIRReference, True, None, False, None), 
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False, None), 
            ("result", "result", fhirreference.FHIRReference, True, None, False, None), 
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True, None, False, None), 
            ("media", "media", DiagnosticReportMedia, True, None, False, None), 
            ("conclusion", "conclusion", fhirdatatypes.FHIRString, False, None, False, None), 
            ("conclusionCode", "conclusionCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("presentedForm", "presentedForm", attachment.Attachment, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DiagnosticReportMedia(backboneelement.BackboneElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Comment about the image (e.g. explanation).
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.link = None
        """ Reference to the image source.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DiagnosticReportMedia, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReportMedia, self).elementProperties()
        js.extend([
            ("comment", "comment", fhirdatatypes.FHIRString, False, None, False, None), 
            ("link", "link", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.codesystems import diagnosticreportstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

