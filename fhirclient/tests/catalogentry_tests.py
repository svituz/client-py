#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import catalogentry

class CatalogEntryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CatalogEntry", js["resourceType"])
        return catalogentry.CatalogEntry(js)

    def testCatalogEntry1(self):
        inst = self.instantiate_from('catalogentry-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CatalogEntry instance')
        self.implCatalogEntry1(inst)

        js = inst.as_json()
        self.assertEqual("CatalogEntry", js["resourceType"])
        inst2 = catalogentry.CatalogEntry(js)
        self.implCatalogEntry1(inst2)

    def implCatalogEntry1(self, inst):
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://example.com/identifier').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://example.com/identifier')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('123').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '123')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertTrue(inst.orderable)
        self.assertEqual(inst.text.div.value, FHIRString('<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>').value)
        self.assertEqual(inst.text.div.as_json(), '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.type.text.value, FHIRString('Medication').value)
        self.assertEqual(inst.type.text.as_json(), 'Medication')


from fhirclient.models.fhirdatatypes import FHIRUri, FHIRString, FHIRCode