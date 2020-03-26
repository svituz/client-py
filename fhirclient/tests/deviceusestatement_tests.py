#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import deviceusestatement

class DeviceUseStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceUseStatement", js["resourceType"])
        return deviceusestatement.DeviceUseStatement(js)

    def testDeviceUseStatement1(self):
        inst = self.instantiate_from('deviceusestatement-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DeviceUseStatement instance')
        self.implDeviceUseStatement1(inst)

        js = inst.as_json()
        self.assertEqual("DeviceUseStatement", js["resourceType"])
        inst2 = deviceusestatement.DeviceUseStatement(js)
        self.implDeviceUseStatement1(inst2)

    def implDeviceUseStatement1(self, inst):
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http:goodhealth.org/identifiers").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http:goodhealth.org/identifiers")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("51ebb7a9-4e3a-4360-9a05-0cc2d869086f").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "51ebb7a9-4e3a-4360-9a05-0cc2d869086f")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRUri, FHIRString, FHIRCode