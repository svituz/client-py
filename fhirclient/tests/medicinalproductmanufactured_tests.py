#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductmanufactured

class MedicinalProductManufacturedTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductManufactured", js["resourceType"])
        return medicinalproductmanufactured.MedicinalProductManufactured(js)

    def testMedicinalProductManufactured1(self):
        inst = self.instantiate_from('medicinalproductmanufactured-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductManufactured instance')
        self.implMedicinalProductManufactured1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductManufactured", js["resourceType"])
        inst2 = medicinalproductmanufactured.MedicinalProductManufactured(js)
        self.implMedicinalProductManufactured1(inst2)

    def implMedicinalProductManufactured1(self, inst):
        self.assertEqual(inst.manufacturedDoseForm.coding[0].code.value, FHIRCode('Film-coatedtablet').value)
        self.assertEqual(inst.manufacturedDoseForm.coding[0].code.as_json(), 'Film-coatedtablet')
        self.assertEqual(inst.manufacturedDoseForm.coding[0].system.value, FHIRUri('http://ema.europa.eu/example/manufactureddoseform').value)
        self.assertEqual(inst.manufacturedDoseForm.coding[0].system.as_json(), 'http://ema.europa.eu/example/manufactureddoseform')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.physicalCharacteristics.color[0].value, FHIRString('Pink').value)
        self.assertEqual(inst.physicalCharacteristics.color[0].as_json(), 'Pink')
        self.assertEqual(inst.physicalCharacteristics.imprint[0].value, FHIRString('894').value)
        self.assertEqual(inst.physicalCharacteristics.imprint[0].as_json(), '894')
        self.assertEqual(inst.physicalCharacteristics.shape.value, FHIRString('Oval').value)
        self.assertEqual(inst.physicalCharacteristics.shape.as_json(), 'Oval')
        self.assertEqual(inst.quantity.unit.value, FHIRString('1').value)
        self.assertEqual(inst.quantity.unit.as_json(), '1')
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.unitOfPresentation.coding[0].code.value, FHIRCode('Tablet').value)
        self.assertEqual(inst.unitOfPresentation.coding[0].code.as_json(), 'Tablet')
        self.assertEqual(inst.unitOfPresentation.coding[0].system.value, FHIRUri('http://ema.europa.eu/example/unitofpresentation').value)
        self.assertEqual(inst.unitOfPresentation.coding[0].system.as_json(), 'http://ema.europa.eu/example/unitofpresentation')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString