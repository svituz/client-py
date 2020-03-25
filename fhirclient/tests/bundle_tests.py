#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import bundle

class BundleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Bundle", js["resourceType"])
        return bundle.Bundle(js)

    def testBundle1(self):
        inst = self.instantiate_from('diagnosticreport-example-lri.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle1(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle1(inst2)

    def implBundle1(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('http://test.fhir.org/r4/DiagnosticReport/lri-example').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'http://test.fhir.org/r4/DiagnosticReport/lri-example')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-gramstain1').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-gramstain1')
        self.assertEqual(inst.entry[2].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-gramstain2').value)
        self.assertEqual(inst.entry[2].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-gramstain2')
        self.assertEqual(inst.entry[3].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-gramstain3').value)
        self.assertEqual(inst.entry[3].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-gramstain3')
        self.assertEqual(inst.entry[4].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-gramstain4').value)
        self.assertEqual(inst.entry[4].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-gramstain4')
        self.assertEqual(inst.entry[5].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-growth1').value)
        self.assertEqual(inst.entry[5].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-growth1')
        self.assertEqual(inst.entry[6].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-growth2').value)
        self.assertEqual(inst.entry[6].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-growth2')
        self.assertEqual(inst.entry[7].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-growth3').value)
        self.assertEqual(inst.entry[7].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-growth3')
        self.assertEqual(inst.entry[8].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-org2-amp').value)
        self.assertEqual(inst.entry[8].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-org2-amp')
        self.assertEqual(inst.entry[9].fullUrl.value, FHIRUri('http://test.fhir.org/r4/Observation/lri-org2-cip').value)
        self.assertEqual(inst.entry[9].fullUrl.as_json(), 'http://test.fhir.org/r4/Observation/lri-org2-cip')
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant('2017-06-27T00:52:51Z').value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), '2017-06-27T00:52:51Z')
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2017-06-27T00:52:51Z').date)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.meta.versionId.value, FHIRId('1').value)
        self.assertEqual(inst.meta.versionId.as_json(), '1')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle2(self):
        inst = self.instantiate_from('practitioner-examples-general.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle2(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle2(inst2)

    def implBundle2(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/1').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/1')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/13').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/13')
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[2].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/14').value)
        self.assertEqual(inst.entry[2].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/14')
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[3].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/15').value)
        self.assertEqual(inst.entry[3].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/15')
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[4].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/16').value)
        self.assertEqual(inst.entry[4].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/16')
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[5].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/17').value)
        self.assertEqual(inst.entry[5].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/17')
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[6].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/18').value)
        self.assertEqual(inst.entry[6].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/18')
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[7].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/19').value)
        self.assertEqual(inst.entry[7].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/19')
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[8].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/20').value)
        self.assertEqual(inst.entry[8].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/20')
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[9].fullUrl.value, FHIRUri('http://hl7.org/fhir/Practitioner/21').value)
        self.assertEqual(inst.entry[9].fullUrl.as_json(), 'http://hl7.org/fhir/Practitioner/21')
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle3(self):
        inst = self.instantiate_from('endpoint-examples-general-template.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle3(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle3(inst2)

    def implBundle3(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/71').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/71')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/72').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/72')
        self.assertEqual(inst.entry[2].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/73').value)
        self.assertEqual(inst.entry[2].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/73')
        self.assertEqual(inst.entry[3].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/74').value)
        self.assertEqual(inst.entry[3].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/74')
        self.assertEqual(inst.entry[4].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/75').value)
        self.assertEqual(inst.entry[4].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/75')
        self.assertEqual(inst.entry[5].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/76').value)
        self.assertEqual(inst.entry[5].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/76')
        self.assertEqual(inst.entry[6].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/77').value)
        self.assertEqual(inst.entry[6].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/77')
        self.assertEqual(inst.entry[7].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/78').value)
        self.assertEqual(inst.entry[7].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/78')
        self.assertEqual(inst.entry[8].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/79').value)
        self.assertEqual(inst.entry[8].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/79')
        self.assertEqual(inst.entry[9].fullUrl.value, FHIRUri('http://hl7.org/fhir/Endpoint/80').value)
        self.assertEqual(inst.entry[9].fullUrl.as_json(), 'http://hl7.org/fhir/Endpoint/80')
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle4(self):
        inst = self.instantiate_from('location-examples-general.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle4(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle4(inst2)

    def implBundle4(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('http://hl7.org/fhir/Location/2').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'http://hl7.org/fhir/Location/2')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('http://hl7.org/fhir/Location/3').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'http://hl7.org/fhir/Location/3')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle5(self):
        inst = self.instantiate_from('diagnosticreport-example-ghp.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle5(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle5(inst2)

    def implBundle5(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('https://example.com/base/DiagnosticReport/ghp').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'https://example.com/base/DiagnosticReport/ghp')
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.value, FHIRInstant('2015-08-16T10:35:23Z').value)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), '2015-08-16T10:35:23Z')
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRInstant('2015-08-16T10:35:23Z').date)
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('https://example.com/base/Specimen/rtt').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'https://example.com/base/Specimen/rtt')
        self.assertEqual(inst.entry[2].fullUrl.value, FHIRUri('https://example.com/base/Specimen/ltt').value)
        self.assertEqual(inst.entry[2].fullUrl.as_json(), 'https://example.com/base/Specimen/ltt')
        self.assertEqual(inst.entry[3].fullUrl.value, FHIRUri('https://example.com/base/Specimen/urine').value)
        self.assertEqual(inst.entry[3].fullUrl.as_json(), 'https://example.com/base/Specimen/urine')
        self.assertEqual(inst.entry[4].fullUrl.value, FHIRUri('https://example.com/base/Observation/p2').value)
        self.assertEqual(inst.entry[4].fullUrl.as_json(), 'https://example.com/base/Observation/p2')
        self.assertEqual(inst.entry[5].fullUrl.value, FHIRUri('https://example.com/base/Observation/r1').value)
        self.assertEqual(inst.entry[5].fullUrl.as_json(), 'https://example.com/base/Observation/r1')
        self.assertEqual(inst.entry[6].fullUrl.value, FHIRUri('https://example.com/base/Observation/r2').value)
        self.assertEqual(inst.entry[6].fullUrl.as_json(), 'https://example.com/base/Observation/r2')
        self.assertEqual(inst.entry[7].fullUrl.value, FHIRUri('https://example.com/base/Observation/r3').value)
        self.assertEqual(inst.entry[7].fullUrl.as_json(), 'https://example.com/base/Observation/r3')
        self.assertEqual(inst.entry[8].fullUrl.value, FHIRUri('https://example.com/base/Observation/r4').value)
        self.assertEqual(inst.entry[8].fullUrl.as_json(), 'https://example.com/base/Observation/r4')
        self.assertEqual(inst.entry[9].fullUrl.value, FHIRUri('https://example.com/base/Observation/r5').value)
        self.assertEqual(inst.entry[9].fullUrl.as_json(), 'https://example.com/base/Observation/r5')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle6(self):
        inst = self.instantiate_from('diagnosticreport-hla-genetics-results-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle6(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle6(inst2)

    def implBundle6(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('urn:uuid:b0a4b18e-94e7-4b1b-8031-c7ae4bdd8db9').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'urn:uuid:b0a4b18e-94e7-4b1b-8031-c7ae4bdd8db9')
        self.assertEqual(inst.entry[0].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[0].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[0].request.url.value, FHIRUri('DiagnosticReport').value)
        self.assertEqual(inst.entry[0].request.url.as_json(), 'DiagnosticReport')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('urn:uuid:8200dab6-18a2-4550-b913-a7db480c0804').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'urn:uuid:8200dab6-18a2-4550-b913-a7db480c0804')
        self.assertEqual(inst.entry[1].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[1].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[1].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[1].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[2].fullUrl.value, FHIRUri('urn:uuid:7c393185-f15c-45bc-a714-c0fdbea32675').value)
        self.assertEqual(inst.entry[2].fullUrl.as_json(), 'urn:uuid:7c393185-f15c-45bc-a714-c0fdbea32675')
        self.assertEqual(inst.entry[2].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[2].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[2].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[2].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[3].fullUrl.value, FHIRUri('urn:uuid:65c85f14-c3a0-4b72-818f-820e04fcc621').value)
        self.assertEqual(inst.entry[3].fullUrl.as_json(), 'urn:uuid:65c85f14-c3a0-4b72-818f-820e04fcc621')
        self.assertEqual(inst.entry[3].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[3].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[3].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[3].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[4].fullUrl.value, FHIRUri('urn:uuid:fbba9fe7-0ece-4ec1-9233-a437a8d242a0').value)
        self.assertEqual(inst.entry[4].fullUrl.as_json(), 'urn:uuid:fbba9fe7-0ece-4ec1-9233-a437a8d242a0')
        self.assertEqual(inst.entry[4].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[4].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[4].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[4].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[5].fullUrl.value, FHIRUri('urn:uuid:cbabf93e-1b4b-46f2-ba1e-d84862670670').value)
        self.assertEqual(inst.entry[5].fullUrl.as_json(), 'urn:uuid:cbabf93e-1b4b-46f2-ba1e-d84862670670')
        self.assertEqual(inst.entry[5].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[5].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[5].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[5].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[6].fullUrl.value, FHIRUri('urn:uuid:c233ad3d-1572-48d6-93da-0a583535e138').value)
        self.assertEqual(inst.entry[6].fullUrl.as_json(), 'urn:uuid:c233ad3d-1572-48d6-93da-0a583535e138')
        self.assertEqual(inst.entry[6].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[6].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[6].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[6].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[7].fullUrl.value, FHIRUri('urn:uuid:05fa52d7-5c67-460a-8722-d3460b24d6fe').value)
        self.assertEqual(inst.entry[7].fullUrl.as_json(), 'urn:uuid:05fa52d7-5c67-460a-8722-d3460b24d6fe')
        self.assertEqual(inst.entry[7].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[7].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[7].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[7].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[8].fullUrl.value, FHIRUri('urn:uuid:db69e549-6267-4777-b4b9-8813f3329309').value)
        self.assertEqual(inst.entry[8].fullUrl.as_json(), 'urn:uuid:db69e549-6267-4777-b4b9-8813f3329309')
        self.assertEqual(inst.entry[8].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[8].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[8].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[8].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.entry[9].fullUrl.value, FHIRUri('urn:uuid:bb55c2bc-5ad2-4bc1-8ff3-c407d06b12d0').value)
        self.assertEqual(inst.entry[9].fullUrl.as_json(), 'urn:uuid:bb55c2bc-5ad2-4bc1-8ff3-c407d06b12d0')
        self.assertEqual(inst.entry[9].request.method.value, FHIRCode('POST').value)
        self.assertEqual(inst.entry[9].request.method.as_json(), 'POST')
        self.assertEqual(inst.entry[9].request.url.value, FHIRUri('MolecularSequence').value)
        self.assertEqual(inst.entry[9].request.url.as_json(), 'MolecularSequence')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('transaction').value)
        self.assertEqual(inst.type.as_json(), 'transaction')

    def testBundle7(self):
        inst = self.instantiate_from('diagnosticreport-example-f202-bloodculture.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle7(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle7(inst2)

    def implBundle7(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('https://example.com/base/DiagnosticReport/f202').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'https://example.com/base/DiagnosticReport/f202')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('https://example.com/base/ServiceRequest/req').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'https://example.com/base/ServiceRequest/req')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle8(self):
        inst = self.instantiate_from('bundle-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle8(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle8(inst2)

    def implBundle8(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('https://example.com/base/MedicationRequest/3123').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'https://example.com/base/MedicationRequest/3123')
        self.assertEqual(inst.entry[0].search.mode.value, FHIRCode('match').value)
        self.assertEqual(inst.entry[0].search.mode.as_json(), 'match')
        self.assertEqual(inst.entry[0].search.score, 1)
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('https://example.com/base/Medication/example').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'https://example.com/base/Medication/example')
        self.assertEqual(inst.entry[1].search.mode.value, FHIRCode('include').value)
        self.assertEqual(inst.entry[1].search.mode.as_json(), 'include')
        self.assertEqual(inst.link[0].relation.value, FHIRString('self').value)
        self.assertEqual(inst.link[0].relation.as_json(), 'self')
        self.assertEqual(inst.link[0].url.value, FHIRUri('https://example.com/base/MedicationRequest?patient=347&_include=MedicationRequest.medication&_count=2').value)
        self.assertEqual(inst.link[0].url.as_json(), 'https://example.com/base/MedicationRequest?patient=347&_include=MedicationRequest.medication&_count=2')
        self.assertEqual(inst.link[1].relation.value, FHIRString('next').value)
        self.assertEqual(inst.link[1].relation.as_json(), 'next')
        self.assertEqual(inst.link[1].url.value, FHIRUri('https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2').value)
        self.assertEqual(inst.link[1].url.as_json(), 'https://example.com/base/MedicationRequest?patient=347&searchId=ff15fd40-ff71-4b48-b366-09c706bed9d0&page=2')
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant('2014-08-18T01:43:30Z').value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), '2014-08-18T01:43:30Z')
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2014-08-18T01:43:30Z').date)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.total.value, FHIRUnsignedInt('3').value)
        self.assertEqual(inst.total.as_json(), 3)
        self.assertEqual(inst.type.value, FHIRCode('searchset').value)
        self.assertEqual(inst.type.as_json(), 'searchset')

    def testBundle9(self):
        inst = self.instantiate_from('diagnosticreport-example-f001-bloodexam.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle9(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle9(inst2)

    def implBundle9(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('https://example.com/base/DiagnosticReport/f001').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'https://example.com/base/DiagnosticReport/f001')
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('https://example.com/base/ServiceRequest/req').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'https://example.com/base/ServiceRequest/req')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')

    def testBundle10(self):
        inst = self.instantiate_from('patient-examples-general.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Bundle instance')
        self.implBundle10(inst)

        js = inst.as_json()
        self.assertEqual("Bundle", js["resourceType"])
        inst2 = bundle.Bundle(js)
        self.implBundle10(inst2)

    def implBundle10(self, inst):
        self.assertEqual(inst.entry[0].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/1').value)
        self.assertEqual(inst.entry[0].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/1')
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[0].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[1].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/2').value)
        self.assertEqual(inst.entry[1].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/2')
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[1].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[2].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/3').value)
        self.assertEqual(inst.entry[2].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/3')
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[2].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[3].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/4').value)
        self.assertEqual(inst.entry[3].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/4')
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[3].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[4].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/5').value)
        self.assertEqual(inst.entry[4].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/5')
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[4].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[5].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/6').value)
        self.assertEqual(inst.entry[5].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/6')
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[5].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[6].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/7').value)
        self.assertEqual(inst.entry[6].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/7')
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[6].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[7].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/8').value)
        self.assertEqual(inst.entry[7].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/8')
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[7].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[8].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/9').value)
        self.assertEqual(inst.entry[8].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/9')
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[8].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.entry[9].fullUrl.value, FHIRUri('http://hl7.org/fhir/Patient/10').value)
        self.assertEqual(inst.entry[9].fullUrl.as_json(), 'http://hl7.org/fhir/Patient/10')
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.entry[9].resource.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant('2012-05-29T23:45:32Z').value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), '2012-05-29T23:45:32Z')
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2012-05-29T23:45:32Z').date)
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.type.value, FHIRCode('collection').value)
        self.assertEqual(inst.type.as_json(), 'collection')


from fhirclient.models.fhirdatatypes import FHIRUri, FHIRInstant, FHIRCode, FHIRString, FHIRId, FHIRUnsignedInt