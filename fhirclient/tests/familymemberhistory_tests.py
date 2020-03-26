#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import familymemberhistory

class FamilyMemberHistoryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("FamilyMemberHistory", js["resourceType"])
        return familymemberhistory.FamilyMemberHistory(js)

    def testFamilyMemberHistory1(self):
        inst = self.instantiate_from('familymemberhistory-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a FamilyMemberHistory instance')
        self.implFamilyMemberHistory1(inst)

        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory1(inst2)

    def implFamilyMemberHistory1(self, inst):
        self.assertEqual(inst.condition[0].code.coding[0].code.value, FHIRCode("315619001").value)
        self.assertEqual(inst.condition[0].code.coding[0].code.as_json(), "315619001")
        self.assertEqual(inst.condition[0].code.coding[0].display.value, FHIRString("Myocardial Infarction").value)
        self.assertEqual(inst.condition[0].code.coding[0].display.as_json(), "Myocardial Infarction")
        self.assertEqual(inst.condition[0].code.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.condition[0].code.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.condition[0].code.text.value, FHIRString("Heart Attack").value)
        self.assertEqual(inst.condition[0].code.text.as_json(), "Heart Attack")
        self.assertTrue(inst.condition[0].contributedToDeath)
        self.assertEqual(inst.condition[0].note[0].text.value, FHIRMarkdown("Was fishing at the time. At least he went doing someting he loved.").value)
        self.assertEqual(inst.condition[0].note[0].text.as_json(), "Was fishing at the time. At least he went doing someting he loved.")
        self.assertEqual(inst.condition[0].onsetAge.code.value, FHIRCode("a").value)
        self.assertEqual(inst.condition[0].onsetAge.code.as_json(), "a")
        self.assertEqual(inst.condition[0].onsetAge.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.condition[0].onsetAge.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.condition[0].onsetAge.unit.value, FHIRString("yr").value)
        self.assertEqual(inst.condition[0].onsetAge.unit.as_json(), "yr")
        self.assertEqual(inst.condition[0].onsetAge.value, 74)
        self.assertEqual(inst.date.value, FHIRDateTime("2011-03-18").value)
        self.assertEqual(inst.date.as_json(), "2011-03-18")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.instantiatesUri[0].value, FHIRUri("http://example.org/family-member-history-questionnaire").value)
        self.assertEqual(inst.instantiatesUri[0].as_json(), "http://example.org/family-member-history-questionnaire")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relationship.coding[0].code.value, FHIRCode("FTH").value)
        self.assertEqual(inst.relationship.coding[0].code.as_json(), "FTH")
        self.assertEqual(inst.relationship.coding[0].display.value, FHIRString("father").value)
        self.assertEqual(inst.relationship.coding[0].display.as_json(), "father")
        self.assertEqual(inst.relationship.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-RoleCode").value)
        self.assertEqual(inst.relationship.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.sex.coding[0].code.value, FHIRCode("male").value)
        self.assertEqual(inst.sex.coding[0].code.as_json(), "male")
        self.assertEqual(inst.sex.coding[0].display.value, FHIRString("Male").value)
        self.assertEqual(inst.sex.coding[0].display.as_json(), "Male")
        self.assertEqual(inst.sex.coding[0].system.value, FHIRUri("http://hl7.org/fhir/administrative-gender").value)
        self.assertEqual(inst.sex.coding[0].system.as_json(), "http://hl7.org/fhir/administrative-gender")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Father died of a heart attack aged 74</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Father died of a heart attack aged 74</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testFamilyMemberHistory2(self):
        inst = self.instantiate_from('familymemberhistory-example-mother.json')
        self.assertIsNotNone(inst, 'Must have instantiated a FamilyMemberHistory instance')
        self.implFamilyMemberHistory2(inst)

        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory2(inst2)

    def implFamilyMemberHistory2(self, inst):
        self.assertEqual(inst.condition[0].code.coding[0].code.value, FHIRCode("371041009").value)
        self.assertEqual(inst.condition[0].code.coding[0].code.as_json(), "371041009")
        self.assertEqual(inst.condition[0].code.coding[0].display.value, FHIRString("Embolic Stroke").value)
        self.assertEqual(inst.condition[0].code.coding[0].display.as_json(), "Embolic Stroke")
        self.assertEqual(inst.condition[0].code.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.condition[0].code.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.condition[0].code.text.value, FHIRString("Stroke").value)
        self.assertEqual(inst.condition[0].code.text.as_json(), "Stroke")
        self.assertEqual(inst.condition[0].onsetAge.code.value, FHIRCode("a").value)
        self.assertEqual(inst.condition[0].onsetAge.code.as_json(), "a")
        self.assertEqual(inst.condition[0].onsetAge.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.condition[0].onsetAge.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.condition[0].onsetAge.unit.value, FHIRString("yr").value)
        self.assertEqual(inst.condition[0].onsetAge.unit.as_json(), "yr")
        self.assertEqual(inst.condition[0].onsetAge.value, 56)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relationship.coding[0].code.value, FHIRCode("MTH").value)
        self.assertEqual(inst.relationship.coding[0].code.as_json(), "MTH")
        self.assertEqual(inst.relationship.coding[0].display.value, FHIRString("mother").value)
        self.assertEqual(inst.relationship.coding[0].display.as_json(), "mother")
        self.assertEqual(inst.relationship.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-RoleCode").value)
        self.assertEqual(inst.relationship.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Mother died of a stroke aged 56</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mother died of a stroke aged 56</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRMarkdown, FHIRDateTime