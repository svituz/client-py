#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductundesirableeffect

class MedicinalProductUndesirableEffectTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductUndesirableEffect", js["resourceType"])
        return medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(js)

    def testMedicinalProductUndesirableEffect1(self):
        inst = self.instantiate_from('medicinalproductundesirableeffect-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductUndesirableEffect instance')
        self.implMedicinalProductUndesirableEffect1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductUndesirableEffect", js["resourceType"])
        inst2 = medicinalproductundesirableeffect.MedicinalProductUndesirableEffect(js)
        self.implMedicinalProductUndesirableEffect1(inst2)

    def implMedicinalProductUndesirableEffect1(self, inst):
        self.assertEqual(inst.classification.coding[0].code.value, FHIRCode("Bloodandlymphaticsystemdisorders").value)
        self.assertEqual(inst.classification.coding[0].code.as_json(), "Bloodandlymphaticsystemdisorders")
        self.assertEqual(inst.classification.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/symptom-condition-effectclassification").value)
        self.assertEqual(inst.classification.coding[0].system.as_json(), "http://ema.europa.eu/example/symptom-condition-effectclassification")
        self.assertEqual(inst.frequencyOfOccurrence.coding[0].code.value, FHIRCode("Common").value)
        self.assertEqual(inst.frequencyOfOccurrence.coding[0].code.as_json(), "Common")
        self.assertEqual(inst.frequencyOfOccurrence.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/frequencyofoccurrence").value)
        self.assertEqual(inst.frequencyOfOccurrence.coding[0].system.as_json(), "http://ema.europa.eu/example/frequencyofoccurrence")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.symptomConditionEffect.coding[0].code.value, FHIRCode("Anaemia").value)
        self.assertEqual(inst.symptomConditionEffect.coding[0].code.as_json(), "Anaemia")
        self.assertEqual(inst.symptomConditionEffect.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/undesirableeffectassymptom-condition-effect").value)
        self.assertEqual(inst.symptomConditionEffect.coding[0].system.as_json(), "http://ema.europa.eu/example/undesirableeffectassymptom-condition-effect")
        self.assertEqual(inst.symptomConditionEffect.text.value, FHIRString("Prevention of\\nVTE in adult\\npatients who have\\nundergone\\nelective hip or\\nknee replacement\\nsurgery (VTEp)").value)
        self.assertEqual(inst.symptomConditionEffect.text.as_json(), "Prevention of\\nVTE in adult\\npatients who have\\nundergone\\nelective hip or\\nknee replacement\\nsurgery (VTEp)")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString