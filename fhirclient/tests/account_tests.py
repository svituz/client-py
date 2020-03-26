#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import account

class AccountTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Account", js["resourceType"])
        return account.Account(js)

    def testAccount1(self):
        inst = self.instantiate_from('account-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Account instance')
        self.implAccount1(inst)

        js = inst.as_json()
        self.assertEqual("Account", js["resourceType"])
        inst2 = account.Account(js)
        self.implAccount1(inst2)

    def implAccount1(self, inst):
        self.assertEqual(inst.coverage[0].priority.value, FHIRPositiveInt('1').value)
        self.assertEqual(inst.coverage[0].priority.as_json(), 1)
        self.assertEqual(inst.description.value, FHIRString("Hospital charges").value)
        self.assertEqual(inst.description.as_json(), "Hospital charges")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:oid:0.1.2.3.4.5.6.7").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("654321").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "654321")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("HACC Funded Billing for Peter James Chalmers").value)
        self.assertEqual(inst.name.as_json(), "HACC Funded Billing for Peter James Chalmers")
        self.assertEqual(inst.servicePeriod.end.value, FHIRDateTime("2016-06-30").value)
        self.assertEqual(inst.servicePeriod.end.as_json(), "2016-06-30")
        self.assertEqual(inst.servicePeriod.start.value, FHIRDateTime("2016-01-01").value)
        self.assertEqual(inst.servicePeriod.start.as_json(), "2016-01-01")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">HACC Funded Billing for Peter James Chalmers</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">HACC Funded Billing for Peter James Chalmers</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("PBILLACCT").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "PBILLACCT")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("patient billing account").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "patient billing account")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.type.text.value, FHIRString("patient").value)
        self.assertEqual(inst.type.text.as_json(), "patient")

    def testAccount2(self):
        inst = self.instantiate_from('account-example-with-guarantor.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Account instance')
        self.implAccount2(inst)

        js = inst.as_json()
        self.assertEqual("Account", js["resourceType"])
        inst2 = account.Account(js)
        self.implAccount2(inst2)

    def implAccount2(self, inst):
        self.assertEqual(inst.coverage[0].priority.value, FHIRPositiveInt('1').value)
        self.assertEqual(inst.coverage[0].priority.as_json(), 1)
        self.assertEqual(inst.coverage[1].priority.value, FHIRPositiveInt('2').value)
        self.assertEqual(inst.coverage[1].priority.as_json(), 2)
        self.assertEqual(inst.description.value, FHIRString("Hospital charges").value)
        self.assertEqual(inst.description.as_json(), "Hospital charges")
        self.assertFalse(inst.guarantor[0].onHold)
        self.assertEqual(inst.guarantor[0].period.start.value, FHIRDateTime("2016-01-01").value)
        self.assertEqual(inst.guarantor[0].period.start.as_json(), "2016-01-01")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:oid:0.1.2.3.4.5.6.7").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:oid:0.1.2.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("654321").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "654321")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("Inpatient: Peter James Chalmers").value)
        self.assertEqual(inst.name.as_json(), "Inpatient: Peter James Chalmers")
        self.assertEqual(inst.servicePeriod.end.value, FHIRDateTime("2016-06-30").value)
        self.assertEqual(inst.servicePeriod.end.as_json(), "2016-06-30")
        self.assertEqual(inst.servicePeriod.start.value, FHIRDateTime("2016-01-01").value)
        self.assertEqual(inst.servicePeriod.start.as_json(), "2016-01-01")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Inpatient Admission for Peter James Chalmers Account</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Inpatient Admission for Peter James Chalmers Account</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("PBILLACCT").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "PBILLACCT")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("patient billing account").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "patient billing account")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.type.text.value, FHIRString("patient").value)
        self.assertEqual(inst.type.text.as_json(), "patient")


from fhirclient.models.fhirdatatypes import FHIRPositiveInt, FHIRString, FHIRUri, FHIRCode, FHIRDateTime