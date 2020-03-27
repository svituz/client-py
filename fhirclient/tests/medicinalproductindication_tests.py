#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductindication

class MedicinalProductIndicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductIndication", js["resourceType"])
        return medicinalproductindication.MedicinalProductIndication(js)

    def testMedicinalProductIndication1(self):
        inst = self.instantiate_from('medicinalproductindication-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductIndication instance')
        self.implMedicinalProductIndication1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductIndication", js["resourceType"])
        inst2 = medicinalproductindication.MedicinalProductIndication(js)
        self.implMedicinalProductIndication1(inst2)

    def implMedicinalProductIndication1(self, inst):
        self.assertEqual(inst.comorbidity[0].coding[0].code.value, FHIRCode("Hipsurgery").value)
        self.assertEqual(inst.comorbidity[0].coding[0].code.as_json(), "Hipsurgery")
        self.assertEqual(inst.comorbidity[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/comorbidity").value)
        self.assertEqual(inst.comorbidity[0].coding[0].system.as_json(), "http://ema.europa.eu/example/comorbidity")
        self.assertEqual(inst.diseaseSymptomProcedure.coding[0].code.value, FHIRCode("Venousthromboembolismprophylaxis").value)
        self.assertEqual(inst.diseaseSymptomProcedure.coding[0].code.as_json(), "Venousthromboembolismprophylaxis")
        self.assertEqual(inst.diseaseSymptomProcedure.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/indicationasdisease-symptom-procedure").value)
        self.assertEqual(inst.diseaseSymptomProcedure.coding[0].system.as_json(), "http://ema.europa.eu/example/indicationasdisease-symptom-procedure")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.intendedEffect.coding[0].code.value, FHIRCode("PRYLX").value)
        self.assertEqual(inst.intendedEffect.coding[0].code.as_json(), "PRYLX")
        self.assertEqual(inst.intendedEffect.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/intendedeffect").value)
        self.assertEqual(inst.intendedEffect.coding[0].system.as_json(), "http://ema.europa.eu/example/intendedeffect")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.population[0].ageRange.low.unit.value, FHIRString("a").value)
        self.assertEqual(inst.population[0].ageRange.low.unit.as_json(), "a")
        self.assertEqual(inst.population[0].ageRange.low.value, 18)
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString