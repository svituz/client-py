#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import subscription

class SubscriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Subscription", js["resourceType"])
        return subscription.Subscription(js)

    def testSubscription1(self):
        inst = self.instantiate_from('subscription-example-error.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Subscription instance')
        self.implSubscription1(inst)

        js = inst.as_json()
        self.assertEqual("Subscription", js["resourceType"])
        inst2 = subscription.Subscription(js)
        self.implSubscription1(inst2)

    def implSubscription1(self, inst):
        self.assertEqual(inst.channel.endpoint.value, FHIRUrl("https://biliwatch.com/customers/mount-auburn-miu/on-result").value)
        self.assertEqual(inst.channel.endpoint.as_json(), "https://biliwatch.com/customers/mount-auburn-miu/on-result")
        self.assertEqual(inst.channel.header[0].value, FHIRString("Authorization: Bearer secret-token-abc-123").value)
        self.assertEqual(inst.channel.header[0].as_json(), "Authorization: Bearer secret-token-abc-123")
        self.assertEqual(inst.channel.payload.value, FHIRCode("application/fhir+json").value)
        self.assertEqual(inst.channel.payload.as_json(), "application/fhir+json")
        self.assertEqual(inst.channel.type.value, FHIRCode("rest-hook").value)
        self.assertEqual(inst.channel.type.as_json(), "rest-hook")
        self.assertEqual(inst.contact[0].system.value, FHIRCode("phone").value)
        self.assertEqual(inst.contact[0].system.as_json(), "phone")
        self.assertEqual(inst.contact[0].value.value, FHIRString("ext 4123").value)
        self.assertEqual(inst.contact[0].value.as_json(), "ext 4123")
        self.assertEqual(inst.criteria.value, FHIRString("Observation?code=http://loinc.org|1975-2").value)
        self.assertEqual(inst.criteria.as_json(), "Observation?code=http://loinc.org|1975-2")
        self.assertEqual(inst.end.value, FHIRInstant("2021-01-01T00:00:00Z").value)
        self.assertEqual(inst.end.as_json(), "2021-01-01T00:00:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2021-01-01T00:00:00Z').date)
        self.assertEqual(inst.error.value, FHIRString("Socket Error 10060 - can't connect to host").value)
        self.assertEqual(inst.error.as_json(), "Socket Error 10060 - can't connect to host")
        self.assertEqual(inst.id.value, FHIRString("example-error").value)
        self.assertEqual(inst.id.as_json(), "example-error")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reason.value, FHIRString("Monitor new neonatal function").value)
        self.assertEqual(inst.reason.as_json(), "Monitor new neonatal function")
        self.assertEqual(inst.status.value, FHIRCode("error").value)
        self.assertEqual(inst.status.as_json(), "error")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testSubscription2(self):
        inst = self.instantiate_from('subscription-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Subscription instance')
        self.implSubscription2(inst)

        js = inst.as_json()
        self.assertEqual("Subscription", js["resourceType"])
        inst2 = subscription.Subscription(js)
        self.implSubscription2(inst2)

    def implSubscription2(self, inst):
        self.assertEqual(inst.channel.endpoint.value, FHIRUrl("https://biliwatch.com/customers/mount-auburn-miu/on-result").value)
        self.assertEqual(inst.channel.endpoint.as_json(), "https://biliwatch.com/customers/mount-auburn-miu/on-result")
        self.assertEqual(inst.channel.header[0].value, FHIRString("Authorization: Bearer secret-token-abc-123").value)
        self.assertEqual(inst.channel.header[0].as_json(), "Authorization: Bearer secret-token-abc-123")
        self.assertEqual(inst.channel.payload.value, FHIRCode("application/fhir+json").value)
        self.assertEqual(inst.channel.payload.as_json(), "application/fhir+json")
        self.assertEqual(inst.channel.type.value, FHIRCode("rest-hook").value)
        self.assertEqual(inst.channel.type.as_json(), "rest-hook")
        self.assertEqual(inst.contact[0].system.value, FHIRCode("phone").value)
        self.assertEqual(inst.contact[0].system.as_json(), "phone")
        self.assertEqual(inst.contact[0].value.value, FHIRString("ext 4123").value)
        self.assertEqual(inst.contact[0].value.as_json(), "ext 4123")
        self.assertEqual(inst.criteria.value, FHIRString("Observation?code=http://loinc.org|1975-2").value)
        self.assertEqual(inst.criteria.as_json(), "Observation?code=http://loinc.org|1975-2")
        self.assertEqual(inst.end.value, FHIRInstant("2021-01-01T00:00:00Z").value)
        self.assertEqual(inst.end.as_json(), "2021-01-01T00:00:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2021-01-01T00:00:00Z').date)
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.reason.value, FHIRString("Monitor new neonatal function").value)
        self.assertEqual(inst.reason.as_json(), "Monitor new neonatal function")
        self.assertEqual(inst.status.value, FHIRCode("requested").value)
        self.assertEqual(inst.status.as_json(), "requested")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRUrl, FHIRString, FHIRCode, FHIRInstant, FHIRUri