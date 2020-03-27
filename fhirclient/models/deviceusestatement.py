#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ Record of use of a device.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_type = "DeviceUseStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ External identifier for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | completed | entered-in-error +.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.subject = None
        """ Patient using device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.derivedFrom = None
        """ Supporting information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ How often  the device was used.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ How often  the device was used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ How often  the device was used.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.recordedOn = None
        """ When statement was recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.source = None
        """ Who made the statement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.device = None
        """ Reference to device used.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why device was used.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why was DeviceUseStatement performed?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Addition details (comments, instructions).
        List of `Annotation` items (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False, None), 
            ("status", "status", fhirdatatypes.FHIRCode, False, None, True, deviceusestatementstatus.DeviceUseStatementStatus), 
            ("subject", "subject", fhirreference.FHIRReference, False, None, True, None), 
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False, None), 
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False, None), 
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False, None), 
            ("timingDateTime", "timingDateTime", fhirdatatypes.FHIRDateTime, False, "timing", False, None), 
            ("recordedOn", "recordedOn", fhirdatatypes.FHIRDateTime, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, False, None, False, None), 
            ("device", "device", fhirreference.FHIRReference, False, None, True, None), 
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False, None), 
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False, None), 
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False, None), 
            ("note", "note", annotation.Annotation, True, None, False, None), 
        ])
        return js



from fhirclient.models import annotation

from fhirclient.models import codeableconcept

from fhirclient.codesystems import deviceusestatementstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import period

from fhirclient.models import timing

