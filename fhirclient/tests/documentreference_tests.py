#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import documentreference

class DocumentReferenceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentReference", js["resourceType"])
        return documentreference.DocumentReference(js)

    def testDocumentReference1(self):
        inst = self.instantiate_from('documentreference-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DocumentReference instance')
        self.implDocumentReference1(inst)

        js = inst.as_json()
        self.assertEqual("DocumentReference", js["resourceType"])
        inst2 = documentreference.DocumentReference(js)
        self.implDocumentReference1(inst2)

    def implDocumentReference1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode('History and Physical').value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), 'History and Physical')
        self.assertEqual(inst.category[0].coding[0].display.value, FHIRString('History and Physical').value)
        self.assertEqual(inst.category[0].coding[0].display.as_json(), 'History and Physical')
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri('http://ihe.net/xds/connectathon/classCodes').value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), 'http://ihe.net/xds/connectathon/classCodes')
        self.assertEqual(inst.content[0].attachment.contentType.value, FHIRCode('application/hl7-v3+xml').value)
        self.assertEqual(inst.content[0].attachment.contentType.as_json(), 'application/hl7-v3+xml')
        self.assertEqual(inst.content[0].attachment.creation.value, FHIRDateTime('2005-12-24T09:35:00+11:00').value)
        self.assertEqual(inst.content[0].attachment.creation.as_json(), '2005-12-24T09:35:00+11:00')
        self.assertEqual(inst.content[0].attachment.hash.value, FHIRBase64Binary('2jmj7l5rSw0yVb/vlWAYkK/YBwk=').value)
        self.assertEqual(inst.content[0].attachment.hash.as_json(), '2jmj7l5rSw0yVb/vlWAYkK/YBwk=')
        self.assertEqual(inst.content[0].attachment.language.value, FHIRCode('en-US').value)
        self.assertEqual(inst.content[0].attachment.language.as_json(), 'en-US')
        self.assertEqual(inst.content[0].attachment.size.value, FHIRUnsignedInt('3654').value)
        self.assertEqual(inst.content[0].attachment.size.as_json(), 3654)
        self.assertEqual(inst.content[0].attachment.title.value, FHIRString('Physical').value)
        self.assertEqual(inst.content[0].attachment.title.as_json(), 'Physical')
        self.assertEqual(inst.content[0].attachment.url.value, FHIRUrl('http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510').value)
        self.assertEqual(inst.content[0].attachment.url.as_json(), 'http://example.org/xds/mhd/Binary/07a6483f-732b-461e-86b6-edb665c45510')
        self.assertEqual(inst.content[0].format.code.value, FHIRCode('urn:ihe:pcc:handp:2008').value)
        self.assertEqual(inst.content[0].format.code.as_json(), 'urn:ihe:pcc:handp:2008')
        self.assertEqual(inst.content[0].format.display.value, FHIRString('History and Physical Specification').value)
        self.assertEqual(inst.content[0].format.display.as_json(), 'History and Physical Specification')
        self.assertEqual(inst.content[0].format.system.value, FHIRUri('urn:oid:1.3.6.1.4.1.19376.1.2.3').value)
        self.assertEqual(inst.content[0].format.system.as_json(), 'urn:oid:1.3.6.1.4.1.19376.1.2.3')
        self.assertEqual(inst.context.event[0].coding[0].code.value, FHIRCode('T-D8200').value)
        self.assertEqual(inst.context.event[0].coding[0].code.as_json(), 'T-D8200')
        self.assertEqual(inst.context.event[0].coding[0].display.value, FHIRString('Arm').value)
        self.assertEqual(inst.context.event[0].coding[0].display.as_json(), 'Arm')
        self.assertEqual(inst.context.event[0].coding[0].system.value, FHIRUri('http://ihe.net/xds/connectathon/eventCodes').value)
        self.assertEqual(inst.context.event[0].coding[0].system.as_json(), 'http://ihe.net/xds/connectathon/eventCodes')
        self.assertEqual(inst.context.facilityType.coding[0].code.value, FHIRCode('Outpatient').value)
        self.assertEqual(inst.context.facilityType.coding[0].code.as_json(), 'Outpatient')
        self.assertEqual(inst.context.facilityType.coding[0].display.value, FHIRString('Outpatient').value)
        self.assertEqual(inst.context.facilityType.coding[0].display.as_json(), 'Outpatient')
        self.assertEqual(inst.context.facilityType.coding[0].system.value, FHIRUri('http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes').value)
        self.assertEqual(inst.context.facilityType.coding[0].system.as_json(), 'http://www.ihe.net/xds/connectathon/healthcareFacilityTypeCodes')
        self.assertEqual(inst.context.period.end.value, FHIRDateTime('2004-12-23T08:01:00+11:00').value)
        self.assertEqual(inst.context.period.end.as_json(), '2004-12-23T08:01:00+11:00')
        self.assertEqual(inst.context.period.start.value, FHIRDateTime('2004-12-23T08:00:00+11:00').value)
        self.assertEqual(inst.context.period.start.as_json(), '2004-12-23T08:00:00+11:00')
        self.assertEqual(inst.context.practiceSetting.coding[0].code.value, FHIRCode('General Medicine').value)
        self.assertEqual(inst.context.practiceSetting.coding[0].code.as_json(), 'General Medicine')
        self.assertEqual(inst.context.practiceSetting.coding[0].display.value, FHIRString('General Medicine').value)
        self.assertEqual(inst.context.practiceSetting.coding[0].display.as_json(), 'General Medicine')
        self.assertEqual(inst.context.practiceSetting.coding[0].system.value, FHIRUri('http://www.ihe.net/xds/connectathon/practiceSettingCodes').value)
        self.assertEqual(inst.context.practiceSetting.coding[0].system.as_json(), 'http://www.ihe.net/xds/connectathon/practiceSettingCodes')
        self.assertEqual(inst.date.value, FHIRInstant('2005-12-24T09:43:41+11:00').value)
        self.assertEqual(inst.date.as_json(), '2005-12-24T09:43:41+11:00')
        self.assertEqual(inst.date.date, FHIRInstant('2005-12-24T09:43:41+11:00').date)
        self.assertEqual(inst.description.value, FHIRString('Physical').value)
        self.assertEqual(inst.description.as_json(), 'Physical')
        self.assertEqual(inst.docStatus.value, FHIRCode('preliminary').value)
        self.assertEqual(inst.docStatus.as_json(), 'preliminary')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('urn:ietf:rfc:3986').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'urn:ietf:rfc:3986')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234').value)
        self.assertEqual(inst.identifier[0].value.as_json(), 'urn:oid:1.3.6.1.4.1.21367.2005.3.7.1234')
        self.assertEqual(inst.masterIdentifier.system.value, FHIRUri('urn:ietf:rfc:3986').value)
        self.assertEqual(inst.masterIdentifier.system.as_json(), 'urn:ietf:rfc:3986')
        self.assertEqual(inst.masterIdentifier.value.value, FHIRString('urn:oid:1.3.6.1.4.1.21367.2005.3.7').value)
        self.assertEqual(inst.masterIdentifier.value.as_json(), 'urn:oid:1.3.6.1.4.1.21367.2005.3.7')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.relatesTo[0].code.value, FHIRCode('appends').value)
        self.assertEqual(inst.relatesTo[0].code.as_json(), 'appends')
        self.assertEqual(inst.securityLabel[0].coding[0].code.value, FHIRCode('V').value)
        self.assertEqual(inst.securityLabel[0].coding[0].code.as_json(), 'V')
        self.assertEqual(inst.securityLabel[0].coding[0].display.value, FHIRString('very restricted').value)
        self.assertEqual(inst.securityLabel[0].coding[0].display.as_json(), 'very restricted')
        self.assertEqual(inst.securityLabel[0].coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-Confidentiality').value)
        self.assertEqual(inst.securityLabel[0].coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-Confidentiality')
        self.assertEqual(inst.status.value, FHIRCode('current').value)
        self.assertEqual(inst.status.as_json(), 'current')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode('34108-1').value)
        self.assertEqual(inst.type.coding[0].code.as_json(), '34108-1')
        self.assertEqual(inst.type.coding[0].display.value, FHIRString('Outpatient Note').value)
        self.assertEqual(inst.type.coding[0].display.as_json(), 'Outpatient Note')
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri('http://loinc.org').value)
        self.assertEqual(inst.type.coding[0].system.as_json(), 'http://loinc.org')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime, FHIRBase64Binary, FHIRUnsignedInt, FHIRUrl, FHIRInstant