#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import eventdefinition

class EventDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EventDefinition", js["resourceType"])
        return eventdefinition.EventDefinition(js)

    def testEventDefinition1(self):
        inst = self.instantiate_from('eventdefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a EventDefinition instance')
        self.implEventDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("EventDefinition", js["resourceType"])
        inst2 = eventdefinition.EventDefinition(js)
        self.implEventDefinition1(inst2)

    def implEventDefinition1(self, inst):
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.purpose.value, FHIRMarkdown("Monitor all admissions to Emergency").value)
        self.assertEqual(inst.purpose.as_json(), "Monitor all admissions to Emergency")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.trigger[0].condition.description.value, FHIRString("Encounter Location = emergency (active/completed encounters, current or previous)").value)
        self.assertEqual(inst.trigger[0].condition.description.as_json(), "Encounter Location = emergency (active/completed encounters, current or previous)")
        self.assertEqual(inst.trigger[0].condition.expression.value, FHIRString("(this | %previous).location.where(location = 'Location/emergency' and status in {'active', 'completed'}).exists()").value)
        self.assertEqual(inst.trigger[0].condition.expression.as_json(), "(this | %previous).location.where(location = 'Location/emergency' and status in {'active', 'completed'}).exists()")
        self.assertEqual(inst.trigger[0].condition.language.value, FHIRCode("text/fhirpath").value)
        self.assertEqual(inst.trigger[0].condition.language.as_json(), "text/fhirpath")
        self.assertEqual(inst.trigger[0].data[0].type.value, FHIRCode("Encounter").value)
        self.assertEqual(inst.trigger[0].data[0].type.as_json(), "Encounter")
        self.assertEqual(inst.trigger[0].name.value, FHIRString("monitor-emergency-admissions").value)
        self.assertEqual(inst.trigger[0].name.as_json(), "monitor-emergency-admissions")
        self.assertEqual(inst.trigger[0].type.value, FHIRCode("named-event").value)
        self.assertEqual(inst.trigger[0].type.as_json(), "named-event")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri, FHIRMarkdown