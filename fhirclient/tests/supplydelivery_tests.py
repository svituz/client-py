#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import supplydelivery

class SupplyDeliveryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SupplyDelivery", js["resourceType"])
        return supplydelivery.SupplyDelivery(js)

    def testSupplyDelivery1(self):
        inst = self.instantiate_from('supplydelivery-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a SupplyDelivery instance')
        self.implSupplyDelivery1(inst)

        js = inst.as_json()
        self.assertEqual("SupplyDelivery", js["resourceType"])
        inst2 = supplydelivery.SupplyDelivery(js)
        self.implSupplyDelivery1(inst2)

    def implSupplyDelivery1(self, inst):
        self.assertEqual(inst.id.value, FHIRString("simpledelivery").value)
        self.assertEqual(inst.id.as_json(), "simpledelivery")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("Order10284").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "Order10284")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime("2016-12-31").value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.suppliedItem.itemCodeableConcept.coding[0].code.value, FHIRCode("BlueTubes").value)
        self.assertEqual(inst.suppliedItem.itemCodeableConcept.coding[0].code.as_json(), "BlueTubes")
        self.assertEqual(inst.suppliedItem.itemCodeableConcept.coding[0].display.value, FHIRString("Blood collect tubes blue cap").value)
        self.assertEqual(inst.suppliedItem.itemCodeableConcept.coding[0].display.as_json(), "Blood collect tubes blue cap")
        self.assertEqual(inst.suppliedItem.quantity.value, 10)
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("device").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "device")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/supply-item-type").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/supply-item-type")
        self.assertEqual(inst.type.text.value, FHIRString("Blood collect tubes blue cap").value)
        self.assertEqual(inst.type.text.as_json(), "Blood collect tubes blue cap")

    def testSupplyDelivery2(self):
        inst = self.instantiate_from('supplydelivery-example-pumpdelivery.json')
        self.assertIsNotNone(inst, 'Must have instantiated a SupplyDelivery instance')
        self.implSupplyDelivery2(inst)

        js = inst.as_json()
        self.assertEqual("SupplyDelivery", js["resourceType"])
        inst2 = supplydelivery.SupplyDelivery(js)
        self.implSupplyDelivery2(inst2)

    def implSupplyDelivery2(self, inst):
        self.assertEqual(inst.id.value, FHIRString("pumpdelivery").value)
        self.assertEqual(inst.id.as_json(), "pumpdelivery")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("98398459409").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "98398459409")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("in-progress").value)
        self.assertEqual(inst.status.as_json(), "in-progress")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri, FHIRDateTime