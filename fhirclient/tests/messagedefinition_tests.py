#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import messagedefinition

class MessageDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MessageDefinition", js["resourceType"])
        return messagedefinition.MessageDefinition(js)

    def testMessageDefinition1(self):
        inst = self.instantiate_from('messagedefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MessageDefinition instance')
        self.implMessageDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("MessageDefinition", js["resourceType"])
        inst2 = messagedefinition.MessageDefinition(js)
        self.implMessageDefinition1(inst2)

    def implMessageDefinition1(self, inst):
        self.assertEqual(inst.category.value, FHIRCode('notification').value)
        self.assertEqual(inst.category.as_json(), 'notification')
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode('url').value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), 'url')
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString('http://hl7.org').value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), 'http://hl7.org')
        self.assertEqual(inst.date.value, FHIRDateTime('2016-11-09').value)
        self.assertEqual(inst.date.as_json(), '2016-11-09')
        self.assertEqual(inst.eventCoding.code.value, FHIRCode('admin-notify').value)
        self.assertEqual(inst.eventCoding.code.as_json(), 'admin-notify')
        self.assertEqual(inst.eventCoding.system.value, FHIRUri('http://example.org/fhir/message-events').value)
        self.assertEqual(inst.eventCoding.system.as_json(), 'http://example.org/fhir/message-events')
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.name.value, FHIRString('EXAMPLE').value)
        self.assertEqual(inst.name.as_json(), 'EXAMPLE')
        self.assertEqual(inst.publisher.value, FHIRString('Health Level Seven, Int\'l').value)
        self.assertEqual(inst.publisher.as_json(), 'Health Level Seven, Int\'l')
        self.assertEqual(inst.purpose.value, FHIRMarkdown('Defines a base example for other MessageDefinition instances.').value)
        self.assertEqual(inst.purpose.as_json(), 'Defines a base example for other MessageDefinition instances.')
        self.assertEqual(inst.status.value, FHIRCode('draft').value)
        self.assertEqual(inst.status.as_json(), 'draft')
        self.assertEqual(inst.text.div.value, FHIRString('<div xmlns="http://www.w3.org/1999/xhtml">Message definition base example</div>').value)
        self.assertEqual(inst.text.div.as_json(), '<div xmlns="http://www.w3.org/1999/xhtml">Message definition base example</div>')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.title.value, FHIRString('Message definition base example').value)
        self.assertEqual(inst.title.as_json(), 'Message definition base example')
        self.assertEqual(inst.url.value, FHIRUri('http://hl7.org/fhir/MessageDefinition/example').value)
        self.assertEqual(inst.url.as_json(), 'http://hl7.org/fhir/MessageDefinition/example')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRDateTime, FHIRUri, FHIRMarkdown