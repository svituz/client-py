#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import compartmentdefinition

class CompartmentDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CompartmentDefinition", js["resourceType"])
        return compartmentdefinition.CompartmentDefinition(js)

    def testCompartmentDefinition1(self):
        inst = self.instantiate_from('compartmentdefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CompartmentDefinition instance')
        self.implCompartmentDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("CompartmentDefinition", js["resourceType"])
        inst2 = compartmentdefinition.CompartmentDefinition(js)
        self.implCompartmentDefinition1(inst2)

    def implCompartmentDefinition1(self, inst):
        self.assertEqual(inst.code.value, FHIRCode("Device").value)
        self.assertEqual(inst.code.as_json(), "Device")
        self.assertEqual(inst.contact[0].name.value, FHIRString("[string]").value)
        self.assertEqual(inst.contact[0].name.as_json(), "[string]")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.date.value, FHIRDateTime("2017-02-24").value)
        self.assertEqual(inst.date.as_json(), "2017-02-24")
        self.assertEqual(inst.description.value, FHIRMarkdown("The set of resources associated with a particular Device (example with Communication and CommunicationRequest resourses only).").value)
        self.assertEqual(inst.description.as_json(), "The set of resources associated with a particular Device (example with Communication and CommunicationRequest resourses only).")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.name.value, FHIRString("EXAMPLE").value)
        self.assertEqual(inst.name.as_json(), "EXAMPLE")
        self.assertEqual(inst.publisher.value, FHIRString("Health Level Seven International (FHIR Infrastructure)").value)
        self.assertEqual(inst.publisher.as_json(), "Health Level Seven International (FHIR Infrastructure)")
        self.assertEqual(inst.purpose.value, FHIRMarkdown("Provides an example of a FHIR compartment definition based on the Device resource type.").value)
        self.assertEqual(inst.purpose.as_json(), "Provides an example of a FHIR compartment definition based on the Device resource type.")
        self.assertEqual(inst.resource[0].code.value, FHIRCode("Communication").value)
        self.assertEqual(inst.resource[0].code.as_json(), "Communication")
        self.assertEqual(inst.resource[0].documentation.value, FHIRString("The device used as the message sender and recipient").value)
        self.assertEqual(inst.resource[0].documentation.as_json(), "The device used as the message sender and recipient")
        self.assertEqual(inst.resource[0].param[0].value, FHIRString("sender").value)
        self.assertEqual(inst.resource[0].param[0].as_json(), "sender")
        self.assertEqual(inst.resource[0].param[1].value, FHIRString("recipient").value)
        self.assertEqual(inst.resource[0].param[1].as_json(), "recipient")
        self.assertEqual(inst.resource[1].code.value, FHIRCode("CommunicationRequest").value)
        self.assertEqual(inst.resource[1].code.as_json(), "CommunicationRequest")
        self.assertEqual(inst.resource[1].documentation.value, FHIRString("The device used as the message sender and recipient").value)
        self.assertEqual(inst.resource[1].documentation.as_json(), "The device used as the message sender and recipient")
        self.assertEqual(inst.resource[1].param[0].value, FHIRString("sender").value)
        self.assertEqual(inst.resource[1].param[0].as_json(), "sender")
        self.assertEqual(inst.resource[1].param[1].value, FHIRString("recipient").value)
        self.assertEqual(inst.resource[1].param[1].as_json(), "recipient")
        self.assertTrue(inst.search)
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/CompartmentDefinition/example").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/CompartmentDefinition/example")
        self.assertEqual(inst.useContext[0].code.code.value, FHIRCode("focus").value)
        self.assertEqual(inst.useContext[0].code.code.as_json(), "focus")
        self.assertEqual(inst.useContext[0].code.system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/usage-context-type").value)
        self.assertEqual(inst.useContext[0].code.system.as_json(), "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code.value, FHIRCode("Device").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code.as_json(), "Device")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system.value, FHIRUri("http://hl7.org/fhir/resource-types").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system.as_json(), "http://hl7.org/fhir/resource-types")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRDateTime, FHIRMarkdown, FHIRUri