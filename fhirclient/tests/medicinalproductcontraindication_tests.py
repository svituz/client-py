#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductcontraindication

class MedicinalProductContraindicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductContraindication", js["resourceType"])
        return medicinalproductcontraindication.MedicinalProductContraindication(js)

    def testMedicinalProductContraindication1(self):
        inst = self.instantiate_from('medicinalproductcontraindication-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductContraindication instance')
        self.implMedicinalProductContraindication1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductContraindication", js["resourceType"])
        inst2 = medicinalproductcontraindication.MedicinalProductContraindication(js)
        self.implMedicinalProductContraindication1(inst2)

    def implMedicinalProductContraindication1(self, inst):
        self.assertEqual(inst.comorbidity[0].coding[0].code.value, FHIRCode("Hepaticdisease").value)
        self.assertEqual(inst.comorbidity[0].coding[0].code.as_json(), "Hepaticdisease")
        self.assertEqual(inst.comorbidity[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/comorbidity").value)
        self.assertEqual(inst.comorbidity[0].coding[0].system.as_json(), "http://ema.europa.eu/example/comorbidity")
        self.assertEqual(inst.disease.coding[0].code.value, FHIRCode("Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)").value)
        self.assertEqual(inst.disease.coding[0].code.as_json(), "Coagulopathiesandbleedingdiatheses(exclthrombocytopenic)")
        self.assertEqual(inst.disease.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/contraindicationsasdisease-symptom-procedure").value)
        self.assertEqual(inst.disease.coding[0].system.as_json(), "http://ema.europa.eu/example/contraindicationsasdisease-symptom-procedure")
        self.assertEqual(inst.disease.text.value, FHIRString("Hepatic disease associated with coagulopathy and clinically relevant bleeding risk").value)
        self.assertEqual(inst.disease.text.as_json(), "Hepatic disease associated with coagulopathy and clinically relevant bleeding risk")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString