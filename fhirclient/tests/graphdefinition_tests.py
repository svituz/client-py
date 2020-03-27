#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import graphdefinition

class GraphDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("GraphDefinition", js["resourceType"])
        return graphdefinition.GraphDefinition(js)

    def testGraphDefinition1(self):
        inst = self.instantiate_from('graphdefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a GraphDefinition instance')
        self.implGraphDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("GraphDefinition", js["resourceType"])
        inst2 = graphdefinition.GraphDefinition(js)
        self.implGraphDefinition1(inst2)

    def implGraphDefinition1(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.date.value, FHIRDateTime("2015-08-04").value)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(inst.description.value, FHIRMarkdown("Specify to include list references when generating a document using the $document operation").value)
        self.assertEqual(inst.description.as_json(), "Specify to include list references when generating a document using the $document operation")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.link[0].description.value, FHIRString("Link to List").value)
        self.assertEqual(inst.link[0].description.as_json(), "Link to List")
        self.assertEqual(inst.link[0].path.value, FHIRString("Composition.section.entry").value)
        self.assertEqual(inst.link[0].path.as_json(), "Composition.section.entry")
        self.assertEqual(inst.link[0].target[0].compartment[0].code.value, FHIRCode("Patient").value)
        self.assertEqual(inst.link[0].target[0].compartment[0].code.as_json(), "Patient")
        self.assertEqual(inst.link[0].target[0].compartment[0].rule.value, FHIRCode("identical").value)
        self.assertEqual(inst.link[0].target[0].compartment[0].rule.as_json(), "identical")
        self.assertEqual(inst.link[0].target[0].compartment[0].use.value, FHIRCode("requirement").value)
        self.assertEqual(inst.link[0].target[0].compartment[0].use.as_json(), "requirement")
        self.assertEqual(inst.link[0].target[0].link[0].description.value, FHIRString("Include any list entries").value)
        self.assertEqual(inst.link[0].target[0].link[0].description.as_json(), "Include any list entries")
        self.assertEqual(inst.link[0].target[0].link[0].path.value, FHIRString("List.entry.item").value)
        self.assertEqual(inst.link[0].target[0].link[0].path.as_json(), "List.entry.item")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].code.value, FHIRCode("Patient").value)
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].code.as_json(), "Patient")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].rule.value, FHIRCode("identical").value)
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].rule.as_json(), "identical")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].use.value, FHIRCode("requirement").value)
        self.assertEqual(inst.link[0].target[0].link[0].target[0].compartment[0].use.as_json(), "requirement")
        self.assertEqual(inst.link[0].target[0].link[0].target[0].type.value, FHIRCode("Resource").value)
        self.assertEqual(inst.link[0].target[0].link[0].target[0].type.as_json(), "Resource")
        self.assertEqual(inst.link[0].target[0].type.value, FHIRCode("List").value)
        self.assertEqual(inst.link[0].target[0].type.as_json(), "List")
        self.assertEqual(inst.name.value, FHIRString("Document Generation Template").value)
        self.assertEqual(inst.name.as_json(), "Document Generation Template")
        self.assertEqual(inst.publisher.value, FHIRString("FHIR Project").value)
        self.assertEqual(inst.publisher.as_json(), "FHIR Project")
        self.assertEqual(inst.start.value, FHIRCode("Composition").value)
        self.assertEqual(inst.start.as_json(), "Composition")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.url.value, FHIRUri("http://h7.org/fhir/GraphDefinition/example").value)
        self.assertEqual(inst.url.as_json(), "http://h7.org/fhir/GraphDefinition/example")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRDateTime, FHIRMarkdown, FHIRUri