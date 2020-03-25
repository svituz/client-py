#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import devicemetric

class DeviceMetricTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceMetric", js["resourceType"])
        return devicemetric.DeviceMetric(js)

    def testDeviceMetric1(self):
        inst = self.instantiate_from('devicemetric-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DeviceMetric instance')
        self.implDeviceMetric1(inst)

        js = inst.as_json()
        self.assertEqual("DeviceMetric", js["resourceType"])
        inst2 = devicemetric.DeviceMetric(js)
        self.implDeviceMetric1(inst2)

    def implDeviceMetric1(self, inst):
        self.assertEqual(inst.calibration[0].state.value, FHIRCode('calibrated').value)
        self.assertEqual(inst.calibration[0].state.as_json(), 'calibrated')
        self.assertEqual(inst.calibration[0].time.value, FHIRInstant('2016-12-28T09:03:04-05:00').value)
        self.assertEqual(inst.calibration[0].time.as_json(), '2016-12-28T09:03:04-05:00')
        self.assertEqual(inst.calibration[0].time.date, FHIRInstant('2016-12-28T09:03:04-05:00').date)
        self.assertEqual(inst.calibration[0].type.value, FHIRCode('two-point').value)
        self.assertEqual(inst.calibration[0].type.as_json(), 'two-point')
        self.assertEqual(inst.category.value, FHIRCode('measurement').value)
        self.assertEqual(inst.category.as_json(), 'measurement')
        self.assertEqual(inst.color.value, FHIRCode('blue').value)
        self.assertEqual(inst.color.as_json(), 'blue')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://goodcare.org/devicemetric/id').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://goodcare.org/devicemetric/id')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('345675').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '345675')
        self.assertEqual(inst.measurementPeriod.repeat.frequency.value, FHIRPositiveInt('1').value)
        self.assertEqual(inst.measurementPeriod.repeat.frequency.as_json(), 1)
        self.assertEqual(inst.measurementPeriod.repeat.period, 1)
        self.assertEqual(inst.measurementPeriod.repeat.periodUnit.value, FHIRCode('s').value)
        self.assertEqual(inst.measurementPeriod.repeat.periodUnit.as_json(), 's')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.operationalStatus.value, FHIRCode('on').value)
        self.assertEqual(inst.operationalStatus.as_json(), 'on')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode('150456').value)
        self.assertEqual(inst.type.coding[0].code.as_json(), '150456')
        self.assertEqual(inst.type.coding[0].display.value, FHIRString('MDC_PULS_OXIM_SAT_O2').value)
        self.assertEqual(inst.type.coding[0].display.as_json(), 'MDC_PULS_OXIM_SAT_O2')
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri('urn:iso:std:iso:11073:10101').value)
        self.assertEqual(inst.type.coding[0].system.as_json(), 'urn:iso:std:iso:11073:10101')
        self.assertEqual(inst.unit.coding[0].code.value, FHIRCode('262688').value)
        self.assertEqual(inst.unit.coding[0].code.as_json(), '262688')
        self.assertEqual(inst.unit.coding[0].display.value, FHIRString('MDC_DIM_PERCENT').value)
        self.assertEqual(inst.unit.coding[0].display.as_json(), 'MDC_DIM_PERCENT')
        self.assertEqual(inst.unit.coding[0].system.value, FHIRUri('urn:iso:std:iso:11073:10101').value)
        self.assertEqual(inst.unit.coding[0].system.as_json(), 'urn:iso:std:iso:11073:10101')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRInstant, FHIRUri, FHIRString, FHIRPositiveInt