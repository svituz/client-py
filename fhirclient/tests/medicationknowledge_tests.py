#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicationknowledge

class MedicationKnowledgeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicationKnowledge", js["resourceType"])
        return medicationknowledge.MedicationKnowledge(js)

    def testMedicationKnowledge1(self):
        inst = self.instantiate_from('medicationknowledge-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicationKnowledge instance')
        self.implMedicationKnowledge1(inst)

        js = inst.as_json()
        self.assertEqual("MedicationKnowledge", js["resourceType"])
        inst2 = medicationknowledge.MedicationKnowledge(js)
        self.implMedicationKnowledge1(inst2)

    def implMedicationKnowledge1(self, inst):
        self.assertEqual(inst.amount.unit.value, FHIRString("mg/ml").value)
        self.assertEqual(inst.amount.unit.as_json(), "mg/ml")
        self.assertEqual(inst.amount.value, 50)
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode("0069-2587-10").value)
        self.assertEqual(inst.code.coding[0].code.as_json(), "0069-2587-10")
        self.assertEqual(inst.code.coding[0].display.value, FHIRString("Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)").value)
        self.assertEqual(inst.code.coding[0].display.as_json(), "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)")
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri("http://hl7.org/fhir/sid/ndc").value)
        self.assertEqual(inst.code.coding[0].system.as_json(), "http://hl7.org/fhir/sid/ndc")
        self.assertEqual(inst.contained[0].id.value, FHIRString("org4").value)
        self.assertEqual(inst.contained[0].id.as_json(), "org4")
        self.assertEqual(inst.doseForm.coding[0].code.value, FHIRCode("385219001").value)
        self.assertEqual(inst.doseForm.coding[0].code.as_json(), "385219001")
        self.assertEqual(inst.doseForm.coding[0].display.value, FHIRString("Injection Solution (qualifier value)").value)
        self.assertEqual(inst.doseForm.coding[0].display.as_json(), "Injection Solution (qualifier value)")
        self.assertEqual(inst.doseForm.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.doseForm.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.synonym[0].value, FHIRString("Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)").value)
        self.assertEqual(inst.synonym[0].as_json(), "Vancomycin Hydrochloride (VANCOMYCIN HYDROCHLORIDE)")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri