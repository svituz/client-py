#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImagingStudy)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).
    
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    
    resource_type = "ImagingStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifiers for the whole study.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | available | cancelled | entered-in-error | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.modality = None
        """ All series modality if actual acquisition modalities.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who or what is the subject of the study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter with which this imaging study is associated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.started = None
        """ When the study was started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Request fulfilled.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.referrer = None
        """ Referring physician.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.interpreter = None
        """ Who interpreted images.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Study access endpoint.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.numberOfSeries = None
        """ Number of Study Related Series.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.numberOfInstances = None
        """ Number of Study Related Instances.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.procedureReference = None
        """ The performed Procedure reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.procedureCode = None
        """ The performed procedure code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where ImagingStudy occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why the study was requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why was study performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.note = None
        """ User-defined comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Institution-generated description.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        
        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, imagingstudystatus.ImagingStudyStatus), 
            ("modality", "modality", coding.Coding, True, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("started", "started", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("referrer", "referrer", fhirreference.FHIRReference, False, None, False, None), 
            ("interpreter", "interpreter", fhirreference.FHIRReference, True, None, False, None), 
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False, None), 
            ("numberOfSeries", "numberOfSeries", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("numberOfInstances", "numberOfInstances", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, None, False, None), 
            ("procedureCode", "procedureCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("location", "location", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("series", "series", ImagingStudySeries, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.
    
    Each study has one or more series of images or other content.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.uid = None
        """ DICOM Series Instance UID for the series.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.number = None
        """ Numeric identifier of this series.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.modality = None
        """ The modality of the instances in the series.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.description = None
        """ A short human readable summary of the series.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.numberOfInstances = None
        """ Number of Series Related Instances.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.endpoint = None
        """ Series access endpoint.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Body part examined.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.laterality = None
        """ Body part laterality.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimen imaged.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.started = None
        """ When the series started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.performer = None
        """ Who performed the series.
        List of `ImagingStudySeriesPerformer` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ A single SOP instance from the series.
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """
        
        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("uid", "uid", fhirdatatypes.FHIRId, False, None, True, None), 
            ("number", "number", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("modality", "modality", coding.Coding, False, None, True, None), 
            ("description", "description", fhirdatatypes.FHIRString, False, None, False, None), 
            ("numberOfInstances", "numberOfInstances", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False, None), 
            ("bodySite", "bodySite", coding.Coding, False, None, False, None), 
            ("laterality", "laterality", coding.Coding, False, None, False, None), 
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False, None), 
            ("started", "started", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("performer", "performer", ImagingStudySeriesPerformer, True, None, False, None), 
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False, None), 
        ])
        return js




class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.
    
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.uid = None
        """ DICOM SOP Instance UID.
        Type `FHIRId` (represented as `str` in JSON). """
        
        self.sopClass = None
        """ DICOM class type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.number = None
        """ The number of this instance in the series.
        Type `FHIRUnsignedInt` (represented as `int` in JSON). """
        
        self.title = None
        """ Description of instance.
        Type `FHIRString` (represented as `str` in JSON). """
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("uid", "uid", fhirdatatypes.FHIRId, False, None, True, None), 
            ("sopClass", "sopClass", coding.Coding, False, None, True, None), 
            ("number", "number", fhirdatatypes.FHIRUnsignedInt, False, None, False, None), 
            ("title", "title", fhirdatatypes.FHIRString, False, None, False, None), 
        ])
        return js




class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ Who performed the series.
    
    Indicates who or what performed the series and how they were involved.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.actor = None
        """ Who performed the series.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImagingStudySeriesPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("function", "function", codeableconcept.CodeableConcept, False, None, False, None), 
            ("actor", "actor", fhirreference.FHIRReference, False, None, True, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.models import coding

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.codesystems import imagingstudystatus

