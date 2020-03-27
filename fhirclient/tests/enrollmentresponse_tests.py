#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import enrollmentresponse

class EnrollmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EnrollmentResponse", js["resourceType"])
        return enrollmentresponse.EnrollmentResponse(js)

    def testEnrollmentResponse1(self):
        inst = self.instantiate_from('enrollmentresponse-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a EnrollmentResponse instance')
        self.implEnrollmentResponse1(inst)

        js = inst.as_json()
        self.assertEqual("EnrollmentResponse", js["resourceType"])
        inst2 = enrollmentresponse.EnrollmentResponse(js)
        self.implEnrollmentResponse1(inst2)

    def implEnrollmentResponse1(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2014-08-16").value)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition.value, FHIRString("Dependant added to policy.").value)
        self.assertEqual(inst.disposition.as_json(), "Dependant added to policy.")
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
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EnrollmentResponse</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EnrollmentResponse</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRString, FHIRUri, FHIRCode