#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import devicerequest

class DeviceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceRequest", js["resourceType"])
        return devicerequest.DeviceRequest(js)

    def testDeviceRequest1(self):
        inst = self.instantiate_from('devicerequest-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DeviceRequest instance')
        self.implDeviceRequest1(inst)

        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest1(inst2)

    def implDeviceRequest1(self, inst):
        self.assertEqual(inst.intent.value, FHIRCode("original-order").value)
        self.assertEqual(inst.intent.as_json(), "original-order")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testDeviceRequest2(self):
        inst = self.instantiate_from('devicerequest-example-insulinpump.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DeviceRequest instance')
        self.implDeviceRequest2(inst)

        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest2(inst2)

    def implDeviceRequest2(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime("2013-05-08T09:33:27+07:00").value)
        self.assertEqual(inst.authoredOn.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.codeCodeableConcept.coding[0].code.value, FHIRCode("43148-6").value)
        self.assertEqual(inst.codeCodeableConcept.coding[0].code.as_json(), "43148-6")
        self.assertEqual(inst.codeCodeableConcept.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.codeCodeableConcept.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.codeCodeableConcept.text.value, FHIRString("Insulin delivery device panel").value)
        self.assertEqual(inst.codeCodeableConcept.text.as_json(), "Insulin delivery device panel")
        self.assertEqual(inst.groupIdentifier.value.value, FHIRString("ip_request1").value)
        self.assertEqual(inst.groupIdentifier.value.as_json(), "ip_request1")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("ip_request1.1").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "ip_request1.1")
        self.assertEqual(inst.instantiatesCanonical[0].value, FHIRCanonical("http://motivemi.com/artifacts/PlanDefinition/low-suicide-risk-order-set").value)
        self.assertEqual(inst.instantiatesCanonical[0].as_json(), "http://motivemi.com/artifacts/PlanDefinition/low-suicide-risk-order-set")
        self.assertEqual(inst.intent.value, FHIRCode("instance-order").value)
        self.assertEqual(inst.intent.as_json(), "instance-order")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown("this is the right device brand and model").value)
        self.assertEqual(inst.note[0].text.as_json(), "this is the right device brand and model")
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime("2013-05-08T09:33:27+07:00").value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.performerType.coding[0].display.value, FHIRString("Qualified nurse").value)
        self.assertEqual(inst.performerType.coding[0].display.as_json(), "Qualified nurse")
        self.assertEqual(inst.performerType.text.value, FHIRString("Nurse").value)
        self.assertEqual(inst.performerType.text.as_json(), "Nurse")
        self.assertEqual(inst.priority.value, FHIRCode("routine").value)
        self.assertEqual(inst.priority.as_json(), "routine")
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString("gastroparesis").value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), "gastroparesis")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime, FHIRCanonical, FHIRMarkdown