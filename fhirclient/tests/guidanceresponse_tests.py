#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import guidanceresponse

class GuidanceResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("GuidanceResponse", js["resourceType"])
        return guidanceresponse.GuidanceResponse(js)

    def testGuidanceResponse1(self):
        inst = self.instantiate_from('guidanceresponse-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a GuidanceResponse instance')
        self.implGuidanceResponse1(inst)

        js = inst.as_json()
        self.assertEqual("GuidanceResponse", js["resourceType"])
        inst2 = guidanceresponse.GuidanceResponse(js)
        self.implGuidanceResponse1(inst2)

    def implGuidanceResponse1(self, inst):
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("guidanceResponse1").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "guidanceResponse1")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.moduleUri.value, FHIRUri("http://someguidelineprovider.org/radiology-appropriateness-guidelines.html").value)
        self.assertEqual(inst.moduleUri.as_json(), "http://someguidelineprovider.org/radiology-appropriateness-guidelines.html")
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime("2017-03-10T16:02:00Z").value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2017-03-10T16:02:00Z")
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString("Guideline Appropriate Ordering Assessment").value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), "Guideline Appropriate Ordering Assessment")
        self.assertEqual(inst.requestIdentifier.system.value, FHIRUri("http://example.org").value)
        self.assertEqual(inst.requestIdentifier.system.as_json(), "http://example.org")
        self.assertEqual(inst.requestIdentifier.value.value, FHIRString("guidanceRequest1").value)
        self.assertEqual(inst.requestIdentifier.value.as_json(), "guidanceRequest1")
        self.assertEqual(inst.status.value, FHIRCode("success").value)
        self.assertEqual(inst.status.as_json(), "success")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRUri, FHIRString, FHIRCode, FHIRDateTime