#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import episodeofcare

class EpisodeOfCareTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EpisodeOfCare", js["resourceType"])
        return episodeofcare.EpisodeOfCare(js)

    def testEpisodeOfCare1(self):
        inst = self.instantiate_from('episodeofcare-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a EpisodeOfCare instance')
        self.implEpisodeOfCare1(inst)

        js = inst.as_json()
        self.assertEqual("EpisodeOfCare", js["resourceType"])
        inst2 = episodeofcare.EpisodeOfCare(js)
        self.implEpisodeOfCare1(inst2)

    def implEpisodeOfCare1(self, inst):
        self.assertEqual(inst.diagnosis[0].rank.value, FHIRPositiveInt('1').value)
        self.assertEqual(inst.diagnosis[0].rank.as_json(), 1)
        self.assertEqual(inst.diagnosis[0].role.coding[0].code.value, FHIRCode("CC").value)
        self.assertEqual(inst.diagnosis[0].role.coding[0].code.as_json(), "CC")
        self.assertEqual(inst.diagnosis[0].role.coding[0].display.value, FHIRString("Chief complaint").value)
        self.assertEqual(inst.diagnosis[0].role.coding[0].display.as_json(), "Chief complaint")
        self.assertEqual(inst.diagnosis[0].role.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/diagnosis-role").value)
        self.assertEqual(inst.diagnosis[0].role.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/diagnosis-role")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/sampleepisodeofcare-identifier").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/sampleepisodeofcare-identifier")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("123").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "123")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2014-09-01").value)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.statusHistory[0].period.end.value, FHIRDateTime("2014-09-14").value)
        self.assertEqual(inst.statusHistory[0].period.end.as_json(), "2014-09-14")
        self.assertEqual(inst.statusHistory[0].period.start.value, FHIRDateTime("2014-09-01").value)
        self.assertEqual(inst.statusHistory[0].period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.statusHistory[0].status.value, FHIRCode("planned").value)
        self.assertEqual(inst.statusHistory[0].status.as_json(), "planned")
        self.assertEqual(inst.statusHistory[1].period.end.value, FHIRDateTime("2014-09-21").value)
        self.assertEqual(inst.statusHistory[1].period.end.as_json(), "2014-09-21")
        self.assertEqual(inst.statusHistory[1].period.start.value, FHIRDateTime("2014-09-15").value)
        self.assertEqual(inst.statusHistory[1].period.start.as_json(), "2014-09-15")
        self.assertEqual(inst.statusHistory[1].status.value, FHIRCode("active").value)
        self.assertEqual(inst.statusHistory[1].status.as_json(), "active")
        self.assertEqual(inst.statusHistory[2].period.end.value, FHIRDateTime("2014-09-24").value)
        self.assertEqual(inst.statusHistory[2].period.end.as_json(), "2014-09-24")
        self.assertEqual(inst.statusHistory[2].period.start.value, FHIRDateTime("2014-09-22").value)
        self.assertEqual(inst.statusHistory[2].period.start.as_json(), "2014-09-22")
        self.assertEqual(inst.statusHistory[2].status.value, FHIRCode("onhold").value)
        self.assertEqual(inst.statusHistory[2].status.as_json(), "onhold")
        self.assertEqual(inst.statusHistory[3].period.start.value, FHIRDateTime("2014-09-25").value)
        self.assertEqual(inst.statusHistory[3].period.start.as_json(), "2014-09-25")
        self.assertEqual(inst.statusHistory[3].status.value, FHIRCode("active").value)
        self.assertEqual(inst.statusHistory[3].status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type[0].coding[0].code.value, FHIRCode("hacc").value)
        self.assertEqual(inst.type[0].coding[0].code.as_json(), "hacc")
        self.assertEqual(inst.type[0].coding[0].display.value, FHIRString("Home and Community Care").value)
        self.assertEqual(inst.type[0].coding[0].display.as_json(), "Home and Community Care")
        self.assertEqual(inst.type[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/episodeofcare-type").value)
        self.assertEqual(inst.type[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/episodeofcare-type")


from fhirclient.models.fhirdatatypes import FHIRPositiveInt, FHIRCode, FHIRString, FHIRUri, FHIRDateTime