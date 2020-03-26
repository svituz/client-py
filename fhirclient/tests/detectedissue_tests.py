#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import detectedissue

class DetectedIssueTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DetectedIssue", js["resourceType"])
        return detectedissue.DetectedIssue(js)

    def testDetectedIssue1(self):
        inst = self.instantiate_from('detectedissue-example-lab.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DetectedIssue instance')
        self.implDetectedIssue1(inst)

        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue1(inst2)

    def implDetectedIssue1(self, inst):
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("final").value)
        self.assertEqual(inst.status.as_json(), "final")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testDetectedIssue2(self):
        inst = self.instantiate_from('detectedissue-example-dup.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DetectedIssue instance')
        self.implDetectedIssue2(inst)

        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue2(inst2)

    def implDetectedIssue2(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("DUPTHPY").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "DUPTHPY")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Duplicate Therapy Alert").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Duplicate Therapy Alert")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.detail.value, FHIRString("Similar test was performed within the past 14 days").value)
        self.assertEqual(inst.detail.as_json(), "Similar test was performed within the past 14 days")
        self.assertEqual(inst.identifiedDateTime.value, FHIRDateTime("2013-05-08").value)
        self.assertEqual(inst.identifiedDateTime.as_json(), "2013-05-08")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("official").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "official")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reference.value, FHIRUri("http://www.tmhp.com/RadiologyClinicalDecisionSupport/2011/CHEST%20IMAGING%20GUIDELINES%202011.pdf").value)
        self.assertEqual(inst.reference.as_json(), "http://www.tmhp.com/RadiologyClinicalDecisionSupport/2011/CHEST%20IMAGING%20GUIDELINES%202011.pdf")
        self.assertEqual(inst.status.value, FHIRCode("final").value)
        self.assertEqual(inst.status.as_json(), "final")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testDetectedIssue3(self):
        inst = self.instantiate_from('detectedissue-example-allergy.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DetectedIssue instance')
        self.implDetectedIssue3(inst)

        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue3(inst2)

    def implDetectedIssue3(self, inst):
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("final").value)
        self.assertEqual(inst.status.as_json(), "final")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testDetectedIssue4(self):
        inst = self.instantiate_from('detectedissue-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DetectedIssue instance')
        self.implDetectedIssue4(inst)

        js = inst.as_json()
        self.assertEqual("DetectedIssue", js["resourceType"])
        inst2 = detectedissue.DetectedIssue(js)
        self.implDetectedIssue4(inst2)

    def implDetectedIssue4(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("DRG").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "DRG")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Drug Interaction Alert").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Drug Interaction Alert")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.identifiedDateTime.value, FHIRDateTime("2014-01-05").value)
        self.assertEqual(inst.identifiedDateTime.as_json(), "2014-01-05")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mitigation[0].action.coding[0].code.value, FHIRCode("13").value)
        self.assertEqual(inst.mitigation[0].action.coding[0].code.as_json(), "13")
        self.assertEqual(inst.mitigation[0].action.coding[0].display.value, FHIRString("Stopped Concurrent Therapy").value)
        self.assertEqual(inst.mitigation[0].action.coding[0].display.as_json(), "Stopped Concurrent Therapy")
        self.assertEqual(inst.mitigation[0].action.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.mitigation[0].action.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.mitigation[0].action.text.value, FHIRString("Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring").value)
        self.assertEqual(inst.mitigation[0].action.text.as_json(), "Asked patient to discontinue regular use of Tylenol and to consult with clinician if they need to resume to allow appropriate INR monitoring")
        self.assertEqual(inst.mitigation[0].date.value, FHIRDateTime("2014-01-05").value)
        self.assertEqual(inst.mitigation[0].date.as_json(), "2014-01-05")
        self.assertEqual(inst.severity.value, FHIRCode("high").value)
        self.assertEqual(inst.severity.as_json(), "high")
        self.assertEqual(inst.status.value, FHIRCode("final").value)
        self.assertEqual(inst.status.as_json(), "final")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime