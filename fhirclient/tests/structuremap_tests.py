#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import structuremap

class StructureMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("StructureMap", js["resourceType"])
        return structuremap.StructureMap(js)

    def testStructureMap1(self):
        inst = self.instantiate_from('structuremap-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a StructureMap instance')
        self.implStructureMap1(inst)

        js = inst.as_json()
        self.assertEqual("StructureMap", js["resourceType"])
        inst2 = structuremap.StructureMap(js)
        self.implStructureMap1(inst2)

    def implStructureMap1(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.date.value, FHIRDateTime("2017-03-09").value)
        self.assertEqual(inst.date.as_json(), "2017-03-09")
        self.assertEqual(inst.description.value, FHIRMarkdown("Example Structure Map").value)
        self.assertEqual(inst.description.as_json(), "Example Structure Map")
        self.assertEqual(inst.group[0].documentation.value, FHIRString("test -> testValue").value)
        self.assertEqual(inst.group[0].documentation.as_json(), "test -> testValue")
        self.assertEqual(inst.group[0].input[0].mode.value, FHIRCode("source").value)
        self.assertEqual(inst.group[0].input[0].mode.as_json(), "source")
        self.assertEqual(inst.group[0].input[0].name.value, FHIRId("test").value)
        self.assertEqual(inst.group[0].input[0].name.as_json(), "test")
        self.assertEqual(inst.group[0].name.value, FHIRId("Examples").value)
        self.assertEqual(inst.group[0].name.as_json(), "Examples")
        self.assertEqual(inst.group[0].rule[0].name.value, FHIRId("rule1").value)
        self.assertEqual(inst.group[0].rule[0].name.as_json(), "rule1")
        self.assertEqual(inst.group[0].rule[0].source[0].context.value, FHIRId("Source").value)
        self.assertEqual(inst.group[0].rule[0].source[0].context.as_json(), "Source")
        self.assertEqual(inst.group[0].rule[0].source[0].element.value, FHIRString("test").value)
        self.assertEqual(inst.group[0].rule[0].source[0].element.as_json(), "test")
        self.assertEqual(inst.group[0].rule[0].source[0].type.value, FHIRString("SourceClassA").value)
        self.assertEqual(inst.group[0].rule[0].source[0].type.as_json(), "SourceClassA")
        self.assertEqual(inst.group[0].rule[0].source[0].variable.value, FHIRId("t").value)
        self.assertEqual(inst.group[0].rule[0].source[0].variable.as_json(), "t")
        self.assertEqual(inst.group[0].rule[0].target[0].context.value, FHIRId("Destination").value)
        self.assertEqual(inst.group[0].rule[0].target[0].context.as_json(), "Destination")
        self.assertEqual(inst.group[0].rule[0].target[0].contextType.value, FHIRCode("variable").value)
        self.assertEqual(inst.group[0].rule[0].target[0].contextType.as_json(), "variable")
        self.assertEqual(inst.group[0].rule[0].target[0].element.value, FHIRString("testValue").value)
        self.assertEqual(inst.group[0].rule[0].target[0].element.as_json(), "testValue")
        self.assertEqual(inst.group[0].rule[0].target[0].transform.value, FHIRCode("copy").value)
        self.assertEqual(inst.group[0].rule[0].target[0].transform.as_json(), "copy")
        self.assertEqual(inst.group[0].typeMode.value, FHIRCode("none").value)
        self.assertEqual(inst.group[0].typeMode.as_json(), "none")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:ietf:rfc:3986").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("urn:oid:37843577-95fb-4adb-84c0-8837188a7bf3").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "urn:oid:37843577-95fb-4adb-84c0-8837188a7bf3")
        self.assertEqual(inst.jurisdiction[0].coding[0].code.value, FHIRCode("009").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.as_json(), "009")
        self.assertEqual(inst.jurisdiction[0].coding[0].display.value, FHIRString("Oceania").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].display.as_json(), "Oceania")
        self.assertEqual(inst.jurisdiction[0].coding[0].system.value, FHIRUri("http://unstats.un.org/unsd/methods/m49/m49.htm").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].system.as_json(), "http://unstats.un.org/unsd/methods/m49/m49.htm")
        self.assertEqual(inst.name.value, FHIRString("ExampleMap").value)
        self.assertEqual(inst.name.as_json(), "ExampleMap")
        self.assertEqual(inst.publisher.value, FHIRString("HL7 FHIR Standard").value)
        self.assertEqual(inst.publisher.as_json(), "HL7 FHIR Standard")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Example Map").value)
        self.assertEqual(inst.title.as_json(), "Example Map")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/StructureMap/example").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/StructureMap/example")
        self.assertEqual(inst.version.value, FHIRString("0.1").value)
        self.assertEqual(inst.version.as_json(), "0.1")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRDateTime, FHIRMarkdown, FHIRId, FHIRUri