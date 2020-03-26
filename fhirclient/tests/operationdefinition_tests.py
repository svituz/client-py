#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import operationdefinition

class OperationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OperationDefinition", js["resourceType"])
        return operationdefinition.OperationDefinition(js)

    def testOperationDefinition1(self):
        inst = self.instantiate_from('operationdefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationDefinition instance')
        self.implOperationDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("OperationDefinition", js["resourceType"])
        inst2 = operationdefinition.OperationDefinition(js)
        self.implOperationDefinition1(inst2)

    def implOperationDefinition1(self, inst):
        self.assertEqual(inst.base.value, FHIRCanonical("OperationDefinition/Questionnaire-populate").value)
        self.assertEqual(inst.base.as_json(), "OperationDefinition/Questionnaire-populate")
        self.assertEqual(inst.code.value, FHIRCode("populate").value)
        self.assertEqual(inst.code.as_json(), "populate")
        self.assertEqual(inst.comment.value, FHIRMarkdown("Only implemented for Labs and Medications so far").value)
        self.assertEqual(inst.comment.as_json(), "Only implemented for Labs and Medications so far")
        self.assertEqual(inst.contact[0].name.value, FHIRString("System Administrator").value)
        self.assertEqual(inst.contact[0].name.as_json(), "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("email").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "email")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("beep@coyote.acme.com").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "beep@coyote.acme.com")
        self.assertEqual(inst.date.value, FHIRDateTime("2015-08-04").value)
        self.assertEqual(inst.date.as_json(), "2015-08-04")
        self.assertEqual(inst.description.value, FHIRMarkdown("Limited implementation of the Populate Questionnaire implementation").value)
        self.assertEqual(inst.description.as_json(), "Limited implementation of the Populate Questionnaire implementation")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertTrue(inst.instance)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.value, FHIRCode("GB").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.as_json(), "GB")
        self.assertEqual(inst.jurisdiction[0].coding[0].display.value, FHIRString("United Kingdom of Great Britain and Northern Ireland (the)").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].display.as_json(), "United Kingdom of Great Britain and Northern Ireland (the)")
        self.assertEqual(inst.jurisdiction[0].coding[0].system.value, FHIRUri("urn:iso:std:iso:3166").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].system.as_json(), "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind.value, FHIRCode("operation").value)
        self.assertEqual(inst.kind.as_json(), "operation")
        self.assertEqual(inst.name.value, FHIRString("Populate Questionnaire").value)
        self.assertEqual(inst.name.as_json(), "Populate Questionnaire")
        self.assertEqual(inst.overload[0].parameterName[0].value, FHIRString("subject").value)
        self.assertEqual(inst.overload[0].parameterName[0].as_json(), "subject")
        self.assertEqual(inst.overload[0].parameterName[1].value, FHIRString("local").value)
        self.assertEqual(inst.overload[0].parameterName[1].as_json(), "local")
        self.assertEqual(inst.overload[1].comment.value, FHIRString("local defaults to false when not passed as a parameter").value)
        self.assertEqual(inst.overload[1].comment.as_json(), "local defaults to false when not passed as a parameter")
        self.assertEqual(inst.overload[1].parameterName[0].value, FHIRString("subject").value)
        self.assertEqual(inst.overload[1].parameterName[0].as_json(), "subject")
        self.assertEqual(inst.parameter[0].max.value, FHIRString("1").value)
        self.assertEqual(inst.parameter[0].max.as_json(), "1")
        self.assertEqual(inst.parameter[0].min, 1)
        self.assertEqual(inst.parameter[0].name.value, FHIRCode("subject").value)
        self.assertEqual(inst.parameter[0].name.as_json(), "subject")
        self.assertEqual(inst.parameter[0].type.value, FHIRCode("Reference").value)
        self.assertEqual(inst.parameter[0].type.as_json(), "Reference")
        self.assertEqual(inst.parameter[0].use.value, FHIRCode("in").value)
        self.assertEqual(inst.parameter[0].use.as_json(), "in")
        self.assertEqual(inst.parameter[1].documentation.value, FHIRString("If the *local* parameter is set to true, server information about the specified subject will be used to populate the instance.").value)
        self.assertEqual(inst.parameter[1].documentation.as_json(), "If the *local* parameter is set to true, server information about the specified subject will be used to populate the instance.")
        self.assertEqual(inst.parameter[1].max.value, FHIRString("1").value)
        self.assertEqual(inst.parameter[1].max.as_json(), "1")
        self.assertEqual(inst.parameter[1].min, 0)
        self.assertEqual(inst.parameter[1].name.value, FHIRCode("local").value)
        self.assertEqual(inst.parameter[1].name.as_json(), "local")
        self.assertEqual(inst.parameter[1].type.value, FHIRCode("Reference").value)
        self.assertEqual(inst.parameter[1].type.as_json(), "Reference")
        self.assertEqual(inst.parameter[1].use.value, FHIRCode("in").value)
        self.assertEqual(inst.parameter[1].use.as_json(), "in")
        self.assertEqual(inst.parameter[2].documentation.value, FHIRString("The partially (or fully)-populated set of answers for the specified Questionnaire").value)
        self.assertEqual(inst.parameter[2].documentation.as_json(), "The partially (or fully)-populated set of answers for the specified Questionnaire")
        self.assertEqual(inst.parameter[2].max.value, FHIRString("1").value)
        self.assertEqual(inst.parameter[2].max.as_json(), "1")
        self.assertEqual(inst.parameter[2].min, 1)
        self.assertEqual(inst.parameter[2].name.value, FHIRCode("return").value)
        self.assertEqual(inst.parameter[2].name.as_json(), "return")
        self.assertEqual(inst.parameter[2].type.value, FHIRCode("QuestionnaireResponse").value)
        self.assertEqual(inst.parameter[2].type.as_json(), "QuestionnaireResponse")
        self.assertEqual(inst.parameter[2].use.value, FHIRCode("out").value)
        self.assertEqual(inst.parameter[2].use.as_json(), "out")
        self.assertEqual(inst.publisher.value, FHIRString("Acme Healthcare Services").value)
        self.assertEqual(inst.publisher.as_json(), "Acme Healthcare Services")
        self.assertEqual(inst.resource[0].value, FHIRCode("Questionnaire").value)
        self.assertEqual(inst.resource[0].as_json(), "Questionnaire")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertFalse(inst.system)
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertFalse(inst.type)
        self.assertEqual(inst.url.value, FHIRUri("http://h7.org/fhir/OperationDefinition/example").value)
        self.assertEqual(inst.url.as_json(), "http://h7.org/fhir/OperationDefinition/example")
        self.assertEqual(inst.useContext[0].code.code.value, FHIRCode("venue").value)
        self.assertEqual(inst.useContext[0].code.code.as_json(), "venue")
        self.assertEqual(inst.useContext[0].code.display.value, FHIRString("Clinical Venue").value)
        self.assertEqual(inst.useContext[0].code.display.as_json(), "Clinical Venue")
        self.assertEqual(inst.useContext[0].code.system.value, FHIRUri("http://build.fhir.org/codesystem-usage-context-type").value)
        self.assertEqual(inst.useContext[0].code.system.as_json(), "http://build.fhir.org/codesystem-usage-context-type")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code.value, FHIRCode("IMP").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code.as_json(), "IMP")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display.value, FHIRString("inpatient encounter").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display.as_json(), "inpatient encounter")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")
        self.assertEqual(inst.version.value, FHIRString("B").value)
        self.assertEqual(inst.version.as_json(), "B")


from fhirclient.models.fhirdatatypes import FHIRCanonical, FHIRCode, FHIRMarkdown, FHIRString, FHIRDateTime, FHIRUri