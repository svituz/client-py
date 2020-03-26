#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import coverageeligibilityrequest

class CoverageEligibilityRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        return coverageeligibilityrequest.CoverageEligibilityRequest(js)

    def testCoverageEligibilityRequest1(self):
        inst = self.instantiate_from('coverageeligibilityrequest-example-2.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CoverageEligibilityRequest instance')
        self.implCoverageEligibilityRequest1(inst)

        js = inst.as_json()
        self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(js)
        self.implCoverageEligibilityRequest1(inst2)

    def implCoverageEligibilityRequest1(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2014-08-16").value)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id.value, FHIRString("52346").value)
        self.assertEqual(inst.id.as_json(), "52346")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://happyvalley.com/coverageelegibilityrequest").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://happyvalley.com/coverageelegibilityrequest")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("52346").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "52346")
        self.assertEqual(inst.insurance[0].businessArrangement.value, FHIRString("NB8742").value)
        self.assertEqual(inst.insurance[0].businessArrangement.as_json(), "NB8742")
        self.assertEqual(inst.item[0].category.coding[0].code.value, FHIRCode("69").value)
        self.assertEqual(inst.item[0].category.coding[0].code.as_json(), "69")
        self.assertEqual(inst.item[0].category.coding[0].display.value, FHIRString("Maternity").value)
        self.assertEqual(inst.item[0].category.coding[0].display.as_json(), "Maternity")
        self.assertEqual(inst.item[0].category.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/ex-benefitcategory").value)
        self.assertEqual(inst.item[0].category.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code.value, FHIRCode("normal").value)
        self.assertEqual(inst.priority.coding[0].code.as_json(), "normal")
        self.assertEqual(inst.purpose[0].value, FHIRCode("validation").value)
        self.assertEqual(inst.purpose[0].as_json(), "validation")
        self.assertEqual(inst.purpose[1].value, FHIRCode("benefits").value)
        self.assertEqual(inst.purpose[1].as_json(), "benefits")
        self.assertEqual(inst.servicedDate.value, FHIRDate("2014-09-17").value)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(inst.servicedDate.date, FHIRDate('2014-09-17').date)
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testCoverageEligibilityRequest2(self):
        inst = self.instantiate_from('coverageeligibilityrequest-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CoverageEligibilityRequest instance')
        self.implCoverageEligibilityRequest2(inst)

        js = inst.as_json()
        self.assertEqual("CoverageEligibilityRequest", js["resourceType"])
        inst2 = coverageeligibilityrequest.CoverageEligibilityRequest(js)
        self.implCoverageEligibilityRequest2(inst2)

    def implCoverageEligibilityRequest2(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2014-08-16").value)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.id.value, FHIRString("52345").value)
        self.assertEqual(inst.id.as_json(), "52345")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://happyvalley.com/coverageelegibilityrequest").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://happyvalley.com/coverageelegibilityrequest")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("52345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "52345")
        self.assertTrue(inst.insurance[0].focal)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code.value, FHIRCode("normal").value)
        self.assertEqual(inst.priority.coding[0].code.as_json(), "normal")
        self.assertEqual(inst.purpose[0].value, FHIRCode("validation").value)
        self.assertEqual(inst.purpose[0].as_json(), "validation")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityRequest</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRString, FHIRUri, FHIRCode, FHIRDate