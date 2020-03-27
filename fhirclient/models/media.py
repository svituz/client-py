#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Media)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    
    resource_type = "Media"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Procedure that caused this media to be created.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.type = None
        """ Classification of media as image, video, or audio.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modality = None
        """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.view = None
        """ Imaging view, e.g. Lateral or Antero-posterior.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who/What this Media is a record of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter associated with media.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.createdDateTime = None
        """ When Media was collected.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.createdPeriod = None
        """ When Media was collected.
        Type `Period` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Date/Time this version was made available.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why was event performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.deviceName = None
        """ Name of the device/manufacturer.
        Type `FHIRString` (represented as `str` in JSON). """
        
        self.device = None
        """ Observing Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.height = None
        """ Height of the image in pixels (photo/video).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.width = None
        """ Width of the image in pixels (photo/video).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.frames = None
        """ Number of frames if > 1 (photo).
        Type `FHIRPositiveInt` (represented as `int` in JSON). """
        
        self.duration = None
        """ Length in seconds (audio / video).
        Type `float`. """
        
        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the media.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(Media, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, eventstatus.EventStatus), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, False, None), 
            ("modality", "modality", codeableconcept.CodeableConcept, False, None, False, None), 
            ("view", "view", codeableconcept.CodeableConcept, False, None, False, None), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, False, None), 
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False, None), 
            ("createdDateTime", "createdDateTime", fhirdatatypes.FHIRDateTime, False, "created", False, None), 
            ("createdPeriod", "createdPeriod", period.Period, False, "created", False, None), 
            ("issued", "issued", fhirdatatypes.FHIRInstant, False, None, False, None), 
            ("operator", "operator", fhirreference.FHIRReference, False, None, False, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False, None), 
            ("deviceName", "deviceName", fhirdatatypes.FHIRString, False, None, False, None), 
            ("device", "device", fhirreference.FHIRReference, False, None, False, None), 
            ("height", "height", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("width", "width", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("frames", "frames", fhirdatatypes.FHIRPositiveInt, False, None, False, None), 
            ("duration", "duration", float, False, None, False, None), 
            ("content", "content", attachment.Attachment, False, None, True, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import attachment

from fhirclient.models import codeableconcept

from fhirclient.codesystems import eventstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

