#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import adverseevent

class AdverseEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AdverseEvent", js["resourceType"])
        return adverseevent.AdverseEvent(js)

    def testAdverseEvent1(self):
        inst = self.instantiate_from('adverseevent-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a AdverseEvent instance')
        self.implAdverseEvent1(inst)

        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent1(inst2)

    def implAdverseEvent1(self, inst):
        self.assertEqual(inst.actuality.value, FHIRCode('actual').value)
        self.assertEqual(inst.actuality.as_json(), 'actual')
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode('product-use-error').value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), 'product-use-error')
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString('Product Use Error').value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), 'Product Use Error')
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/adverse-event-category').value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/adverse-event-category')
        self.assertEqual(inst.date.value, FHIRDateTime('2017-01-29T12:34:56+00:00').value)
        self.assertEqual(inst.date.as_json(), '2017-01-29T12:34:56+00:00')
        self.assertEqual(inst.event.coding[0].code.value, FHIRCode('304386008').value)
        self.assertEqual(inst.event.coding[0].code.as_json(), '304386008')
        self.assertEqual(inst.event.coding[0].display.value, FHIRString('O/E - itchy rash').value)
        self.assertEqual(inst.event.coding[0].display.as_json(), 'O/E - itchy rash')
        self.assertEqual(inst.event.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.event.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.event.text.value, FHIRString('This was a mild rash on the left forearm').value)
        self.assertEqual(inst.event.text.as_json(), 'This was a mild rash on the left forearm')
        self.assertEqual(inst.identifier.system.value, FHIRUri('http://acme.com/ids/patients/risks').value)
        self.assertEqual(inst.identifier.system.as_json(), 'http://acme.com/ids/patients/risks')
        self.assertEqual(inst.identifier.value.value, FHIRString('49476534').value)
        self.assertEqual(inst.identifier.value.as_json(), '49476534')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.seriousness.coding[0].code.value, FHIRCode('Non-serious').value)
        self.assertEqual(inst.seriousness.coding[0].code.as_json(), 'Non-serious')
        self.assertEqual(inst.seriousness.coding[0].display.value, FHIRString('Non-serious').value)
        self.assertEqual(inst.seriousness.coding[0].display.as_json(), 'Non-serious')
        self.assertEqual(inst.seriousness.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/adverse-event-seriousness').value)
        self.assertEqual(inst.seriousness.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/adverse-event-seriousness')
        self.assertEqual(inst.severity.coding[0].code.value, FHIRCode('mild').value)
        self.assertEqual(inst.severity.coding[0].code.as_json(), 'mild')
        self.assertEqual(inst.severity.coding[0].display.value, FHIRString('Mild').value)
        self.assertEqual(inst.severity.coding[0].display.as_json(), 'Mild')
        self.assertEqual(inst.severity.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/adverse-event-severity').value)
        self.assertEqual(inst.severity.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/adverse-event-severity')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime