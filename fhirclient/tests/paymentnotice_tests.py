#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import paymentnotice

class PaymentNoticeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PaymentNotice", js["resourceType"])
        return paymentnotice.PaymentNotice(js)

    def testPaymentNotice1(self):
        inst = self.instantiate_from('paymentnotice-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a PaymentNotice instance')
        self.implPaymentNotice1(inst)

        js = inst.as_json()
        self.assertEqual("PaymentNotice", js["resourceType"])
        inst2 = paymentnotice.PaymentNotice(js)
        self.implPaymentNotice1(inst2)

    def implPaymentNotice1(self, inst):
        self.assertEqual(inst.amount.currency.value, FHIRCode("USD").value)
        self.assertEqual(inst.amount.currency.as_json(), "USD")
        self.assertEqual(inst.amount.value, 12500.0)
        self.assertEqual(inst.created.value, FHIRDateTime("2014-08-16").value)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://benefitsinc.com/paymentnotice").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://benefitsinc.com/paymentnotice")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("776543").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "776543")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.paymentDate.value, FHIRDate("2014-08-15").value)
        self.assertEqual(inst.paymentDate.as_json(), "2014-08-15")
        self.assertEqual(inst.paymentDate.date, FHIRDate('2014-08-15').date)
        self.assertEqual(inst.paymentStatus.coding[0].code.value, FHIRCode("paid").value)
        self.assertEqual(inst.paymentStatus.coding[0].code.as_json(), "paid")
        self.assertEqual(inst.paymentStatus.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/paymentstatus").value)
        self.assertEqual(inst.paymentStatus.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/paymentstatus")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentNotice</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentNotice</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRDateTime, FHIRUri, FHIRString, FHIRDate