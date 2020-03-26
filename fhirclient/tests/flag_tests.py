#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import flag

class FlagTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Flag", js["resourceType"])
        return flag.Flag(js)

    def testFlag1(self):
        inst = self.instantiate_from('flag-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Flag instance')
        self.implFlag1(inst)

        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag1(inst2)

    def implFlag1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("safety").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "safety")
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString("Safety").value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), "Safety")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/flag-category").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/flag-category")
        self.assertEqual(inst.category[0].text.value, FHIRString("Safety").value)
        self.assertEqual(inst.category[0].text.as_json(), "Safety")
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("bigdog").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "bigdog")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Big dog").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Big dog")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://example.org/local").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://example.org/local")
        self.assertEqual(inst.code.text.value, FHIRString("Patient has a big dog at his home. Always always wear a suit of armor or take other active counter-measures").value)
        self.assertEqual(inst.code.text.as_json(), "Patient has a big dog at his home. Always always wear a suit of armor or take other active counter-measures")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2016-12-01").value)
        self.assertEqual(inst.period.end.as_json(), "2016-12-01")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2015-01-17").value)
        self.assertEqual(inst.period.start.as_json(), "2015-01-17")
        self.assertEqual(inst.status.value, FHIRCode("inactive").value)
        self.assertEqual(inst.status.as_json(), "inactive")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Large Dog warning for Peter Patient</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Large Dog warning for Peter Patient</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testFlag2(self):
        inst = self.instantiate_from('flag-example-encounter.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Flag instance')
        self.implFlag2(inst)

        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag2(inst2)

    def implFlag2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("infection").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "infection")
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString("Infection Control Level").value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), "Infection Control Level")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://example.org/local").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://example.org/local")
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("l3").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "l3")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Follow Level 3 Protocol").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Follow Level 3 Protocol")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://example.org/local/if1").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://example.org/local/if1")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Follow Infection Control Level 3 Protocol</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Follow Infection Control Level 3 Protocol</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime