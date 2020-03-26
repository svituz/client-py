#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import list

class ListTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("List", js["resourceType"])
        return list.List(js)

    def testList1(self):
        inst = self.instantiate_from('list-example-familyhistory-genetics-profile.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList1(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList1(inst2)

    def implList1(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("8670-2").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "8670-2")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("History of family member diseases").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.contained[0].id.value, FHIRString("1").value)
        self.assertEqual(inst.contained[0].id.as_json(), "1")
        self.assertEqual(inst.contained[1].id.value, FHIRString("2").value)
        self.assertEqual(inst.contained[1].id.as_json(), "2")
        self.assertEqual(inst.contained[2].id.value, FHIRString("3").value)
        self.assertEqual(inst.contained[2].id.as_json(), "3")
        self.assertEqual(inst.contained[3].id.value, FHIRString("4").value)
        self.assertEqual(inst.contained[3].id.as_json(), "4")
        self.assertEqual(inst.contained[4].id.value, FHIRString("5").value)
        self.assertEqual(inst.contained[4].id.as_json(), "5")
        self.assertEqual(inst.contained[5].id.value, FHIRString("6").value)
        self.assertEqual(inst.contained[5].id.as_json(), "6")
        self.assertEqual(inst.contained[6].id.value, FHIRString("7").value)
        self.assertEqual(inst.contained[6].id.as_json(), "7")
        self.assertEqual(inst.contained[7].id.value, FHIRString("8").value)
        self.assertEqual(inst.contained[7].id.as_json(), "8")
        self.assertEqual(inst.id.value, FHIRString("genetic").value)
        self.assertEqual(inst.id.as_json(), "genetic")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("snapshot").value)
        self.assertEqual(inst.mode.as_json(), "snapshot")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList2(self):
        inst = self.instantiate_from('list-example-double-cousin-relationship-pedigree.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList2(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList2(inst2)

    def implList2(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("80738-8").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "80738-8")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.code.text.value, FHIRString("TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal").value)
        self.assertEqual(inst.code.text.as_json(), "TPMT gene mutations found [Identifier] in Blood or Tissue by Sequencing Nominal")
        self.assertEqual(inst.contained[0].id.value, FHIRString("1").value)
        self.assertEqual(inst.contained[0].id.as_json(), "1")
        self.assertEqual(inst.contained[1].id.value, FHIRString("2").value)
        self.assertEqual(inst.contained[1].id.as_json(), "2")
        self.assertEqual(inst.contained[2].id.value, FHIRString("3").value)
        self.assertEqual(inst.contained[2].id.as_json(), "3")
        self.assertEqual(inst.contained[3].id.value, FHIRString("4").value)
        self.assertEqual(inst.contained[3].id.as_json(), "4")
        self.assertEqual(inst.contained[4].id.value, FHIRString("5").value)
        self.assertEqual(inst.contained[4].id.as_json(), "5")
        self.assertEqual(inst.contained[5].id.value, FHIRString("6").value)
        self.assertEqual(inst.contained[5].id.as_json(), "6")
        self.assertEqual(inst.id.value, FHIRString("example-double-cousin-relationship").value)
        self.assertEqual(inst.id.as_json(), "example-double-cousin-relationship")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("snapshot").value)
        self.assertEqual(inst.mode.as_json(), "snapshot")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList3(self):
        inst = self.instantiate_from('list-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList3(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList3(inst2)

    def implList3(self, inst):
        self.assertEqual(inst.date.value, FHIRDateTime("2012-11-25T22:17:00+11:00").value)
        self.assertEqual(inst.date.as_json(), "2012-11-25T22:17:00+11:00")
        self.assertTrue(inst.entry[0].deleted)
        self.assertEqual(inst.entry[0].flag.text.value, FHIRString("Deleted due to error").value)
        self.assertEqual(inst.entry[0].flag.text.as_json(), "Deleted due to error")
        self.assertEqual(inst.entry[1].flag.text.value, FHIRString("Added").value)
        self.assertEqual(inst.entry[1].flag.text.as_json(), "Added")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:uuid:a9fcea7c-fcdf-4d17-a5e0-f26dda030b59")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("23974652").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "23974652")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("changes").value)
        self.assertEqual(inst.mode.as_json(), "changes")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList4(self):
        inst = self.instantiate_from('list-example-familyhistory-f201-roel.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList4(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList4(inst2)

    def implList4(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("8670-2").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "8670-2")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("History of family member diseases").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.contained[0].id.value, FHIRString("fmh-1").value)
        self.assertEqual(inst.contained[0].id.as_json(), "fmh-1")
        self.assertEqual(inst.contained[1].id.value, FHIRString("fmh-2").value)
        self.assertEqual(inst.contained[1].id.as_json(), "fmh-2")
        self.assertEqual(inst.id.value, FHIRString("f201").value)
        self.assertEqual(inst.id.as_json(), "f201")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("snapshot").value)
        self.assertEqual(inst.mode.as_json(), "snapshot")
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown("Both parents, both brothers and both children (twin) are still alive.").value)
        self.assertEqual(inst.note[0].text.as_json(), "Both parents, both brothers and both children (twin) are still alive.")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList5(self):
        inst = self.instantiate_from('list-example-familyhistory-genetics-profile-annie.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList5(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList5(inst2)

    def implList5(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("8670-2").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "8670-2")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("History of family member diseases").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "History of family member diseases")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.contained[0].id.value, FHIRString("image").value)
        self.assertEqual(inst.contained[0].id.as_json(), "image")
        self.assertEqual(inst.contained[1].id.value, FHIRString("1").value)
        self.assertEqual(inst.contained[1].id.as_json(), "1")
        self.assertEqual(inst.contained[2].id.value, FHIRString("2").value)
        self.assertEqual(inst.contained[2].id.as_json(), "2")
        self.assertEqual(inst.contained[3].id.value, FHIRString("3").value)
        self.assertEqual(inst.contained[3].id.as_json(), "3")
        self.assertEqual(inst.contained[4].id.value, FHIRString("4").value)
        self.assertEqual(inst.contained[4].id.as_json(), "4")
        self.assertEqual(inst.contained[5].id.value, FHIRString("5").value)
        self.assertEqual(inst.contained[5].id.as_json(), "5")
        self.assertEqual(inst.contained[6].id.value, FHIRString("6").value)
        self.assertEqual(inst.contained[6].id.as_json(), "6")
        self.assertEqual(inst.contained[7].id.value, FHIRString("7").value)
        self.assertEqual(inst.contained[7].id.as_json(), "7")
        self.assertEqual(inst.contained[8].id.value, FHIRString("8").value)
        self.assertEqual(inst.contained[8].id.as_json(), "8")
        self.assertEqual(inst.contained[9].id.value, FHIRString("9").value)
        self.assertEqual(inst.contained[9].id.as_json(), "9")
        self.assertEqual(inst.id.value, FHIRString("prognosis").value)
        self.assertEqual(inst.id.as_json(), "prognosis")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("snapshot").value)
        self.assertEqual(inst.mode.as_json(), "snapshot")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList6(self):
        inst = self.instantiate_from('list-example-empty.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList6(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList6(inst2)

    def implList6(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("182836005").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "182836005")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Review of medication").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Review of medication")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.code.text.value, FHIRString("Medication Review").value)
        self.assertEqual(inst.code.text.as_json(), "Medication Review")
        self.assertEqual(inst.date.value, FHIRDateTime("2012-11-26T07:30:23+11:00").value)
        self.assertEqual(inst.date.as_json(), "2012-11-26T07:30:23+11:00")
        self.assertEqual(inst.emptyReason.coding[0].code.value, FHIRCode("nilknown").value)
        self.assertEqual(inst.emptyReason.coding[0].code.as_json(), "nilknown")
        self.assertEqual(inst.emptyReason.coding[0].display.value, FHIRString("Nil Known").value)
        self.assertEqual(inst.emptyReason.coding[0].display.as_json(), "Nil Known")
        self.assertEqual(inst.emptyReason.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/list-empty-reason").value)
        self.assertEqual(inst.emptyReason.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/list-empty-reason")
        self.assertEqual(inst.emptyReason.text.value, FHIRString("The patient is not on any medications").value)
        self.assertEqual(inst.emptyReason.text.as_json(), "The patient is not on any medications")
        self.assertEqual(inst.id.value, FHIRString("example-empty").value)
        self.assertEqual(inst.id.as_json(), "example-empty")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("snapshot").value)
        self.assertEqual(inst.mode.as_json(), "snapshot")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList7(self):
        inst = self.instantiate_from('list-example-allergies.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList7(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList7(inst2)

    def implList7(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("52472-8").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "52472-8")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Allergies and Adverse Drug Reactions").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Allergies and Adverse Drug Reactions")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.code.text.value, FHIRString("Current Allergy List").value)
        self.assertEqual(inst.code.text.as_json(), "Current Allergy List")
        self.assertEqual(inst.date.value, FHIRDateTime("2015-07-14T23:10:23+11:00").value)
        self.assertEqual(inst.date.as_json(), "2015-07-14T23:10:23+11:00")
        self.assertEqual(inst.id.value, FHIRString("current-allergies").value)
        self.assertEqual(inst.id.as_json(), "current-allergies")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("working").value)
        self.assertEqual(inst.mode.as_json(), "working")
        self.assertEqual(inst.orderedBy.coding[0].code.value, FHIRCode("entry-date").value)
        self.assertEqual(inst.orderedBy.coding[0].code.as_json(), "entry-date")
        self.assertEqual(inst.orderedBy.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/list-order").value)
        self.assertEqual(inst.orderedBy.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/list-order")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Current Allergy List").value)
        self.assertEqual(inst.title.as_json(), "Current Allergy List")

    def testList8(self):
        inst = self.instantiate_from('list-example-medlist.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList8(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList8(inst2)

    def implList8(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("182836005").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "182836005")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Review of medication").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Review of medication")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.code.text.value, FHIRString("Medication Review").value)
        self.assertEqual(inst.code.text.as_json(), "Medication Review")
        self.assertEqual(inst.date.value, FHIRDateTime("2013-11-20T23:10:23+11:00").value)
        self.assertEqual(inst.date.as_json(), "2013-11-20T23:10:23+11:00")
        self.assertEqual(inst.entry[0].flag.coding[0].code.value, FHIRCode("01").value)
        self.assertEqual(inst.entry[0].flag.coding[0].code.as_json(), "01")
        self.assertEqual(inst.entry[0].flag.coding[0].display.value, FHIRString("Prescribed").value)
        self.assertEqual(inst.entry[0].flag.coding[0].display.as_json(), "Prescribed")
        self.assertEqual(inst.entry[0].flag.coding[0].system.value, FHIRUri("http://nehta.gov.au/codes/medications/changetype").value)
        self.assertEqual(inst.entry[0].flag.coding[0].system.as_json(), "http://nehta.gov.au/codes/medications/changetype")
        self.assertTrue(inst.entry[1].deleted)
        self.assertEqual(inst.entry[1].flag.coding[0].code.value, FHIRCode("02").value)
        self.assertEqual(inst.entry[1].flag.coding[0].code.as_json(), "02")
        self.assertEqual(inst.entry[1].flag.coding[0].display.value, FHIRString("Cancelled").value)
        self.assertEqual(inst.entry[1].flag.coding[0].display.as_json(), "Cancelled")
        self.assertEqual(inst.entry[1].flag.coding[0].system.value, FHIRUri("http://nehta.gov.au/codes/medications/changetype").value)
        self.assertEqual(inst.entry[1].flag.coding[0].system.as_json(), "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.id.value, FHIRString("med-list").value)
        self.assertEqual(inst.id.as_json(), "med-list")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("changes").value)
        self.assertEqual(inst.mode.as_json(), "changes")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList9(self):
        inst = self.instantiate_from('list-example-simple-empty.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList9(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList9(inst2)

    def implList9(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("346638").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "346638")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Patient Admission List").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Patient Admission List")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://acme.com/list-codes").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://acme.com/list-codes")
        self.assertEqual(inst.date.value, FHIRDateTime("2016-07-14T11:54:05+10:00").value)
        self.assertEqual(inst.date.as_json(), "2016-07-14T11:54:05+10:00")
        self.assertEqual(inst.id.value, FHIRString("example-simple-empty").value)
        self.assertEqual(inst.id.as_json(), "example-simple-empty")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("snapshot").value)
        self.assertEqual(inst.mode.as_json(), "snapshot")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testList10(self):
        inst = self.instantiate_from('list-example-long.json')
        self.assertIsNotNone(inst, 'Must have instantiated a List instance')
        self.implList10(inst)

        js = inst.as_json()
        self.assertEqual("List", js["resourceType"])
        inst2 = list.List(js)
        self.implList10(inst2)

    def implList10(self, inst):
        self.assertEqual(inst.date.value, FHIRDateTime("2018-02-21T12:17:00+11:00").value)
        self.assertEqual(inst.date.as_json(), "2018-02-21T12:17:00+11:00")
        self.assertEqual(inst.id.value, FHIRString("long").value)
        self.assertEqual(inst.id.as_json(), "long")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode.value, FHIRCode("changes").value)
        self.assertEqual(inst.mode.as_json(), "changes")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime, FHIRMarkdown