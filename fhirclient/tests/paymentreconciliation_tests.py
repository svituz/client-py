#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import paymentreconciliation

class PaymentReconciliationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PaymentReconciliation", js["resourceType"])
        return paymentreconciliation.PaymentReconciliation(js)

    def testPaymentReconciliation1(self):
        inst = self.instantiate_from('paymentreconciliation-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a PaymentReconciliation instance')
        self.implPaymentReconciliation1(inst)

        js = inst.as_json()
        self.assertEqual("PaymentReconciliation", js["resourceType"])
        inst2 = paymentreconciliation.PaymentReconciliation(js)
        self.implPaymentReconciliation1(inst2)

    def implPaymentReconciliation1(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2014-08-16").value)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.detail[0].amount.currency.value, FHIRCode("USD").value)
        self.assertEqual(inst.detail[0].amount.currency.as_json(), "USD")
        self.assertEqual(inst.detail[0].amount.value, 3500.0)
        self.assertEqual(inst.detail[0].date.value, FHIRDate("2014-08-16").value)
        self.assertEqual(inst.detail[0].date.as_json(), "2014-08-16")
        self.assertEqual(inst.detail[0].date.date, FHIRDate('2014-08-16').date)
        self.assertEqual(inst.detail[0].identifier.system.value, FHIRUri("http://www.BenefitsInc.com/payment/2018/detail").value)
        self.assertEqual(inst.detail[0].identifier.system.as_json(), "http://www.BenefitsInc.com/payment/2018/detail")
        self.assertEqual(inst.detail[0].identifier.value.value, FHIRString("10-12345-001").value)
        self.assertEqual(inst.detail[0].identifier.value.as_json(), "10-12345-001")
        self.assertEqual(inst.detail[0].type.coding[0].code.value, FHIRCode("payment").value)
        self.assertEqual(inst.detail[0].type.coding[0].code.as_json(), "payment")
        self.assertEqual(inst.detail[0].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/payment-type").value)
        self.assertEqual(inst.detail[0].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/payment-type")
        self.assertEqual(inst.detail[1].amount.currency.value, FHIRCode("USD").value)
        self.assertEqual(inst.detail[1].amount.currency.as_json(), "USD")
        self.assertEqual(inst.detail[1].amount.value, 4000.0)
        self.assertEqual(inst.detail[1].date.value, FHIRDate("2014-08-12").value)
        self.assertEqual(inst.detail[1].date.as_json(), "2014-08-12")
        self.assertEqual(inst.detail[1].date.date, FHIRDate('2014-08-12').date)
        self.assertEqual(inst.detail[1].identifier.system.value, FHIRUri("http://www.BenefitsInc.com/payment/2018/detail").value)
        self.assertEqual(inst.detail[1].identifier.system.as_json(), "http://www.BenefitsInc.com/payment/2018/detail")
        self.assertEqual(inst.detail[1].identifier.value.value, FHIRString("10-12345-002").value)
        self.assertEqual(inst.detail[1].identifier.value.as_json(), "10-12345-002")
        self.assertEqual(inst.detail[1].type.coding[0].code.value, FHIRCode("payment").value)
        self.assertEqual(inst.detail[1].type.coding[0].code.as_json(), "payment")
        self.assertEqual(inst.detail[1].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/payment-type").value)
        self.assertEqual(inst.detail[1].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/payment-type")
        self.assertEqual(inst.detail[2].amount.currency.value, FHIRCode("USD").value)
        self.assertEqual(inst.detail[2].amount.currency.as_json(), "USD")
        self.assertEqual(inst.detail[2].amount.value, -1500.0)
        self.assertEqual(inst.detail[2].date.value, FHIRDate("2014-08-16").value)
        self.assertEqual(inst.detail[2].date.as_json(), "2014-08-16")
        self.assertEqual(inst.detail[2].date.date, FHIRDate('2014-08-16').date)
        self.assertEqual(inst.detail[2].identifier.system.value, FHIRUri("http://www.BenefitsInc.com/payment/2018/detail").value)
        self.assertEqual(inst.detail[2].identifier.system.as_json(), "http://www.BenefitsInc.com/payment/2018/detail")
        self.assertEqual(inst.detail[2].identifier.value.value, FHIRString("10-12345-003").value)
        self.assertEqual(inst.detail[2].identifier.value.as_json(), "10-12345-003")
        self.assertEqual(inst.detail[2].type.coding[0].code.value, FHIRCode("advance").value)
        self.assertEqual(inst.detail[2].type.coding[0].code.as_json(), "advance")
        self.assertEqual(inst.detail[2].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/payment-type").value)
        self.assertEqual(inst.detail[2].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/payment-type")
        self.assertEqual(inst.disposition.value, FHIRString("2014 August mid-month settlement.").value)
        self.assertEqual(inst.disposition.as_json(), "2014 August mid-month settlement.")
        self.assertEqual(inst.formCode.coding[0].code.value, FHIRCode("PAYREC/2016/01B").value)
        self.assertEqual(inst.formCode.coding[0].code.as_json(), "PAYREC/2016/01B")
        self.assertEqual(inst.formCode.coding[0].system.value, FHIRUri("http://ncforms.org/formid").value)
        self.assertEqual(inst.formCode.coding[0].system.as_json(), "http://ncforms.org/formid")
        self.assertEqual(inst.id.value, FHIRString("ER2500").value)
        self.assertEqual(inst.id.as_json(), "ER2500")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.BenefitsInc.com/fhir/enrollmentresponse").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.BenefitsInc.com/fhir/enrollmentresponse")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("781234").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "781234")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome.value, FHIRCode("complete").value)
        self.assertEqual(inst.outcome.as_json(), "complete")
        self.assertEqual(inst.paymentAmount.currency.value, FHIRCode("USD").value)
        self.assertEqual(inst.paymentAmount.currency.as_json(), "USD")
        self.assertEqual(inst.paymentAmount.value, 7000.0)
        self.assertEqual(inst.paymentDate.value, FHIRDate("2014-08-01").value)
        self.assertEqual(inst.paymentDate.as_json(), "2014-08-01")
        self.assertEqual(inst.paymentDate.date, FHIRDate('2014-08-01').date)
        self.assertEqual(inst.paymentIdentifier.system.value, FHIRUri("http://www.BenefitsInc.com/payment/2018").value)
        self.assertEqual(inst.paymentIdentifier.system.as_json(), "http://www.BenefitsInc.com/payment/2018")
        self.assertEqual(inst.paymentIdentifier.value.value, FHIRString("10-12345").value)
        self.assertEqual(inst.paymentIdentifier.value.as_json(), "10-12345")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2014-08-31").value)
        self.assertEqual(inst.period.end.as_json(), "2014-08-31")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2014-08-16").value)
        self.assertEqual(inst.period.start.as_json(), "2014-08-16")
        self.assertEqual(inst.processNote[0].text.value, FHIRString("Due to the year end holiday the cutoff for submissions for December will be the 28th.").value)
        self.assertEqual(inst.processNote[0].text.as_json(), "Due to the year end holiday the cutoff for submissions for December will be the 28th.")
        self.assertEqual(inst.processNote[0].type.value, FHIRCode("display").value)
        self.assertEqual(inst.processNote[0].type.as_json(), "display")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentReconciliation</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the PaymentReconciliation</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRCode, FHIRDate, FHIRUri, FHIRString