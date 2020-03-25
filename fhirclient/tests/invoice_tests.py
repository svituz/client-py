#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import invoice

class InvoiceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Invoice", js["resourceType"])
        return invoice.Invoice(js)

    def testInvoice1(self):
        inst = self.instantiate_from('invoice-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Invoice instance')
        self.implInvoice1(inst)

        js = inst.as_json()
        self.assertEqual("Invoice", js["resourceType"])
        inst2 = invoice.Invoice(js)
        self.implInvoice1(inst2)

    def implInvoice1(self, inst):
        self.assertEqual(inst.date.value, FHIRDateTime('2017-01-25T08:00:00+01:00').value)
        self.assertEqual(inst.date.as_json(), '2017-01-25T08:00:00+01:00')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://myHospital.org/Invoices').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://myHospital.org/Invoices')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('654321').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '654321')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.participant[0].role.coding[0].code.value, FHIRCode('17561000').value)
        self.assertEqual(inst.participant[0].role.coding[0].code.as_json(), '17561000')
        self.assertEqual(inst.participant[0].role.coding[0].display.value, FHIRString('Cardiologist').value)
        self.assertEqual(inst.participant[0].role.coding[0].display.as_json(), 'Cardiologist')
        self.assertEqual(inst.participant[0].role.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.participant[0].role.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.status.value, FHIRCode('issued').value)
        self.assertEqual(inst.status.as_json(), 'issued')
        self.assertEqual(inst.text.div.value, FHIRString('<div xmlns="http://www.w3.org/1999/xhtml">Example of Invoice</div>').value)
        self.assertEqual(inst.text.div.as_json(), '<div xmlns="http://www.w3.org/1999/xhtml">Example of Invoice</div>')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.totalGross.currency.value, FHIRCode('EUR').value)
        self.assertEqual(inst.totalGross.currency.as_json(), 'EUR')
        self.assertEqual(inst.totalGross.value, 48)
        self.assertEqual(inst.totalNet.currency.value, FHIRCode('EUR').value)
        self.assertEqual(inst.totalNet.currency.as_json(), 'EUR')
        self.assertEqual(inst.totalNet.value, 40)


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRUri, FHIRString, FHIRCode