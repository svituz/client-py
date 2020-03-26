#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import messageheader

class MessageHeaderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MessageHeader", js["resourceType"])
        return messageheader.MessageHeader(js)

    def testMessageHeader1(self):
        inst = self.instantiate_from('messageheader-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MessageHeader instance')
        self.implMessageHeader1(inst)

        js = inst.as_json()
        self.assertEqual("MessageHeader", js["resourceType"])
        inst2 = messageheader.MessageHeader(js)
        self.implMessageHeader1(inst2)

    def implMessageHeader1(self, inst):
        self.assertEqual(inst.definition.value, FHIRCanonical("http:////acme.com/ehr/fhir/messagedefinition/patientrequest").value)
        self.assertEqual(inst.definition.as_json(), "http:////acme.com/ehr/fhir/messagedefinition/patientrequest")
        self.assertEqual(inst.destination[0].endpoint.value, FHIRUrl("llp:10.11.12.14:5432").value)
        self.assertEqual(inst.destination[0].endpoint.as_json(), "llp:10.11.12.14:5432")
        self.assertEqual(inst.destination[0].name.value, FHIRString("Acme Message Gateway").value)
        self.assertEqual(inst.destination[0].name.as_json(), "Acme Message Gateway")
        self.assertEqual(inst.eventCoding.code.value, FHIRCode("admin-notify").value)
        self.assertEqual(inst.eventCoding.code.as_json(), "admin-notify")
        self.assertEqual(inst.eventCoding.system.value, FHIRUri("http://example.org/fhir/message-events").value)
        self.assertEqual(inst.eventCoding.system.as_json(), "http://example.org/fhir/message-events")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reason.coding[0].code.value, FHIRCode("admit").value)
        self.assertEqual(inst.reason.coding[0].code.as_json(), "admit")
        self.assertEqual(inst.reason.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/message-reasons-encounter").value)
        self.assertEqual(inst.reason.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/message-reasons-encounter")
        self.assertEqual(inst.response.code.value, FHIRCode("ok").value)
        self.assertEqual(inst.response.code.as_json(), "ok")
        self.assertEqual(inst.response.identifier.value, FHIRId("5015fe84-8e76-4526-89d8-44b322e8d4fb").value)
        self.assertEqual(inst.response.identifier.as_json(), "5015fe84-8e76-4526-89d8-44b322e8d4fb")
        self.assertEqual(inst.source.contact.system.value, FHIRCode("phone").value)
        self.assertEqual(inst.source.contact.system.as_json(), "phone")
        self.assertEqual(inst.source.contact.value.value, FHIRString("+1 (555) 123 4567").value)
        self.assertEqual(inst.source.contact.value.as_json(), "+1 (555) 123 4567")
        self.assertEqual(inst.source.endpoint.value, FHIRUrl("llp:10.11.12.13:5432").value)
        self.assertEqual(inst.source.endpoint.as_json(), "llp:10.11.12.13:5432")
        self.assertEqual(inst.source.name.value, FHIRString("Acme Central Patient Registry").value)
        self.assertEqual(inst.source.name.as_json(), "Acme Central Patient Registry")
        self.assertEqual(inst.source.software.value, FHIRString("FooBar Patient Manager").value)
        self.assertEqual(inst.source.software.as_json(), "FooBar Patient Manager")
        self.assertEqual(inst.source.version.value, FHIRString("3.1.45.AABB").value)
        self.assertEqual(inst.source.version.as_json(), "3.1.45.AABB")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCanonical, FHIRUrl, FHIRString, FHIRCode, FHIRUri, FHIRId