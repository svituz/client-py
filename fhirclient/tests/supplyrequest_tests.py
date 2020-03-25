#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import supplyrequest

class SupplyRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SupplyRequest", js["resourceType"])
        return supplyrequest.SupplyRequest(js)

    def testSupplyRequest1(self):
        inst = self.instantiate_from('supplyrequest-example-simpleorder.json')
        self.assertIsNotNone(inst, 'Must have instantiated a SupplyRequest instance')
        self.implSupplyRequest1(inst)

        js = inst.as_json()
        self.assertEqual("SupplyRequest", js["resourceType"])
        inst2 = supplyrequest.SupplyRequest(js)
        self.implSupplyRequest1(inst2)

    def implSupplyRequest1(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime('2016-12-31').value)
        self.assertEqual(inst.authoredOn.as_json(), '2016-12-31')
        self.assertEqual(inst.category.coding[0].code.value, FHIRCode('central').value)
        self.assertEqual(inst.category.coding[0].code.as_json(), 'central')
        self.assertEqual(inst.category.coding[0].display.value, FHIRString('Central Stock Resupply').value)
        self.assertEqual(inst.category.coding[0].display.as_json(), 'Central Stock Resupply')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('Order10284').value)
        self.assertEqual(inst.identifier[0].value.as_json(), 'Order10284')
        self.assertEqual(inst.itemCodeableConcept.coding[0].code.value, FHIRCode('BlueTubes').value)
        self.assertEqual(inst.itemCodeableConcept.coding[0].code.as_json(), 'BlueTubes')
        self.assertEqual(inst.itemCodeableConcept.coding[0].display.value, FHIRString('Blood collect tubes blue cap').value)
        self.assertEqual(inst.itemCodeableConcept.coding[0].display.as_json(), 'Blood collect tubes blue cap')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime('2016-12-31').value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), '2016-12-31')
        self.assertEqual(inst.priority.value, FHIRCode('asap').value)
        self.assertEqual(inst.priority.as_json(), 'asap')
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(inst.reasonCode[0].coding[0].code.value, FHIRCode('stock_low').value)
        self.assertEqual(inst.reasonCode[0].coding[0].code.as_json(), 'stock_low')
        self.assertEqual(inst.reasonCode[0].coding[0].display.value, FHIRString('Refill due to low stock').value)
        self.assertEqual(inst.reasonCode[0].coding[0].display.as_json(), 'Refill due to low stock')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRCode, FHIRString, FHIRUri