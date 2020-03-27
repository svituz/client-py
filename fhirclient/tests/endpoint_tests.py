#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import endpoint

class EndpointTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Endpoint", js["resourceType"])
        return endpoint.Endpoint(js)

    def testEndpoint1(self):
        inst = self.instantiate_from('endpoint-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Endpoint instance')
        self.implEndpoint1(inst)

        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint1(inst2)

    def implEndpoint1(self, inst):
        self.assertEqual(inst.address.value, FHIRUrl("http://fhir3.healthintersections.com.au/open/CarePlan").value)
        self.assertEqual(inst.address.as_json(), "http://fhir3.healthintersections.com.au/open/CarePlan")
        self.assertEqual(inst.connectionType.code.value, FHIRCode("hl7-fhir-rest").value)
        self.assertEqual(inst.connectionType.code.as_json(), "hl7-fhir-rest")
        self.assertEqual(inst.connectionType.system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/endpoint-connection-type").value)
        self.assertEqual(inst.connectionType.system.as_json(), "http://terminology.hl7.org/CodeSystem/endpoint-connection-type")
        self.assertEqual(inst.contact[0].system.value, FHIRCode("email").value)
        self.assertEqual(inst.contact[0].system.as_json(), "email")
        self.assertEqual(inst.contact[0].use.value, FHIRCode("work").value)
        self.assertEqual(inst.contact[0].use.as_json(), "work")
        self.assertEqual(inst.contact[0].value.value, FHIRString("endpointmanager@example.org").value)
        self.assertEqual(inst.contact[0].value.as_json(), "endpointmanager@example.org")
        self.assertEqual(inst.header[0].value, FHIRString("bearer-code BASGS534s4").value)
        self.assertEqual(inst.header[0].as_json(), "bearer-code BASGS534s4")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/enpoint-identifier").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/enpoint-identifier")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("epcp12").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "epcp12")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("Health Intersections CarePlan Hub").value)
        self.assertEqual(inst.name.as_json(), "Health Intersections CarePlan Hub")
        self.assertEqual(inst.payloadMimeType[0].value, FHIRCode("application/fhir+xml").value)
        self.assertEqual(inst.payloadMimeType[0].as_json(), "application/fhir+xml")
        self.assertEqual(inst.payloadType[0].coding[0].code.value, FHIRCode("CarePlan").value)
        self.assertEqual(inst.payloadType[0].coding[0].code.as_json(), "CarePlan")
        self.assertEqual(inst.payloadType[0].coding[0].system.value, FHIRUri("http://hl7.org/fhir/resource-types").value)
        self.assertEqual(inst.payloadType[0].coding[0].system.as_json(), "http://hl7.org/fhir/resource-types")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2014-09-01").value)
        self.assertEqual(inst.period.start.as_json(), "2014-09-01")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testEndpoint2(self):
        inst = self.instantiate_from('endpoint-example-direct.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Endpoint instance')
        self.implEndpoint2(inst)

        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint2(inst2)

    def implEndpoint2(self, inst):
        self.assertEqual(inst.address.value, FHIRUrl("mailto:MARTIN.SMIETANKA@directnppes.com").value)
        self.assertEqual(inst.address.as_json(), "mailto:MARTIN.SMIETANKA@directnppes.com")
        self.assertEqual(inst.connectionType.code.value, FHIRCode("direct-project").value)
        self.assertEqual(inst.connectionType.code.as_json(), "direct-project")
        self.assertEqual(inst.id.value, FHIRString("direct-endpoint").value)
        self.assertEqual(inst.id.as_json(), "direct-endpoint")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("MARTIN SMIETANKA").value)
        self.assertEqual(inst.name.as_json(), "MARTIN SMIETANKA")
        self.assertEqual(inst.payloadType[0].coding[0].code.value, FHIRCode("urn:hl7-org:sdwg:ccda-structuredBody:1.1").value)
        self.assertEqual(inst.payloadType[0].coding[0].code.as_json(), "urn:hl7-org:sdwg:ccda-structuredBody:1.1")
        self.assertEqual(inst.payloadType[0].coding[0].system.value, FHIRUri("urn:oid:1.3.6.1.4.1.19376.1.2.3").value)
        self.assertEqual(inst.payloadType[0].coding[0].system.as_json(), "urn:oid:1.3.6.1.4.1.19376.1.2.3")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testEndpoint3(self):
        inst = self.instantiate_from('endpoint-example-wadors.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Endpoint instance')
        self.implEndpoint3(inst)

        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint3(inst2)

    def implEndpoint3(self, inst):
        self.assertEqual(inst.address.value, FHIRUrl("https://pacs.hospital.org/wado-rs").value)
        self.assertEqual(inst.address.as_json(), "https://pacs.hospital.org/wado-rs")
        self.assertEqual(inst.connectionType.code.value, FHIRCode("dicom-wado-rs").value)
        self.assertEqual(inst.connectionType.code.as_json(), "dicom-wado-rs")
        self.assertEqual(inst.connectionType.system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/endpoint-connection-type").value)
        self.assertEqual(inst.connectionType.system.as_json(), "http://terminology.hl7.org/CodeSystem/endpoint-connection-type")
        self.assertEqual(inst.id.value, FHIRString("example-wadors").value)
        self.assertEqual(inst.id.as_json(), "example-wadors")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("PACS Hospital DICOM WADO-RS endpoint").value)
        self.assertEqual(inst.name.as_json(), "PACS Hospital DICOM WADO-RS endpoint")
        self.assertEqual(inst.payloadMimeType[0].value, FHIRCode("application/dicom").value)
        self.assertEqual(inst.payloadMimeType[0].as_json(), "application/dicom")
        self.assertEqual(inst.payloadType[0].text.value, FHIRString("DICOM WADO-RS").value)
        self.assertEqual(inst.payloadType[0].text.as_json(), "DICOM WADO-RS")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testEndpoint4(self):
        inst = self.instantiate_from('endpoint-example-iid.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Endpoint instance')
        self.implEndpoint4(inst)

        js = inst.as_json()
        self.assertEqual("Endpoint", js["resourceType"])
        inst2 = endpoint.Endpoint(js)
        self.implEndpoint4(inst2)

    def implEndpoint4(self, inst):
        self.assertEqual(inst.address.value, FHIRUrl("https://pacs.hospital.org/IHEInvokeImageDisplay").value)
        self.assertEqual(inst.address.as_json(), "https://pacs.hospital.org/IHEInvokeImageDisplay")
        self.assertEqual(inst.connectionType.code.value, FHIRCode("ihe-iid").value)
        self.assertEqual(inst.connectionType.code.as_json(), "ihe-iid")
        self.assertEqual(inst.connectionType.system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/endpoint-connection-type").value)
        self.assertEqual(inst.connectionType.system.as_json(), "http://terminology.hl7.org/CodeSystem/endpoint-connection-type")
        self.assertEqual(inst.id.value, FHIRString("example-iid").value)
        self.assertEqual(inst.id.as_json(), "example-iid")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name.value, FHIRString("PACS Hospital Invoke Image Display endpoint").value)
        self.assertEqual(inst.name.as_json(), "PACS Hospital Invoke Image Display endpoint")
        self.assertEqual(inst.payloadType[0].text.value, FHIRString("DICOM IID").value)
        self.assertEqual(inst.payloadType[0].text.as_json(), "DICOM IID")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRUrl, FHIRCode, FHIRUri, FHIRString, FHIRDateTime