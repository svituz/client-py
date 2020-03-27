#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import careteam

class CareTeamTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CareTeam", js["resourceType"])
        return careteam.CareTeam(js)

    def testCareTeam1(self):
        inst = self.instantiate_from('careteam-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CareTeam instance')
        self.implCareTeam1(inst)

        js = inst.as_json()
        self.assertEqual("CareTeam", js["resourceType"])
        inst2 = careteam.CareTeam(js)
        self.implCareTeam1(inst2)

    def implCareTeam1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("LA27976-2").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "LA27976-2")
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString("Encounter-focused care team").value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), "Encounter-focused care team")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.contained[0].id.value, FHIRString("pr1").value)
        self.assertEqual(inst.contained[0].id.as_json(), "pr1")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("Peter James Charlmers Care Plan for Inpatient Encounter").value)
        self.assertEqual(inst.name.as_json(), "Peter James Charlmers Care Plan for Inpatient Encounter")
        self.assertEqual(inst.participant[0].role[0].text.value, FHIRString("responsiblePerson").value)
        self.assertEqual(inst.participant[0].role[0].text.as_json(), "responsiblePerson")
        self.assertEqual(inst.participant[1].period.end.value, FHIRDateTime("2013-01-01").value)
        self.assertEqual(inst.participant[1].period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.participant[1].role[0].text.value, FHIRString("adviser").value)
        self.assertEqual(inst.participant[1].role[0].text.as_json(), "adviser")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2013-01-01").value)
        self.assertEqual(inst.period.end.as_json(), "2013-01-01")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Care Team</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Care Team</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime