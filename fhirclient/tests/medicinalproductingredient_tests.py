#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductingredient

class MedicinalProductIngredientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductIngredient", js["resourceType"])
        return medicinalproductingredient.MedicinalProductIngredient(js)

    def testMedicinalProductIngredient1(self):
        inst = self.instantiate_from('medicinalproductingredient-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductIngredient instance')
        self.implMedicinalProductIngredient1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductIngredient", js["resourceType"])
        inst2 = medicinalproductingredient.MedicinalProductIngredient(js)
        self.implMedicinalProductIngredient1(inst2)

    def implMedicinalProductIngredient1(self, inst):
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.role.coding[0].code.value, FHIRCode("ActiveBase").value)
        self.assertEqual(inst.role.coding[0].code.as_json(), "ActiveBase")
        self.assertEqual(inst.role.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/ingredientRole").value)
        self.assertEqual(inst.role.coding[0].system.as_json(), "http://ema.europa.eu/example/ingredientRole")
        self.assertEqual(inst.specifiedSubstance[0].code.coding[0].code.value, FHIRCode("equixabanCompanyequixaban1").value)
        self.assertEqual(inst.specifiedSubstance[0].code.coding[0].code.as_json(), "equixabanCompanyequixaban1")
        self.assertEqual(inst.specifiedSubstance[0].code.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/specifiedSubstance").value)
        self.assertEqual(inst.specifiedSubstance[0].code.coding[0].system.as_json(), "http://ema.europa.eu/example/specifiedSubstance")
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].code.value, FHIRCode("2").value)
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].code.as_json(), "2")
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/specifiedSubstanceGroup").value)
        self.assertEqual(inst.specifiedSubstance[0].group.coding[0].system.as_json(), "http://ema.europa.eu/example/specifiedSubstanceGroup")
        self.assertEqual(inst.substance.code.coding[0].code.value, FHIRCode("EQUIXABAN").value)
        self.assertEqual(inst.substance.code.coding[0].code.as_json(), "EQUIXABAN")
        self.assertEqual(inst.substance.code.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/substance").value)
        self.assertEqual(inst.substance.code.coding[0].system.as_json(), "http://ema.europa.eu/example/substance")
        self.assertEqual(inst.substance.strength[0].presentation.denominator.unit.value, FHIRString("{tablet}").value)
        self.assertEqual(inst.substance.strength[0].presentation.denominator.unit.as_json(), "{tablet}")
        self.assertEqual(inst.substance.strength[0].presentation.denominator.value, 1)
        self.assertEqual(inst.substance.strength[0].presentation.numerator.unit.value, FHIRString("mg").value)
        self.assertEqual(inst.substance.strength[0].presentation.numerator.unit.as_json(), "mg")
        self.assertEqual(inst.substance.strength[0].presentation.numerator.value, 2.5)
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri