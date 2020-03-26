#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import namingsystem

class NamingSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("NamingSystem", js["resourceType"])
        return namingsystem.NamingSystem(js)

    def testNamingSystem1(self):
        inst = self.instantiate_from('namingsystem-example-id.json')
        self.assertIsNotNone(inst, 'Must have instantiated a NamingSystem instance')
        self.implNamingSystem1(inst)

        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem1(inst2)

    def implNamingSystem1(self, inst):
        self.assertEqual(inst.contact[0].name.value, FHIRString("HL7 Australia FHIR Team").value)
        self.assertEqual(inst.contact[0].name.as_json(), "HL7 Australia FHIR Team")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7-australia.wikispaces.com/FHIR+Australia").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7-australia.wikispaces.com/FHIR+Australia")
        self.assertEqual(inst.date.value, FHIRDateTime("2015-08-31").value)
        self.assertEqual(inst.date.as_json(), "2015-08-31")
        self.assertEqual(inst.description.value, FHIRMarkdown("Australian HI Identifier as established by relevant regulations etc.").value)
        self.assertEqual(inst.description.as_json(), "Australian HI Identifier as established by relevant regulations etc.")
        self.assertEqual(inst.id.value, FHIRString("example-id").value)
        self.assertEqual(inst.id.as_json(), "example-id")
        self.assertEqual(inst.jurisdiction[0].coding[0].code.value, FHIRCode("AU").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.as_json(), "AU")
        self.assertEqual(inst.jurisdiction[0].coding[0].system.value, FHIRUri("urn:iso:std:iso:3166").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].system.as_json(), "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind.value, FHIRCode("identifier").value)
        self.assertEqual(inst.kind.as_json(), "identifier")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("Austalian Healthcare Identifier - Individual").value)
        self.assertEqual(inst.name.as_json(), "Austalian Healthcare Identifier - Individual")
        self.assertEqual(inst.publisher.value, FHIRString("HL7 Australia on behalf of NEHTA").value)
        self.assertEqual(inst.publisher.as_json(), "HL7 Australia on behalf of NEHTA")
        self.assertEqual(inst.responsible.value, FHIRString("HI Service Operator / NEHTA").value)
        self.assertEqual(inst.responsible.as_json(), "HI Service Operator / NEHTA")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("NI").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "NI")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("National unique individual identifier").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "National unique individual identifier")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v2-0203").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.type.text.value, FHIRString("IHI").value)
        self.assertEqual(inst.type.text.as_json(), "IHI")
        self.assertEqual(inst.uniqueId[0].comment.value, FHIRString("This value is used in Australian CDA documents").value)
        self.assertEqual(inst.uniqueId[0].comment.as_json(), "This value is used in Australian CDA documents")
        self.assertEqual(inst.uniqueId[0].type.value, FHIRCode("oid").value)
        self.assertEqual(inst.uniqueId[0].type.as_json(), "oid")
        self.assertEqual(inst.uniqueId[0].value.value, FHIRString("1.2.36.1.2001.1003.0").value)
        self.assertEqual(inst.uniqueId[0].value.as_json(), "1.2.36.1.2001.1003.0")
        self.assertEqual(inst.uniqueId[1].period.start.value, FHIRDateTime("2015-08-21").value)
        self.assertEqual(inst.uniqueId[1].period.start.as_json(), "2015-08-21")
        self.assertTrue(inst.uniqueId[1].preferred)
        self.assertEqual(inst.uniqueId[1].type.value, FHIRCode("uri").value)
        self.assertEqual(inst.uniqueId[1].type.as_json(), "uri")
        self.assertEqual(inst.uniqueId[1].value.value, FHIRString("http://ns.electronichealth.net.au/id/hi/ihi/1.0").value)
        self.assertEqual(inst.uniqueId[1].value.as_json(), "http://ns.electronichealth.net.au/id/hi/ihi/1.0")
        self.assertEqual(inst.usage.value, FHIRString("Used in Australia for identifying patients").value)
        self.assertEqual(inst.usage.as_json(), "Used in Australia for identifying patients")

    def testNamingSystem2(self):
        inst = self.instantiate_from('namingsystem-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a NamingSystem instance')
        self.implNamingSystem2(inst)

        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem2(inst2)

    def implNamingSystem2(self, inst):
        self.assertEqual(inst.contact[0].name.value, FHIRString("FHIR project team").value)
        self.assertEqual(inst.contact[0].name.as_json(), "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://hl7.org/fhir").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://hl7.org/fhir")
        self.assertEqual(inst.date.value, FHIRDateTime("2014-12-13").value)
        self.assertEqual(inst.date.as_json(), "2014-12-13")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.kind.value, FHIRCode("codesystem").value)
        self.assertEqual(inst.kind.as_json(), "codesystem")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("SNOMED CT").value)
        self.assertEqual(inst.name.as_json(), "SNOMED CT")
        self.assertEqual(inst.publisher.value, FHIRString("HL7 International on behalf of IHTSDO").value)
        self.assertEqual(inst.publisher.as_json(), "HL7 International on behalf of IHTSDO")
        self.assertEqual(inst.responsible.value, FHIRString("IHTSDO & affiliates").value)
        self.assertEqual(inst.responsible.as_json(), "IHTSDO & affiliates")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.uniqueId[0].type.value, FHIRCode("oid").value)
        self.assertEqual(inst.uniqueId[0].type.as_json(), "oid")
        self.assertEqual(inst.uniqueId[0].value.value, FHIRString("2.16.840.1.113883.6.96").value)
        self.assertEqual(inst.uniqueId[0].value.as_json(), "2.16.840.1.113883.6.96")
        self.assertTrue(inst.uniqueId[1].preferred)
        self.assertEqual(inst.uniqueId[1].type.value, FHIRCode("uri").value)
        self.assertEqual(inst.uniqueId[1].type.as_json(), "uri")
        self.assertEqual(inst.uniqueId[1].value.value, FHIRString("http://snomed.info/sct").value)
        self.assertEqual(inst.uniqueId[1].value.as_json(), "http://snomed.info/sct")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRDateTime, FHIRMarkdown, FHIRUri