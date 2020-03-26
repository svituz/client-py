#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import person

class PersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Person", js["resourceType"])
        return person.Person(js)

    def testPerson1(self):
        inst = self.instantiate_from('person-example-f002-ariadne.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Person instance')
        self.implPerson1(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson1(inst2)

    def implPerson1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.value, FHIRDate("1963").value)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(inst.birthDate.date, FHIRDate('1963').date)
        self.assertEqual(inst.gender.value, FHIRCode("female").value)
        self.assertEqual(inst.gender.as_json(), "female")
        self.assertEqual(inst.id.value, FHIRString("f002").value)
        self.assertEqual(inst.id.as_json(), "f002")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].text.value, FHIRString("Ariadne Bor-Jansma").value)
        self.assertEqual(inst.name[0].text.as_json(), "Ariadne Bor-Jansma")
        self.assertEqual(inst.name[0].use.value, FHIRCode("usual").value)
        self.assertEqual(inst.name[0].use.as_json(), "usual")
        self.assertEqual(inst.photo.contentType.value, FHIRCode("image/jpeg").value)
        self.assertEqual(inst.photo.contentType.as_json(), "image/jpeg")
        self.assertEqual(inst.telecom[0].system.value, FHIRCode("phone").value)
        self.assertEqual(inst.telecom[0].system.as_json(), "phone")
        self.assertEqual(inst.telecom[0].use.value, FHIRCode("home").value)
        self.assertEqual(inst.telecom[0].use.as_json(), "home")
        self.assertEqual(inst.telecom[0].value.value, FHIRString("+31201234567").value)
        self.assertEqual(inst.telecom[0].value.as_json(), "+31201234567")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testPerson2(self):
        inst = self.instantiate_from('person-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Person instance')
        self.implPerson2(inst)

        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson2(inst2)

    def implPerson2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city.value, FHIRString("PleasantVille").value)
        self.assertEqual(inst.address[0].city.as_json(), "PleasantVille")
        self.assertEqual(inst.address[0].line[0].value, FHIRString("534 Erewhon St").value)
        self.assertEqual(inst.address[0].line[0].as_json(), "534 Erewhon St")
        self.assertEqual(inst.address[0].postalCode.value, FHIRString("3999").value)
        self.assertEqual(inst.address[0].postalCode.as_json(), "3999")
        self.assertEqual(inst.address[0].state.value, FHIRString("Vic").value)
        self.assertEqual(inst.address[0].state.as_json(), "Vic")
        self.assertEqual(inst.address[0].use.value, FHIRCode("home").value)
        self.assertEqual(inst.address[0].use.as_json(), "home")
        self.assertEqual(inst.birthDate.value, FHIRDate("1974-12-25").value)
        self.assertEqual(inst.birthDate.as_json(), "1974-12-25")
        self.assertEqual(inst.birthDate.date, FHIRDate('1974-12-25').date)
        self.assertEqual(inst.gender.value, FHIRCode("male").value)
        self.assertEqual(inst.gender.as_json(), "male")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].period.start.value, FHIRDateTime("2001-05-06").value)
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2001-05-06")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:oid:1.2.36.146.595.217.0.1").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:oid:1.2.36.146.595.217.0.1")
        self.assertEqual(inst.identifier[0].type.coding[0].code.value, FHIRCode("MR").value)
        self.assertEqual(inst.identifier[0].type.coding[0].code.as_json(), "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v2-0203").value)
        self.assertEqual(inst.identifier[0].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("usual").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "usual")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family.value, FHIRString("Chalmers").value)
        self.assertEqual(inst.name[0].family.as_json(), "Chalmers")
        self.assertEqual(inst.name[0].given[0].value, FHIRString("Peter").value)
        self.assertEqual(inst.name[0].given[0].as_json(), "Peter")
        self.assertEqual(inst.name[0].given[1].value, FHIRString("James").value)
        self.assertEqual(inst.name[0].given[1].as_json(), "James")
        self.assertEqual(inst.name[0].use.value, FHIRCode("official").value)
        self.assertEqual(inst.name[0].use.as_json(), "official")
        self.assertEqual(inst.name[1].given[0].value, FHIRString("Jim").value)
        self.assertEqual(inst.name[1].given[0].as_json(), "Jim")
        self.assertEqual(inst.name[1].use.value, FHIRCode("usual").value)
        self.assertEqual(inst.name[1].use.as_json(), "usual")
        self.assertEqual(inst.telecom[0].use.value, FHIRCode("home").value)
        self.assertEqual(inst.telecom[0].use.as_json(), "home")
        self.assertEqual(inst.telecom[1].system.value, FHIRCode("phone").value)
        self.assertEqual(inst.telecom[1].system.as_json(), "phone")
        self.assertEqual(inst.telecom[1].use.value, FHIRCode("work").value)
        self.assertEqual(inst.telecom[1].use.as_json(), "work")
        self.assertEqual(inst.telecom[1].value.value, FHIRString("(03) 5555 6473").value)
        self.assertEqual(inst.telecom[1].value.as_json(), "(03) 5555 6473")
        self.assertEqual(inst.telecom[2].system.value, FHIRCode("email").value)
        self.assertEqual(inst.telecom[2].system.as_json(), "email")
        self.assertEqual(inst.telecom[2].use.value, FHIRCode("home").value)
        self.assertEqual(inst.telecom[2].use.as_json(), "home")
        self.assertEqual(inst.telecom[2].value.value, FHIRString("Jim@example.org").value)
        self.assertEqual(inst.telecom[2].value.as_json(), "Jim@example.org")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDate, FHIRCode, FHIRString, FHIRUri, FHIRDateTime