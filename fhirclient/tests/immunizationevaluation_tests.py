#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import immunizationevaluation

class ImmunizationEvaluationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        return immunizationevaluation.ImmunizationEvaluation(js)

    def testImmunizationEvaluation1(self):
        inst = self.instantiate_from('immunizationevaluation-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ImmunizationEvaluation instance')
        self.implImmunizationEvaluation1(inst)

        js = inst.as_json()
        self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        inst2 = immunizationevaluation.ImmunizationEvaluation(js)
        self.implImmunizationEvaluation1(inst2)

    def implImmunizationEvaluation1(self, inst):
        self.assertEqual(inst.date.value, FHIRDateTime('2013-01-10').value)
        self.assertEqual(inst.date.as_json(), '2013-01-10')
        self.assertEqual(inst.doseNumberPositiveInt.value, FHIRPositiveInt('1').value)
        self.assertEqual(inst.doseNumberPositiveInt.as_json(), 1)
        self.assertEqual(inst.doseStatus.coding[0].code.value, FHIRCode('valid').value)
        self.assertEqual(inst.doseStatus.coding[0].code.as_json(), 'valid')
        self.assertEqual(inst.doseStatus.coding[0].display.value, FHIRString('Valid').value)
        self.assertEqual(inst.doseStatus.coding[0].display.as_json(), 'Valid')
        self.assertEqual(inst.doseStatus.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status').value)
        self.assertEqual(inst.doseStatus.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('urn:ietf:rfc:3986').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'urn:ietf:rfc:3986')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234').value)
        self.assertEqual(inst.identifier[0].value.as_json(), 'urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.series.value, FHIRString('Vaccination Series 1').value)
        self.assertEqual(inst.series.as_json(), 'Vaccination Series 1')
        self.assertEqual(inst.seriesDosesPositiveInt.value, FHIRPositiveInt('3').value)
        self.assertEqual(inst.seriesDosesPositiveInt.as_json(), 3)
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.targetDisease.coding[0].code.value, FHIRCode('1857005').value)
        self.assertEqual(inst.targetDisease.coding[0].code.as_json(), '1857005')
        self.assertEqual(inst.targetDisease.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.targetDisease.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testImmunizationEvaluation2(self):
        inst = self.instantiate_from('immunizationevaluation-example-notvalid.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ImmunizationEvaluation instance')
        self.implImmunizationEvaluation2(inst)

        js = inst.as_json()
        self.assertEqual("ImmunizationEvaluation", js["resourceType"])
        inst2 = immunizationevaluation.ImmunizationEvaluation(js)
        self.implImmunizationEvaluation2(inst2)

    def implImmunizationEvaluation2(self, inst):
        self.assertEqual(inst.date.value, FHIRDateTime('2013-01-10').value)
        self.assertEqual(inst.date.as_json(), '2013-01-10')
        self.assertEqual(inst.doseNumberPositiveInt.value, FHIRPositiveInt('2').value)
        self.assertEqual(inst.doseNumberPositiveInt.as_json(), 2)
        self.assertEqual(inst.doseStatus.coding[0].code.value, FHIRCode('notvalid').value)
        self.assertEqual(inst.doseStatus.coding[0].code.as_json(), 'notvalid')
        self.assertEqual(inst.doseStatus.coding[0].display.value, FHIRString('Not Valid').value)
        self.assertEqual(inst.doseStatus.coding[0].display.as_json(), 'Not Valid')
        self.assertEqual(inst.doseStatus.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status').value)
        self.assertEqual(inst.doseStatus.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status')
        self.assertEqual(inst.doseStatusReason[0].coding[0].code.value, FHIRCode('outsidesched').value)
        self.assertEqual(inst.doseStatusReason[0].coding[0].code.as_json(), 'outsidesched')
        self.assertEqual(inst.doseStatusReason[0].coding[0].display.value, FHIRString('Administered outside recommended schedule').value)
        self.assertEqual(inst.doseStatusReason[0].coding[0].display.as_json(), 'Administered outside recommended schedule')
        self.assertEqual(inst.doseStatusReason[0].coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason').value)
        self.assertEqual(inst.doseStatusReason[0].coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/immunization-evaluation-dose-status-reason')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('urn:ietf:rfc:3986').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'urn:ietf:rfc:3986')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234').value)
        self.assertEqual(inst.identifier[0].value.as_json(), 'urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.series.value, FHIRString('Vaccination Series 1').value)
        self.assertEqual(inst.series.as_json(), 'Vaccination Series 1')
        self.assertEqual(inst.seriesDosesPositiveInt.value, FHIRPositiveInt('3').value)
        self.assertEqual(inst.seriesDosesPositiveInt.as_json(), 3)
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.targetDisease.coding[0].code.value, FHIRCode('1857005').value)
        self.assertEqual(inst.targetDisease.coding[0].code.as_json(), '1857005')
        self.assertEqual(inst.targetDisease.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.targetDisease.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRPositiveInt, FHIRCode, FHIRString, FHIRUri