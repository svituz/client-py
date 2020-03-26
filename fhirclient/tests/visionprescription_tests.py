#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import visionprescription

class VisionPrescriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("VisionPrescription", js["resourceType"])
        return visionprescription.VisionPrescription(js)

    def testVisionPrescription1(self):
        inst = self.instantiate_from('visionprescription-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a VisionPrescription instance')
        self.implVisionPrescription1(inst)

        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription1(inst2)

    def implVisionPrescription1(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2014-06-15").value)
        self.assertEqual(inst.created.as_json(), "2014-06-15")
        self.assertEqual(inst.dateWritten.value, FHIRDateTime("2014-06-15").value)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.happysight.com/prescription").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("15013").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "15013")
        self.assertEqual(inst.lensSpecification[0].add, 2.0)
        self.assertEqual(inst.lensSpecification[0].eye.value, FHIRCode("right").value)
        self.assertEqual(inst.lensSpecification[0].eye.as_json(), "right")
        self.assertEqual(inst.lensSpecification[0].prism[0].amount, 0.5)
        self.assertEqual(inst.lensSpecification[0].prism[0].base.value, FHIRCode("down").value)
        self.assertEqual(inst.lensSpecification[0].prism[0].base.as_json(), "down")
        self.assertEqual(inst.lensSpecification[0].product.coding[0].code.value, FHIRCode("lens").value)
        self.assertEqual(inst.lensSpecification[0].product.coding[0].code.as_json(), "lens")
        self.assertEqual(inst.lensSpecification[0].product.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct").value)
        self.assertEqual(inst.lensSpecification[0].product.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.lensSpecification[0].sphere, -2.0)
        self.assertEqual(inst.lensSpecification[1].add, 2.0)
        self.assertEqual(inst.lensSpecification[1].axis, 180)
        self.assertEqual(inst.lensSpecification[1].cylinder, -0.5)
        self.assertEqual(inst.lensSpecification[1].eye.value, FHIRCode("left").value)
        self.assertEqual(inst.lensSpecification[1].eye.as_json(), "left")
        self.assertEqual(inst.lensSpecification[1].prism[0].amount, 0.5)
        self.assertEqual(inst.lensSpecification[1].prism[0].base.value, FHIRCode("up").value)
        self.assertEqual(inst.lensSpecification[1].prism[0].base.as_json(), "up")
        self.assertEqual(inst.lensSpecification[1].product.coding[0].code.value, FHIRCode("lens").value)
        self.assertEqual(inst.lensSpecification[1].product.coding[0].code.as_json(), "lens")
        self.assertEqual(inst.lensSpecification[1].product.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct").value)
        self.assertEqual(inst.lensSpecification[1].product.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.lensSpecification[1].sphere, -1.0)
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

    def testVisionPrescription2(self):
        inst = self.instantiate_from('visionprescription-example-1.json')
        self.assertIsNotNone(inst, 'Must have instantiated a VisionPrescription instance')
        self.implVisionPrescription2(inst)

        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription2(inst2)

    def implVisionPrescription2(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2014-06-15").value)
        self.assertEqual(inst.created.as_json(), "2014-06-15")
        self.assertEqual(inst.dateWritten.value, FHIRDateTime("2014-06-15").value)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.happysight.com/prescription").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("15014").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "15014")
        self.assertEqual(inst.lensSpecification[0].add, 1.75)
        self.assertEqual(inst.lensSpecification[0].axis, 160)
        self.assertEqual(inst.lensSpecification[0].backCurve, 8.7)
        self.assertEqual(inst.lensSpecification[0].brand.value, FHIRString("OphthaGuard").value)
        self.assertEqual(inst.lensSpecification[0].brand.as_json(), "OphthaGuard")
        self.assertEqual(inst.lensSpecification[0].color.value, FHIRString("green").value)
        self.assertEqual(inst.lensSpecification[0].color.as_json(), "green")
        self.assertEqual(inst.lensSpecification[0].cylinder, -2.25)
        self.assertEqual(inst.lensSpecification[0].diameter, 14.0)
        self.assertEqual(inst.lensSpecification[0].duration.code.value, FHIRCode("month").value)
        self.assertEqual(inst.lensSpecification[0].duration.code.as_json(), "month")
        self.assertEqual(inst.lensSpecification[0].duration.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.lensSpecification[0].duration.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.lensSpecification[0].duration.unit.value, FHIRString("month").value)
        self.assertEqual(inst.lensSpecification[0].duration.unit.as_json(), "month")
        self.assertEqual(inst.lensSpecification[0].duration.value, 1)
        self.assertEqual(inst.lensSpecification[0].eye.value, FHIRCode("right").value)
        self.assertEqual(inst.lensSpecification[0].eye.as_json(), "right")
        self.assertEqual(inst.lensSpecification[0].note[0].text.value, FHIRMarkdown("Shade treatment for extreme light sensitivity").value)
        self.assertEqual(inst.lensSpecification[0].note[0].text.as_json(), "Shade treatment for extreme light sensitivity")
        self.assertEqual(inst.lensSpecification[0].power, -2.75)
        self.assertEqual(inst.lensSpecification[0].product.coding[0].code.value, FHIRCode("contact").value)
        self.assertEqual(inst.lensSpecification[0].product.coding[0].code.as_json(), "contact")
        self.assertEqual(inst.lensSpecification[0].product.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct").value)
        self.assertEqual(inst.lensSpecification[0].product.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.lensSpecification[1].add, 1.75)
        self.assertEqual(inst.lensSpecification[1].axis, 160)
        self.assertEqual(inst.lensSpecification[1].backCurve, 8.7)
        self.assertEqual(inst.lensSpecification[1].brand.value, FHIRString("OphthaGuard").value)
        self.assertEqual(inst.lensSpecification[1].brand.as_json(), "OphthaGuard")
        self.assertEqual(inst.lensSpecification[1].color.value, FHIRString("green").value)
        self.assertEqual(inst.lensSpecification[1].color.as_json(), "green")
        self.assertEqual(inst.lensSpecification[1].cylinder, -3.5)
        self.assertEqual(inst.lensSpecification[1].diameter, 14.0)
        self.assertEqual(inst.lensSpecification[1].duration.code.value, FHIRCode("month").value)
        self.assertEqual(inst.lensSpecification[1].duration.code.as_json(), "month")
        self.assertEqual(inst.lensSpecification[1].duration.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.lensSpecification[1].duration.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.lensSpecification[1].duration.unit.value, FHIRString("month").value)
        self.assertEqual(inst.lensSpecification[1].duration.unit.as_json(), "month")
        self.assertEqual(inst.lensSpecification[1].duration.value, 1)
        self.assertEqual(inst.lensSpecification[1].eye.value, FHIRCode("left").value)
        self.assertEqual(inst.lensSpecification[1].eye.as_json(), "left")
        self.assertEqual(inst.lensSpecification[1].note[0].text.value, FHIRMarkdown("Shade treatment for extreme light sensitivity").value)
        self.assertEqual(inst.lensSpecification[1].note[0].text.as_json(), "Shade treatment for extreme light sensitivity")
        self.assertEqual(inst.lensSpecification[1].power, -2.75)
        self.assertEqual(inst.lensSpecification[1].product.coding[0].code.value, FHIRCode("contact").value)
        self.assertEqual(inst.lensSpecification[1].product.coding[0].code.as_json(), "contact")
        self.assertEqual(inst.lensSpecification[1].product.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct").value)
        self.assertEqual(inst.lensSpecification[1].product.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Sample Contract Lens prescription</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Sample Contract Lens prescription</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRUri, FHIRString, FHIRCode, FHIRMarkdown