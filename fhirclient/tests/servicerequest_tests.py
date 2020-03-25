#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import servicerequest

class ServiceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ServiceRequest", js["resourceType"])
        return servicerequest.ServiceRequest(js)

    def testServiceRequest1(self):
        inst = self.instantiate_from('servicerequest-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest1(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest1(inst2)

    def implServiceRequest1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode('103693007').value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), '103693007')
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString('Diagnostic procedure (procedure)').value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), 'Diagnostic procedure (procedure)')
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.category[0].text.value, FHIRString('Diagnostics Procedure').value)
        self.assertEqual(inst.category[0].text.as_json(), 'Diagnostics Procedure')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('303653007').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '303653007')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Computed tomography of head').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Computed tomography of head')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.text.div.value, FHIRString('<div xmlns="http://www.w3.org/1999/xhtml">To be added</div>').value)
        self.assertEqual(inst.text.div.as_json(), '<div xmlns="http://www.w3.org/1999/xhtml">To be added</div>')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest2(self):
        inst = self.instantiate_from('servicerequest-example-myringotomy.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest2(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest2(inst2)

    def implServiceRequest2(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime('2014-02-14').value)
        self.assertEqual(inst.authoredOn.as_json(), '2014-02-14')
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode('103696004').value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), '103696004')
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString('Patient referral to specialist').value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), 'Patient referral to specialist')
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('172676009').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '172676009')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Myringotomy and insertion of tympanic ventilation tube').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Myringotomy and insertion of tympanic ventilation tube')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.code.text.value, FHIRString('Insertion of grommets').value)
        self.assertEqual(inst.code.text.as_json(), 'Insertion of grommets')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://orionhealth.com/fhir/apps/referralids').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://orionhealth.com/fhir/apps/referralids')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('ret4421').value)
        self.assertEqual(inst.identifier[0].value.as_json(), 'ret4421')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.note[0].authorString.value, FHIRString('Serena Shrink').value)
        self.assertEqual(inst.note[0].authorString.as_json(), 'Serena Shrink')
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown('In the past 2 years Beverly has had 6 instances of rt-sided Otitis media. She is     falling behind her peers at school, and displaying some learning difficulties.').value)
        self.assertEqual(inst.note[0].text.as_json(), 'In the past 2 years Beverly has had 6 instances of rt-sided Otitis media. She is     falling behind her peers at school, and displaying some learning difficulties.')
        self.assertEqual(inst.note[0].time.value, FHIRDateTime('2014-02-14').value)
        self.assertEqual(inst.note[0].time.as_json(), '2014-02-14')
        self.assertEqual(inst.occurrencePeriod.end.value, FHIRDateTime('2014-03-14').value)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), '2014-03-14')
        self.assertEqual(inst.performerType.coding[0].code.value, FHIRCode('ent').value)
        self.assertEqual(inst.performerType.coding[0].code.as_json(), 'ent')
        self.assertEqual(inst.performerType.coding[0].display.value, FHIRString('ENT').value)
        self.assertEqual(inst.performerType.coding[0].display.as_json(), 'ENT')
        self.assertEqual(inst.performerType.coding[0].system.value, FHIRUri('http://orionhealth.com/fhir/apps/specialties').value)
        self.assertEqual(inst.performerType.coding[0].system.as_json(), 'http://orionhealth.com/fhir/apps/specialties')
        self.assertEqual(inst.priority.value, FHIRCode('routine').value)
        self.assertEqual(inst.priority.as_json(), 'routine')
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString('For consideration of Grommets').value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), 'For consideration of Grommets')
        self.assertEqual(inst.requisition.value.value, FHIRString('1234').value)
        self.assertEqual(inst.requisition.value.as_json(), '1234')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest3(self):
        inst = self.instantiate_from('servicerequest-example3.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest3(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest3(inst2)

    def implServiceRequest3(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime('2017-02-01T17:23:07Z').value)
        self.assertEqual(inst.authoredOn.as_json(), '2017-02-01T17:23:07Z')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('359962006').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '359962006')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Turning patient in bed (procedure)').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Turning patient in bed (procedure)')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertTrue(inst.doNotPerform)
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://goodhealth.org/placer-ids').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://goodhealth.org/placer-ids')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('20170201-0002').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '20170201-0002')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.priority.value, FHIRCode('stat').value)
        self.assertEqual(inst.priority.as_json(), 'stat')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest4(self):
        inst = self.instantiate_from('servicerequest-example-pt.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest4(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest4(inst2)

    def implServiceRequest4(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime('2016-09-20').value)
        self.assertEqual(inst.authoredOn.as_json(), '2016-09-20')
        self.assertEqual(inst.bodySite[0].coding[0].code.value, FHIRCode('36701003').value)
        self.assertEqual(inst.bodySite[0].coding[0].code.as_json(), '36701003')
        self.assertEqual(inst.bodySite[0].coding[0].display.value, FHIRString('Both knees (body structure)').value)
        self.assertEqual(inst.bodySite[0].coding[0].display.as_json(), 'Both knees (body structure)')
        self.assertEqual(inst.bodySite[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.bodySite[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.bodySite[0].text.value, FHIRString('Both knees').value)
        self.assertEqual(inst.bodySite[0].text.as_json(), 'Both knees')
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode('386053000').value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), '386053000')
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString('Evaluation procedure (procedure)').value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), 'Evaluation procedure (procedure)')
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.category[0].text.value, FHIRString('Evaluation').value)
        self.assertEqual(inst.category[0].text.as_json(), 'Evaluation')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('710830005').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '710830005')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Assessment of passive range of motion (procedure)').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Assessment of passive range of motion (procedure)')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.code.text.value, FHIRString('Assessment of passive range of motion').value)
        self.assertEqual(inst.code.text.as_json(), 'Assessment of passive range of motion')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime('2016-09-27').value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), '2016-09-27')
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString('assessment of mobility limitations due to osteoarthritis').value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), 'assessment of mobility limitations due to osteoarthritis')
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest5(self):
        inst = self.instantiate_from('servicerequest-example-colonoscopy-bx.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest5(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest5(inst2)

    def implServiceRequest5(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime('2017-03-05').value)
        self.assertEqual(inst.authoredOn.as_json(), '2017-03-05')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('76164006').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '76164006')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Biopsy of colon (procedure)').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Biopsy of colon (procedure)')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.code.text.value, FHIRString('Biopsy of colon').value)
        self.assertEqual(inst.code.text.as_json(), 'Biopsy of colon')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('12345').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '12345')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.requisition.system.value, FHIRUri('http://bumc.org/requisitions').value)
        self.assertEqual(inst.requisition.system.as_json(), 'http://bumc.org/requisitions')
        self.assertEqual(inst.requisition.value.value, FHIRString('req12345').value)
        self.assertEqual(inst.requisition.value.as_json(), 'req12345')
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest6(self):
        inst = self.instantiate_from('servicerequest-example-appendectomy.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest6(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest6(inst2)

    def implServiceRequest6(self, inst):
        self.assertEqual(inst.code.text.value, FHIRString('Appendectomy').value)
        self.assertEqual(inst.code.text.as_json(), 'Appendectomy')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.text.status.value, FHIRCode('additional').value)
        self.assertEqual(inst.text.status.as_json(), 'additional')

    def testServiceRequest7(self):
        inst = self.instantiate_from('servicerequest-genetics-example-1.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest7(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest7(inst2)

    def implServiceRequest7(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('49874-1').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '49874-1')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://loinc.org').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://loinc.org')
        self.assertEqual(inst.code.text.value, FHIRString('ABCB4 gene mutation analysis').value)
        self.assertEqual(inst.code.text.as_json(), 'ABCB4 gene mutation analysis')
        self.assertEqual(inst.intent.value, FHIRCode('original-order').value)
        self.assertEqual(inst.intent.as_json(), 'original-order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime('2014-05-12T16:16:00-07:00').value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), '2014-05-12T16:16:00-07:00')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest8(self):
        inst = self.instantiate_from('servicerequest-example-lipid.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest8(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest8(inst2)

    def implServiceRequest8(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('LIPID').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), 'LIPID')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://acme.org/tests').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://acme.org/tests')
        self.assertEqual(inst.code.text.value, FHIRString('Lipid Panel').value)
        self.assertEqual(inst.code.text.as_json(), 'Lipid Panel')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('urn:oid:1.3.4.5.6.7').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'urn:oid:1.3.4.5.6.7')
        self.assertEqual(inst.identifier[0].type.coding[0].code.value, FHIRCode('PLAC').value)
        self.assertEqual(inst.identifier[0].type.coding[0].code.as_json(), 'PLAC')
        self.assertEqual(inst.identifier[0].type.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v2-0203').value)
        self.assertEqual(inst.identifier[0].type.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v2-0203')
        self.assertEqual(inst.identifier[0].type.text.value, FHIRString('Placer').value)
        self.assertEqual(inst.identifier[0].type.text.as_json(), 'Placer')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('2345234234234').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '2345234234234')
        self.assertEqual(inst.intent.value, FHIRCode('original-order').value)
        self.assertEqual(inst.intent.as_json(), 'original-order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown('patient is afraid of needles').value)
        self.assertEqual(inst.note[0].text.as_json(), 'patient is afraid of needles')
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime('2013-05-02T16:16:00-07:00').value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), '2013-05-02T16:16:00-07:00')
        self.assertEqual(inst.reasonCode[0].coding[0].code.value, FHIRCode('V173').value)
        self.assertEqual(inst.reasonCode[0].coding[0].code.as_json(), 'V173')
        self.assertEqual(inst.reasonCode[0].coding[0].display.value, FHIRString('Fam hx-ischem heart dis').value)
        self.assertEqual(inst.reasonCode[0].coding[0].display.as_json(), 'Fam hx-ischem heart dis')
        self.assertEqual(inst.reasonCode[0].coding[0].system.value, FHIRUri('http://hl7.org/fhir/sid/icd-9').value)
        self.assertEqual(inst.reasonCode[0].coding[0].system.as_json(), 'http://hl7.org/fhir/sid/icd-9')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest9(self):
        inst = self.instantiate_from('servicerequest-example-ob.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest9(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest9(inst2)

    def implServiceRequest9(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode('386637004').value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), '386637004')
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString('Obstetric procedure (procedure)').value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), 'Obstetric procedure (procedure)')
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.category[0].text.value, FHIRString('OB').value)
        self.assertEqual(inst.category[0].text.as_json(), 'OB')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('22633006').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '22633006')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Vaginal delivery, medical personnel present (procedure)').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Vaginal delivery, medical personnel present (procedure)')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.code.text.value, FHIRString('Vaginal delivery').value)
        self.assertEqual(inst.code.text.as_json(), 'Vaginal delivery')
        self.assertEqual(inst.intent.value, FHIRCode('order').value)
        self.assertEqual(inst.intent.as_json(), 'order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime('2012-06-02').value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), '2012-06-02')
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString('term pregnancy, active labor').value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), 'term pregnancy, active labor')
        self.assertEqual(inst.status.value, FHIRCode('completed').value)
        self.assertEqual(inst.status.as_json(), 'completed')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')

    def testServiceRequest10(self):
        inst = self.instantiate_from('servicerequest-example-di.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ServiceRequest instance')
        self.implServiceRequest10(inst)

        js = inst.as_json()
        self.assertEqual("ServiceRequest", js["resourceType"])
        inst2 = servicerequest.ServiceRequest(js)
        self.implServiceRequest10(inst2)

    def implServiceRequest10(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('24627-2').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '24627-2')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://loinc.org').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://loinc.org')
        self.assertEqual(inst.code.text.value, FHIRString('Chest CT').value)
        self.assertEqual(inst.code.text.as_json(), 'Chest CT')
        self.assertEqual(inst.intent.value, FHIRCode('original-order').value)
        self.assertEqual(inst.intent.as_json(), 'original-order')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime('2013-05-08T09:33:27+07:00').value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), '2013-05-08T09:33:27+07:00')
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString('Check for metastatic disease').value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), 'Check for metastatic disease')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime, FHIRMarkdown