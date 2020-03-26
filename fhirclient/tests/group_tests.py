#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import group

class GroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Group", js["resourceType"])
        return group.Group(js)

    def testGroup1(self):
        inst = self.instantiate_from('group-example-herd1.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Group instance')
        self.implGroup1(inst)

        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup1(inst2)

    def implGroup1(self, inst):
        self.assertTrue(inst.active)
        self.assertTrue(inst.actual)
        self.assertEqual(inst.characteristic[0].code.text.value, FHIRString("gender").value)
        self.assertEqual(inst.characteristic[0].code.text.as_json(), "gender")
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(inst.characteristic[0].valueCodeableConcept.text.value, FHIRString("female").value)
        self.assertEqual(inst.characteristic[0].valueCodeableConcept.text.as_json(), "female")
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("388393002").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "388393002")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Genus Sus (organism)").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Genus Sus (organism)")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.code.coding[1].code.value, FHIRCode("POR").value)
        self.assertEqual(inst.code.coding[1].code.as_json(), "POR")
        self.assertEqual(inst.code.coding[1].display.value, FHIRString("porcine").value)
        self.assertEqual(inst.code.coding[1].display.as_json(), "porcine")
        self.assertEqual(inst.code.coding[1].system.value, FHIRUri("https://www.aphis.usda.gov").value)
        self.assertEqual(inst.code.coding[1].system.as_json(), "https://www.aphis.usda.gov")
        self.assertEqual(inst.code.text.value, FHIRString("Porcine").value)
        self.assertEqual(inst.code.text.as_json(), "Porcine")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("https://vetmed.iastate.edu/vdl").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "https://vetmed.iastate.edu/vdl")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("20171120-1234").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "20171120-1234")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("Breeding herd").value)
        self.assertEqual(inst.name.as_json(), "Breeding herd")
        self.assertEqual(inst.quantity.value, FHIRUnsignedInt('2500').value)
        self.assertEqual(inst.quantity.as_json(), 2500)
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.value, FHIRCode("animal").value)
        self.assertEqual(inst.type.as_json(), "animal")

    def testGroup2(self):
        inst = self.instantiate_from('group-example-member.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Group instance')
        self.implGroup2(inst)

        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup2(inst2)

    def implGroup2(self, inst):
        self.assertTrue(inst.actual)
        self.assertEqual(inst.member[0].period.start.value, FHIRDateTime("2014-10-08").value)
        self.assertEqual(inst.member[0].period.start.as_json(), "2014-10-08")
        self.assertTrue(inst.member[1].inactive)
        self.assertEqual(inst.member[1].period.start.value, FHIRDateTime("2015-04-02").value)
        self.assertEqual(inst.member[1].period.start.as_json(), "2015-04-02")
        self.assertEqual(inst.member[2].period.start.value, FHIRDateTime("2015-08-06").value)
        self.assertEqual(inst.member[2].period.start.as_json(), "2015-08-06")
        self.assertEqual(inst.member[3].period.start.value, FHIRDateTime("2015-08-06").value)
        self.assertEqual(inst.member[3].period.start.as_json(), "2015-08-06")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("additional").value)
        self.assertEqual(inst.text.status.as_json(), "additional")
        self.assertEqual(inst.type.value, FHIRCode("person").value)
        self.assertEqual(inst.type.as_json(), "person")

    def testGroup3(self):
        inst = self.instantiate_from('group-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Group instance')
        self.implGroup3(inst)

        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup3(inst2)

    def implGroup3(self, inst):
        self.assertTrue(inst.actual)
        self.assertEqual(inst.characteristic[0].code.text.value, FHIRString("gender").value)
        self.assertEqual(inst.characteristic[0].code.text.as_json(), "gender")
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(inst.characteristic[0].valueCodeableConcept.text.value, FHIRString("mixed").value)
        self.assertEqual(inst.characteristic[0].valueCodeableConcept.text.as_json(), "mixed")
        self.assertEqual(inst.characteristic[1].code.text.value, FHIRString("owner").value)
        self.assertEqual(inst.characteristic[1].code.text.as_json(), "owner")
        self.assertFalse(inst.characteristic[1].exclude)
        self.assertEqual(inst.characteristic[1].valueCodeableConcept.text.value, FHIRString("John Smith").value)
        self.assertEqual(inst.characteristic[1].valueCodeableConcept.text.as_json(), "John Smith")
        self.assertEqual(inst.code.text.value, FHIRString("Horse").value)
        self.assertEqual(inst.code.text.as_json(), "Horse")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://someveterinarianclinic.org/fhir/NamingSystem/herds").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://someveterinarianclinic.org/fhir/NamingSystem/herds")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("John's herd").value)
        self.assertEqual(inst.name.as_json(), "John's herd")
        self.assertEqual(inst.quantity.value, FHIRUnsignedInt('25').value)
        self.assertEqual(inst.quantity.as_json(), 25)
        self.assertEqual(inst.text.status.value, FHIRCode("additional").value)
        self.assertEqual(inst.text.status.as_json(), "additional")
        self.assertEqual(inst.type.value, FHIRCode("animal").value)
        self.assertEqual(inst.type.as_json(), "animal")

    def testGroup4(self):
        inst = self.instantiate_from('group-example-patientlist.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Group instance')
        self.implGroup4(inst)

        js = inst.as_json()
        self.assertEqual("Group", js["resourceType"])
        inst2 = group.Group(js)
        self.implGroup4(inst2)

    def implGroup4(self, inst):
        self.assertTrue(inst.actual)
        self.assertEqual(inst.characteristic[0].code.coding[0].code.value, FHIRCode("attributed-to").value)
        self.assertEqual(inst.characteristic[0].code.coding[0].code.as_json(), "attributed-to")
        self.assertEqual(inst.characteristic[0].code.coding[0].system.value, FHIRUri("http://example.org").value)
        self.assertEqual(inst.characteristic[0].code.coding[0].system.as_json(), "http://example.org")
        self.assertEqual(inst.characteristic[0].code.text.value, FHIRString("Patients primarily attributed to").value)
        self.assertEqual(inst.characteristic[0].code.text.as_json(), "Patients primarily attributed to")
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("additional").value)
        self.assertEqual(inst.text.status.as_json(), "additional")
        self.assertEqual(inst.type.value, FHIRCode("person").value)
        self.assertEqual(inst.type.as_json(), "person")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri, FHIRUnsignedInt, FHIRDateTime