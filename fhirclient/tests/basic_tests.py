#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import basic

class BasicTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Basic", js["resourceType"])
        return basic.Basic(js)

    def testBasic1(self):
        inst = self.instantiate_from('basic-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Basic instance')
        self.implBasic1(inst)

        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic1(inst2)

    def implBasic1(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('referral').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), 'referral')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/basic-resource-type').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/basic-resource-type')
        self.assertEqual(inst.created.value, FHIRDate('2013-05-14').value)
        self.assertEqual(inst.created.as_json(), '2013-05-14')
        self.assertEqual(inst.created.date, FHIRDate('2013-05-14').date)
        self.assertEqual(inst.extension[1].valueString.value, FHIRString('The patient had fever peaks over the last couple of days. He is worried about these peaks.').value)
        self.assertEqual(inst.extension[1].valueString.as_json(), 'The patient had fever peaks over the last couple of days. He is worried about these peaks.')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://goodhealth.org/basic/identifiers').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://goodhealth.org/basic/identifiers')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('19283746').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '19283746')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].code.value, FHIRCode('11429006').value)
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].code.as_json(), '11429006')
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].display.value, FHIRString('Consultation').value)
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].display.as_json(), 'Consultation')
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.modifierExtension[0].valueCodeableConcept.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.modifierExtension[1].valuePeriod.end.value, FHIRDateTime('2013-04-15').value)
        self.assertEqual(inst.modifierExtension[1].valuePeriod.end.as_json(), '2013-04-15')
        self.assertEqual(inst.modifierExtension[1].valuePeriod.start.value, FHIRDateTime('2013-04-01').value)
        self.assertEqual(inst.modifierExtension[1].valuePeriod.start.as_json(), '2013-04-01')
        self.assertEqual(inst.modifierExtension[2].valueCode.value, FHIRCode('complete').value)
        self.assertEqual(inst.modifierExtension[2].valueCode.as_json(), 'complete')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testBasic2(self):
        inst = self.instantiate_from('basic-example2.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Basic instance')
        self.implBasic2(inst)

        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic2(inst2)

    def implBasic2(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('UMLCLASSMODEL').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), 'UMLCLASSMODEL')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://example.org/do-not-use/fhir-codes#resourceTypes').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://example.org/do-not-use/fhir-codes#resourceTypes')
        self.assertEqual(inst.extension[0].extension[0].valueString.value, FHIRString('Class1').value)
        self.assertEqual(inst.extension[0].extension[0].valueString.as_json(), 'Class1')
        self.assertEqual(inst.extension[0].extension[1].extension[0].valueString.value, FHIRString('attribute1').value)
        self.assertEqual(inst.extension[0].extension[1].extension[0].valueString.as_json(), 'attribute1')
        self.assertEqual(inst.extension[0].extension[1].extension[1].valueInteger, 1)
        self.assertEqual(inst.extension[0].extension[1].extension[2].valueCode.value, FHIRCode('*').value)
        self.assertEqual(inst.extension[0].extension[1].extension[2].valueCode.as_json(), '*')
        self.assertEqual(inst.extension[0].extension[2].extension[0].valueString.value, FHIRString('attribute2').value)
        self.assertEqual(inst.extension[0].extension[2].extension[0].valueString.as_json(), 'attribute2')
        self.assertEqual(inst.extension[0].extension[2].extension[1].valueInteger, 0)
        self.assertEqual(inst.extension[0].extension[2].extension[2].valueInteger, 1)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testBasic3(self):
        inst = self.instantiate_from('basic-example-narrative.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Basic instance')
        self.implBasic3(inst)

        js = inst.as_json()
        self.assertEqual("Basic", js["resourceType"])
        inst2 = basic.Basic(js)
        self.implBasic3(inst2)

    def implBasic3(self, inst):
        self.assertEqual(inst.code.text.value, FHIRString('Example Narrative Tester').value)
        self.assertEqual(inst.code.text.as_json(), 'Example Narrative Tester')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.text.status.value, FHIRCode('additional').value)
        self.assertEqual(inst.text.status.as_json(), 'additional')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRDate, FHIRString, FHIRDateTime