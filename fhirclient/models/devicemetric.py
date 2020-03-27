#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceMetric)
#  2020, SMART Health IT.


from fhirclient.models import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
    
    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    
    resource_type = "DeviceMetric"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Identity of metric, for example Heart Rate or PEEP Setting.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Unit of Measure for the Metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ Describes the link to the source Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Describes the link to the parent Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.operationalStatus = None
        """ on | off | standby | entered-in-error.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.color = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.category = None
        """ measurement | setting | calculation | unspecified.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.measurementPeriod = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.calibration = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        
        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False, None), 
            ("type", "type", codeableconcept.CodeableConcept, False, None, True, None), 
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False, None), 
            ("source", "source", fhirreference.FHIRReference, False, None, False, None), 
            ("parent", "parent", fhirreference.FHIRReference, False, None, False, None), 
            ("operationalStatus", "operationalStatus", fhirdatatypes.FHIRCode, False, None, False, devicemetricoperationalstatus.DeviceMetricOperationalStatus), 
            ("color", "color", fhirdatatypes.FHIRCode, False, None, False, devicemetriccolor.DeviceMetricColor), 
            ("category", "category", fhirdatatypes.FHIRCode, False, None, True, devicemetriccategory.DeviceMetricCategory), 
            ("measurementPeriod", "measurementPeriod", timing.Timing, False, None, False, None), 
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False, None), 
        ])
        return js



from fhirclient.models import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ unspecified | offset | gain | two-point.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.state = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `FHIRCode` (represented as `str` in JSON). """
        
        self.time = None
        """ Describes the time last calibration has been performed.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("type", "type", fhirdatatypes.FHIRCode, False, None, False, devicemetriccalibrationtype.DeviceMetricCalibrationType), 
            ("state", "state", fhirdatatypes.FHIRCode, False, None, False, devicemetriccalibrationstate.DeviceMetricCalibrationState), 
            ("time", "time", fhirdatatypes.FHIRInstant, False, None, False, None), 
        ])
        return js



from fhirclient.models import codeableconcept

from fhirclient.codesystems import devicemetriccalibrationstate

from fhirclient.codesystems import devicemetriccalibrationtype

from fhirclient.codesystems import devicemetriccategory

from fhirclient.codesystems import devicemetriccolor

from fhirclient.codesystems import devicemetricoperationalstatus

from fhirclient.models import fhirdatatypes

from fhirclient.models import fhirreference

from fhirclient.models import identifier

from fhirclient.models import timing

