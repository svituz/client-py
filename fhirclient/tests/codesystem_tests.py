#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import codesystem

class CodeSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CodeSystem", js["resourceType"])
        return codesystem.CodeSystem(js)

    def testCodeSystem1(self):
        inst = self.instantiate_from('codesystem-example-summary.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CodeSystem instance')
        self.implCodeSystem1(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem1(inst2)

    def implCodeSystem1(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(inst.contact[0].name.value, FHIRString("FHIR project team").value)
        self.assertEqual(inst.contact[0].name.as_json(), "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.content.value, FHIRCode("not-present").value)
        self.assertEqual(inst.content.as_json(), "not-present")
        self.assertEqual(inst.count.value, FHIRUnsignedInt('92').value)
        self.assertEqual(inst.count.as_json(), 92)
        self.assertEqual(inst.description.value, FHIRMarkdown("This is an example code system summary for the ACME codes for body site.").value)
        self.assertEqual(inst.description.as_json(), "This is an example code system summary for the ACME codes for body site.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id.value, FHIRString("summary").value)
        self.assertEqual(inst.id.as_json(), "summary")
        self.assertEqual(inst.jurisdiction[0].coding[0].code.value, FHIRCode("CA").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.as_json(), "CA")
        self.assertEqual(inst.jurisdiction[0].coding[0].system.value, FHIRUri("urn:iso:std:iso:3166").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].system.as_json(), "urn:iso:std:iso:3166")
        self.assertEqual(inst.name.value, FHIRString("Code system summary example for ACME body sites").value)
        self.assertEqual(inst.name.as_json(), "Code system summary example for ACME body sites")
        self.assertEqual(inst.publisher.value, FHIRString("HL7 International").value)
        self.assertEqual(inst.publisher.as_json(), "HL7 International")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/CodeSystem/summary").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/CodeSystem/summary")
        self.assertEqual(inst.useContext[0].code.code.value, FHIRCode("species").value)
        self.assertEqual(inst.useContext[0].code.code.as_json(), "species")
        self.assertEqual(inst.useContext[0].code.system.value, FHIRUri("http://example.org/CodeSystem/contexttype").value)
        self.assertEqual(inst.useContext[0].code.system.as_json(), "http://example.org/CodeSystem/contexttype")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code.value, FHIRCode("337915000").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].code.as_json(), "337915000")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display.value, FHIRString("Homo sapiens (organism)").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].display.as_json(), "Homo sapiens (organism)")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.version.value, FHIRString("4.0.1").value)
        self.assertEqual(inst.version.as_json(), "4.0.1")

    def testCodeSystem2(self):
        inst = self.instantiate_from('codesystem-example-supplement.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CodeSystem instance')
        self.implCodeSystem2(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem2(inst2)

    def implCodeSystem2(self, inst):
        self.assertEqual(inst.concept[0].code.value, FHIRCode("chol-mmol").value)
        self.assertEqual(inst.concept[0].code.as_json(), "chol-mmol")
        self.assertEqual(inst.concept[0].property[0].code.value, FHIRCode("legacy").value)
        self.assertEqual(inst.concept[0].property[0].code.as_json(), "legacy")
        self.assertFalse(inst.concept[0].property[0].valueBoolean)
        self.assertEqual(inst.concept[1].code.value, FHIRCode("chol-mass").value)
        self.assertEqual(inst.concept[1].code.as_json(), "chol-mass")
        self.assertEqual(inst.concept[1].property[0].code.value, FHIRCode("legacy").value)
        self.assertEqual(inst.concept[1].property[0].code.as_json(), "legacy")
        self.assertTrue(inst.concept[1].property[0].valueBoolean)
        self.assertEqual(inst.concept[2].code.value, FHIRCode("chol").value)
        self.assertEqual(inst.concept[2].code.as_json(), "chol")
        self.assertEqual(inst.concept[2].property[0].code.value, FHIRCode("legacy").value)
        self.assertEqual(inst.concept[2].property[0].code.as_json(), "legacy")
        self.assertTrue(inst.concept[2].property[0].valueBoolean)
        self.assertEqual(inst.contact[0].name.value, FHIRString("FHIR project team").value)
        self.assertEqual(inst.contact[0].name.as_json(), "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.content.value, FHIRCode("supplement").value)
        self.assertEqual(inst.content.as_json(), "supplement")
        self.assertEqual(inst.date.value, FHIRDateTime("2016-01-28").value)
        self.assertEqual(inst.date.as_json(), "2016-01-28")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id.value, FHIRString("example-supplement").value)
        self.assertEqual(inst.id.as_json(), "example-supplement")
        self.assertEqual(inst.name.value, FHIRString("CholCodeLegacyStatus").value)
        self.assertEqual(inst.name.as_json(), "CholCodeLegacyStatus")
        self.assertEqual(inst.property[0].code.value, FHIRCode("legacy").value)
        self.assertEqual(inst.property[0].code.as_json(), "legacy")
        self.assertEqual(inst.property[0].description.value, FHIRString("hether the test is currently performed").value)
        self.assertEqual(inst.property[0].description.as_json(), "hether the test is currently performed")
        self.assertEqual(inst.property[0].type.value, FHIRCode("boolean").value)
        self.assertEqual(inst.property[0].type.as_json(), "boolean")
        self.assertEqual(inst.publisher.value, FHIRString("ACME Co").value)
        self.assertEqual(inst.publisher.as_json(), "ACME Co")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.supplements.value, FHIRCanonical("http://hl7.org/fhir/CodeSystem/example").value)
        self.assertEqual(inst.supplements.as_json(), "http://hl7.org/fhir/CodeSystem/example")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/CodeSystem/example-supplement").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/CodeSystem/example-supplement")
        self.assertEqual(inst.version.value, FHIRString("201801103").value)
        self.assertEqual(inst.version.as_json(), "201801103")

    def testCodeSystem3(self):
        inst = self.instantiate_from('codesystem-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CodeSystem instance')
        self.implCodeSystem3(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem3(inst2)

    def implCodeSystem3(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(inst.concept[0].code.value, FHIRCode("chol-mmol").value)
        self.assertEqual(inst.concept[0].code.as_json(), "chol-mmol")
        self.assertEqual(inst.concept[0].definition.value, FHIRString("Serum Cholesterol, in mmol/L").value)
        self.assertEqual(inst.concept[0].definition.as_json(), "Serum Cholesterol, in mmol/L")
        self.assertEqual(inst.concept[0].designation[0].use.code.value, FHIRCode("internal-label").value)
        self.assertEqual(inst.concept[0].designation[0].use.code.as_json(), "internal-label")
        self.assertEqual(inst.concept[0].designation[0].use.system.value, FHIRUri("http://acme.com/config/fhir/codesystems/internal").value)
        self.assertEqual(inst.concept[0].designation[0].use.system.as_json(), "http://acme.com/config/fhir/codesystems/internal")
        self.assertEqual(inst.concept[0].designation[0].value.value, FHIRString("From ACME POC Testing").value)
        self.assertEqual(inst.concept[0].designation[0].value.as_json(), "From ACME POC Testing")
        self.assertEqual(inst.concept[0].display.value, FHIRString("SChol (mmol/L)").value)
        self.assertEqual(inst.concept[0].display.as_json(), "SChol (mmol/L)")
        self.assertEqual(inst.concept[1].code.value, FHIRCode("chol-mass").value)
        self.assertEqual(inst.concept[1].code.as_json(), "chol-mass")
        self.assertEqual(inst.concept[1].definition.value, FHIRString("Serum Cholesterol, in mg/L").value)
        self.assertEqual(inst.concept[1].definition.as_json(), "Serum Cholesterol, in mg/L")
        self.assertEqual(inst.concept[1].designation[0].use.code.value, FHIRCode("internal-label").value)
        self.assertEqual(inst.concept[1].designation[0].use.code.as_json(), "internal-label")
        self.assertEqual(inst.concept[1].designation[0].use.system.value, FHIRUri("http://acme.com/config/fhir/codesystems/internal").value)
        self.assertEqual(inst.concept[1].designation[0].use.system.as_json(), "http://acme.com/config/fhir/codesystems/internal")
        self.assertEqual(inst.concept[1].designation[0].value.value, FHIRString("From Paragon Labs").value)
        self.assertEqual(inst.concept[1].designation[0].value.as_json(), "From Paragon Labs")
        self.assertEqual(inst.concept[1].display.value, FHIRString("SChol (mg/L)").value)
        self.assertEqual(inst.concept[1].display.as_json(), "SChol (mg/L)")
        self.assertEqual(inst.concept[2].code.value, FHIRCode("chol").value)
        self.assertEqual(inst.concept[2].code.as_json(), "chol")
        self.assertEqual(inst.concept[2].definition.value, FHIRString("Serum Cholesterol").value)
        self.assertEqual(inst.concept[2].definition.as_json(), "Serum Cholesterol")
        self.assertEqual(inst.concept[2].designation[0].use.code.value, FHIRCode("internal-label").value)
        self.assertEqual(inst.concept[2].designation[0].use.code.as_json(), "internal-label")
        self.assertEqual(inst.concept[2].designation[0].use.system.value, FHIRUri("http://acme.com/config/fhir/codesystems/internal").value)
        self.assertEqual(inst.concept[2].designation[0].use.system.as_json(), "http://acme.com/config/fhir/codesystems/internal")
        self.assertEqual(inst.concept[2].designation[0].value.value, FHIRString("Obdurate Labs uses this with both kinds of units...").value)
        self.assertEqual(inst.concept[2].designation[0].value.as_json(), "Obdurate Labs uses this with both kinds of units...")
        self.assertEqual(inst.concept[2].display.value, FHIRString("SChol").value)
        self.assertEqual(inst.concept[2].display.as_json(), "SChol")
        self.assertEqual(inst.contact[0].name.value, FHIRString("FHIR project team").value)
        self.assertEqual(inst.contact[0].name.as_json(), "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.content.value, FHIRCode("complete").value)
        self.assertEqual(inst.content.as_json(), "complete")
        self.assertEqual(inst.date.value, FHIRDateTime("2016-01-28").value)
        self.assertEqual(inst.date.as_json(), "2016-01-28")
        self.assertEqual(inst.description.value, FHIRMarkdown("This is an example code system that includes all the ACME codes for serum/plasma cholesterol from v2.36.").value)
        self.assertEqual(inst.description.as_json(), "This is an example code system that includes all the ACME codes for serum/plasma cholesterol from v2.36.")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.filter[0].code.value, FHIRCode("acme-plasma").value)
        self.assertEqual(inst.filter[0].code.as_json(), "acme-plasma")
        self.assertEqual(inst.filter[0].description.value, FHIRString("An internal filter used to select codes that are only used with plasma").value)
        self.assertEqual(inst.filter[0].description.as_json(), "An internal filter used to select codes that are only used with plasma")
        self.assertEqual(inst.filter[0].operator[0].value, FHIRCode("=").value)
        self.assertEqual(inst.filter[0].operator[0].as_json(), "=")
        self.assertEqual(inst.filter[0].value.value, FHIRString("the value of this filter is either 'true' or 'false'").value)
        self.assertEqual(inst.filter[0].value.as_json(), "the value of this filter is either 'true' or 'false'")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://acme.com/identifiers/codesystems").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://acme.com/identifiers/codesystems")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("internal-cholesterol-inl").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "internal-cholesterol-inl")
        self.assertEqual(inst.meta.profile[0].value, FHIRCanonical("http://hl7.org/fhir/StructureDefinition/shareablecodesystem").value)
        self.assertEqual(inst.meta.profile[0].as_json(), "http://hl7.org/fhir/StructureDefinition/shareablecodesystem")
        self.assertEqual(inst.name.value, FHIRString("ACMECholCodesBlood").value)
        self.assertEqual(inst.name.as_json(), "ACMECholCodesBlood")
        self.assertEqual(inst.publisher.value, FHIRString("Acme Co").value)
        self.assertEqual(inst.publisher.as_json(), "Acme Co")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("ACME Codes for Cholesterol in Serum/Plasma").value)
        self.assertEqual(inst.title.as_json(), "ACME Codes for Cholesterol in Serum/Plasma")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/CodeSystem/example").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/CodeSystem/example")
        self.assertEqual(inst.version.value, FHIRString("20160128").value)
        self.assertEqual(inst.version.as_json(), "20160128")

    def testCodeSystem4(self):
        inst = self.instantiate_from('codesystem-list-example-codes.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CodeSystem instance')
        self.implCodeSystem4(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem4(inst2)

    def implCodeSystem4(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(inst.concept[0].code.value, FHIRCode("alerts").value)
        self.assertEqual(inst.concept[0].code.as_json(), "alerts")
        self.assertEqual(inst.concept[0].definition.value, FHIRString("A list of alerts for the patient.").value)
        self.assertEqual(inst.concept[0].definition.as_json(), "A list of alerts for the patient.")
        self.assertEqual(inst.concept[0].display.value, FHIRString("Alerts").value)
        self.assertEqual(inst.concept[0].display.as_json(), "Alerts")
        self.assertEqual(inst.concept[1].code.value, FHIRCode("adverserxns").value)
        self.assertEqual(inst.concept[1].code.as_json(), "adverserxns")
        self.assertEqual(inst.concept[1].definition.value, FHIRString("A list of part adverse reactions.").value)
        self.assertEqual(inst.concept[1].definition.as_json(), "A list of part adverse reactions.")
        self.assertEqual(inst.concept[1].display.value, FHIRString("Adverse Reactions").value)
        self.assertEqual(inst.concept[1].display.as_json(), "Adverse Reactions")
        self.assertEqual(inst.concept[2].code.value, FHIRCode("allergies").value)
        self.assertEqual(inst.concept[2].code.as_json(), "allergies")
        self.assertEqual(inst.concept[2].definition.value, FHIRString("A list of Allergies for the patient.").value)
        self.assertEqual(inst.concept[2].definition.as_json(), "A list of Allergies for the patient.")
        self.assertEqual(inst.concept[2].display.value, FHIRString("Allergies").value)
        self.assertEqual(inst.concept[2].display.as_json(), "Allergies")
        self.assertEqual(inst.concept[3].code.value, FHIRCode("medications").value)
        self.assertEqual(inst.concept[3].code.as_json(), "medications")
        self.assertEqual(inst.concept[3].definition.value, FHIRString("A list of medication statements for the patient.").value)
        self.assertEqual(inst.concept[3].definition.as_json(), "A list of medication statements for the patient.")
        self.assertEqual(inst.concept[3].display.value, FHIRString("Medication List").value)
        self.assertEqual(inst.concept[3].display.as_json(), "Medication List")
        self.assertEqual(inst.concept[4].code.value, FHIRCode("problems").value)
        self.assertEqual(inst.concept[4].code.as_json(), "problems")
        self.assertEqual(inst.concept[4].definition.value, FHIRString("A list of problems that the patient is known of have (or have had in the past).").value)
        self.assertEqual(inst.concept[4].definition.as_json(), "A list of problems that the patient is known of have (or have had in the past).")
        self.assertEqual(inst.concept[4].display.value, FHIRString("Problem List").value)
        self.assertEqual(inst.concept[4].display.as_json(), "Problem List")
        self.assertEqual(inst.concept[5].code.value, FHIRCode("worklist").value)
        self.assertEqual(inst.concept[5].code.as_json(), "worklist")
        self.assertEqual(inst.concept[5].definition.value, FHIRString("A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).").value)
        self.assertEqual(inst.concept[5].definition.as_json(), "A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).")
        self.assertEqual(inst.concept[5].display.value, FHIRString("Worklist").value)
        self.assertEqual(inst.concept[5].display.as_json(), "Worklist")
        self.assertEqual(inst.concept[6].code.value, FHIRCode("waiting").value)
        self.assertEqual(inst.concept[6].code.as_json(), "waiting")
        self.assertEqual(inst.concept[6].definition.value, FHIRString("A list of items waiting for an event (perhaps a surgical patient waiting list).").value)
        self.assertEqual(inst.concept[6].definition.as_json(), "A list of items waiting for an event (perhaps a surgical patient waiting list).")
        self.assertEqual(inst.concept[6].display.value, FHIRString("Waiting List").value)
        self.assertEqual(inst.concept[6].display.as_json(), "Waiting List")
        self.assertEqual(inst.concept[7].code.value, FHIRCode("protocols").value)
        self.assertEqual(inst.concept[7].code.as_json(), "protocols")
        self.assertEqual(inst.concept[7].definition.value, FHIRString("A set of protocols to be followed.").value)
        self.assertEqual(inst.concept[7].definition.as_json(), "A set of protocols to be followed.")
        self.assertEqual(inst.concept[7].display.value, FHIRString("Protocols").value)
        self.assertEqual(inst.concept[7].display.as_json(), "Protocols")
        self.assertEqual(inst.concept[8].code.value, FHIRCode("plans").value)
        self.assertEqual(inst.concept[8].code.as_json(), "plans")
        self.assertEqual(inst.concept[8].definition.value, FHIRString("A set of care plans that apply in a particular context of care.").value)
        self.assertEqual(inst.concept[8].definition.as_json(), "A set of care plans that apply in a particular context of care.")
        self.assertEqual(inst.concept[8].display.value, FHIRString("Care Plans").value)
        self.assertEqual(inst.concept[8].display.as_json(), "Care Plans")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.content.value, FHIRCode("complete").value)
        self.assertEqual(inst.content.as_json(), "complete")
        self.assertEqual(inst.description.value, FHIRMarkdown("Example use codes for the List resource - typical kinds of use.").value)
        self.assertEqual(inst.description.as_json(), "Example use codes for the List resource - typical kinds of use.")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.extension[0].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/structuredefinition-wg").value)
        self.assertEqual(inst.extension[0].url.as_json(), "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg")
        self.assertEqual(inst.extension[0].valueCode.value, FHIRCode("fhir").value)
        self.assertEqual(inst.extension[0].valueCode.as_json(), "fhir")
        self.assertEqual(inst.extension[1].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status").value)
        self.assertEqual(inst.extension[1].url.as_json(), "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status")
        self.assertEqual(inst.extension[1].valueCode.value, FHIRCode("draft").value)
        self.assertEqual(inst.extension[1].valueCode.as_json(), "draft")
        self.assertEqual(inst.extension[2].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm").value)
        self.assertEqual(inst.extension[2].url.as_json(), "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm")
        self.assertEqual(inst.extension[2].valueInteger, 1)
        self.assertEqual(inst.id.value, FHIRString("list-example-codes").value)
        self.assertEqual(inst.id.as_json(), "list-example-codes")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:ietf:rfc:3986").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("urn:oid:2.16.840.1.113883.4.642.4.1105").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "urn:oid:2.16.840.1.113883.4.642.4.1105")
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant("2019-11-01T09:29:23.356+11:00").value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2019-11-01T09:29:23.356+11:00').date)
        self.assertEqual(inst.meta.profile[0].value, FHIRCanonical("http://hl7.org/fhir/StructureDefinition/shareablecodesystem").value)
        self.assertEqual(inst.meta.profile[0].as_json(), "http://hl7.org/fhir/StructureDefinition/shareablecodesystem")
        self.assertEqual(inst.name.value, FHIRString("ExampleUseCodesForList").value)
        self.assertEqual(inst.name.as_json(), "ExampleUseCodesForList")
        self.assertEqual(inst.publisher.value, FHIRString("FHIR Project").value)
        self.assertEqual(inst.publisher.as_json(), "FHIR Project")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Example Use Codes for List").value)
        self.assertEqual(inst.title.as_json(), "Example Use Codes for List")
        self.assertEqual(inst.url.value, FHIRUri("http://terminology.hl7.org/CodeSystem/list-example-use-codes").value)
        self.assertEqual(inst.url.as_json(), "http://terminology.hl7.org/CodeSystem/list-example-use-codes")
        self.assertEqual(inst.valueSet.value, FHIRCanonical("http://hl7.org/fhir/ValueSet/list-example-codes").value)
        self.assertEqual(inst.valueSet.as_json(), "http://hl7.org/fhir/ValueSet/list-example-codes")
        self.assertEqual(inst.version.value, FHIRString("4.0.1").value)
        self.assertEqual(inst.version.as_json(), "4.0.1")

    def testCodeSystem5(self):
        inst = self.instantiate_from('codesystem-examplescenario-actor-type.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CodeSystem instance')
        self.implCodeSystem5(inst)

        js = inst.as_json()
        self.assertEqual("CodeSystem", js["resourceType"])
        inst2 = codesystem.CodeSystem(js)
        self.implCodeSystem5(inst2)

    def implCodeSystem5(self, inst):
        self.assertTrue(inst.caseSensitive)
        self.assertEqual(inst.concept[0].code.value, FHIRCode("person").value)
        self.assertEqual(inst.concept[0].code.as_json(), "person")
        self.assertEqual(inst.concept[0].definition.value, FHIRString("A person.").value)
        self.assertEqual(inst.concept[0].definition.as_json(), "A person.")
        self.assertEqual(inst.concept[0].display.value, FHIRString("Person").value)
        self.assertEqual(inst.concept[0].display.as_json(), "Person")
        self.assertEqual(inst.concept[1].code.value, FHIRCode("entity").value)
        self.assertEqual(inst.concept[1].code.as_json(), "entity")
        self.assertEqual(inst.concept[1].definition.value, FHIRString("A system.").value)
        self.assertEqual(inst.concept[1].definition.as_json(), "A system.")
        self.assertEqual(inst.concept[1].display.value, FHIRString("System").value)
        self.assertEqual(inst.concept[1].display.as_json(), "System")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.contact[0].telecom[1].system.value, FHIRCode("email").value)
        self.assertEqual(inst.contact[0].telecom[1].system.as_json(), "email")
        self.assertEqual(inst.contact[0].telecom[1].value.value, FHIRString("fhir@lists.hl7.org").value)
        self.assertEqual(inst.contact[0].telecom[1].value.as_json(), "fhir@lists.hl7.org")
        self.assertEqual(inst.content.value, FHIRCode("complete").value)
        self.assertEqual(inst.content.as_json(), "complete")
        self.assertEqual(inst.date.value, FHIRDateTime("2019-11-01T09:29:23+11:00").value)
        self.assertEqual(inst.date.as_json(), "2019-11-01T09:29:23+11:00")
        self.assertEqual(inst.description.value, FHIRMarkdown("The type of actor - system or human.").value)
        self.assertEqual(inst.description.as_json(), "The type of actor - system or human.")
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.extension[0].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/structuredefinition-wg").value)
        self.assertEqual(inst.extension[0].url.as_json(), "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg")
        self.assertEqual(inst.extension[0].valueCode.value, FHIRCode("fhir").value)
        self.assertEqual(inst.extension[0].valueCode.as_json(), "fhir")
        self.assertEqual(inst.extension[1].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status").value)
        self.assertEqual(inst.extension[1].url.as_json(), "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status")
        self.assertEqual(inst.extension[1].valueCode.value, FHIRCode("trial-use").value)
        self.assertEqual(inst.extension[1].valueCode.as_json(), "trial-use")
        self.assertEqual(inst.extension[2].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm").value)
        self.assertEqual(inst.extension[2].url.as_json(), "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm")
        self.assertEqual(inst.extension[2].valueInteger, 0)
        self.assertEqual(inst.id.value, FHIRString("examplescenario-actor-type").value)
        self.assertEqual(inst.id.as_json(), "examplescenario-actor-type")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:ietf:rfc:3986").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("urn:oid:2.16.840.1.113883.4.642.4.859").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "urn:oid:2.16.840.1.113883.4.642.4.859")
        self.assertEqual(inst.meta.lastUpdated.value, FHIRInstant("2019-11-01T09:29:23.356+11:00").value)
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2019-11-01T09:29:23.356+11:00")
        self.assertEqual(inst.meta.lastUpdated.date, FHIRInstant('2019-11-01T09:29:23.356+11:00').date)
        self.assertEqual(inst.name.value, FHIRString("ExampleScenarioActorType").value)
        self.assertEqual(inst.name.as_json(), "ExampleScenarioActorType")
        self.assertEqual(inst.publisher.value, FHIRString("HL7 (FHIR Project)").value)
        self.assertEqual(inst.publisher.as_json(), "HL7 (FHIR Project)")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("ExampleScenarioActorType").value)
        self.assertEqual(inst.title.as_json(), "ExampleScenarioActorType")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/examplescenario-actor-type").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/examplescenario-actor-type")
        self.assertEqual(inst.valueSet.value, FHIRCanonical("http://hl7.org/fhir/ValueSet/examplescenario-actor-type").value)
        self.assertEqual(inst.valueSet.as_json(), "http://hl7.org/fhir/ValueSet/examplescenario-actor-type")
        self.assertEqual(inst.version.value, FHIRString("4.0.1").value)
        self.assertEqual(inst.version.as_json(), "4.0.1")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUnsignedInt, FHIRMarkdown, FHIRUri, FHIRDateTime, FHIRCanonical, FHIRInstant