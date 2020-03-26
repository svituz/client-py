#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductinteraction

class MedicinalProductInteractionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductInteraction", js["resourceType"])
        return medicinalproductinteraction.MedicinalProductInteraction(js)

    def testMedicinalProductInteraction1(self):
        inst = self.instantiate_from('medicinalproductinteraction-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductInteraction instance')
        self.implMedicinalProductInteraction1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductInteraction", js["resourceType"])
        inst2 = medicinalproductinteraction.MedicinalProductInteraction(js)
        self.implMedicinalProductInteraction1(inst2)

    def implMedicinalProductInteraction1(self, inst):
        self.assertEqual(inst.effect.coding[0].code.value, FHIRCode("Increasedplasmaconcentrations").value)
        self.assertEqual(inst.effect.coding[0].code.as_json(), "Increasedplasmaconcentrations")
        self.assertEqual(inst.effect.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/interactionseffect").value)
        self.assertEqual(inst.effect.coding[0].system.as_json(), "http://ema.europa.eu/example/interactionseffect")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.interactant[0].itemCodeableConcept.coding[0].code.value, FHIRCode("ketoconazole").value)
        self.assertEqual(inst.interactant[0].itemCodeableConcept.coding[0].code.as_json(), "ketoconazole")
        self.assertEqual(inst.interactant[0].itemCodeableConcept.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/interactant").value)
        self.assertEqual(inst.interactant[0].itemCodeableConcept.coding[0].system.as_json(), "http://ema.europa.eu/example/interactant")
        self.assertEqual(inst.interactant[1].itemCodeableConcept.coding[0].code.value, FHIRCode("itraconazole").value)
        self.assertEqual(inst.interactant[1].itemCodeableConcept.coding[0].code.as_json(), "itraconazole")
        self.assertEqual(inst.interactant[1].itemCodeableConcept.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/interactant").value)
        self.assertEqual(inst.interactant[1].itemCodeableConcept.coding[0].system.as_json(), "http://ema.europa.eu/example/interactant")
        self.assertEqual(inst.management.text.value, FHIRString("Coadministration not recommended in patients receiving concomitant systemic treatment strong inhibitors of both CYP3A4 and P-gp").value)
        self.assertEqual(inst.management.text.as_json(), "Coadministration not recommended in patients receiving concomitant systemic treatment strong inhibitors of both CYP3A4 and P-gp")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("StrongInhibitorofCYP3A4").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "StrongInhibitorofCYP3A4")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/interactionsType").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://ema.europa.eu/example/interactionsType")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString