#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import biologicallyderivedproduct

class BiologicallyDerivedProductTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BiologicallyDerivedProduct", js["resourceType"])
        return biologicallyderivedproduct.BiologicallyDerivedProduct(js)

    def testBiologicallyDerivedProduct1(self):
        inst = self.instantiate_from('biologicallyderivedproduct-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a BiologicallyDerivedProduct instance')
        self.implBiologicallyDerivedProduct1(inst)

        js = inst.as_json()
        self.assertEqual("BiologicallyDerivedProduct", js["resourceType"])
        inst2 = biologicallyderivedproduct.BiologicallyDerivedProduct(js)
        self.implBiologicallyDerivedProduct1(inst2)

    def implBiologicallyDerivedProduct1(self, inst):
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri