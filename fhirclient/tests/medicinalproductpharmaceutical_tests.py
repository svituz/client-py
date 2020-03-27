#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductpharmaceutical

class MedicinalProductPharmaceuticalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductPharmaceutical", js["resourceType"])
        return medicinalproductpharmaceutical.MedicinalProductPharmaceutical(js)

    def testMedicinalProductPharmaceutical1(self):
        inst = self.instantiate_from('medicinalproductpharmaceutical-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductPharmaceutical instance')
        self.implMedicinalProductPharmaceutical1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductPharmaceutical", js["resourceType"])
        inst2 = medicinalproductpharmaceutical.MedicinalProductPharmaceutical(js)
        self.implMedicinalProductPharmaceutical1(inst2)

    def implMedicinalProductPharmaceutical1(self, inst):
        self.assertEqual(inst.administrableDoseForm.coding[0].code.value, FHIRCode("Film-coatedtablet").value)
        self.assertEqual(inst.administrableDoseForm.coding[0].code.as_json(), "Film-coatedtablet")
        self.assertEqual(inst.administrableDoseForm.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/administrabledoseform").value)
        self.assertEqual(inst.administrableDoseForm.coding[0].system.as_json(), "http://ema.europa.eu/example/administrabledoseform")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://ema.europa.eu/example/phpididentifiersets").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://ema.europa.eu/example/phpididentifiersets")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("{PhPID}").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "{PhPID}")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].code.value, FHIRCode("OralUse").value)
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].code.as_json(), "OralUse")
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/routeofadministration").value)
        self.assertEqual(inst.routeOfAdministration[0].code.coding[0].system.as_json(), "http://ema.europa.eu/example/routeofadministration")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.unitOfPresentation.coding[0].code.value, FHIRCode("Tablet").value)
        self.assertEqual(inst.unitOfPresentation.coding[0].code.as_json(), "Tablet")
        self.assertEqual(inst.unitOfPresentation.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/unitofpresentation").value)
        self.assertEqual(inst.unitOfPresentation.coding[0].system.as_json(), "http://ema.europa.eu/example/unitofpresentation")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString