#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import documentmanifest

class DocumentManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DocumentManifest", js["resourceType"])
        return documentmanifest.DocumentManifest(js)

    def testDocumentManifest1(self):
        inst = self.instantiate_from('documentmanifest-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a DocumentManifest instance')
        self.implDocumentManifest1(inst)

        js = inst.as_json()
        self.assertEqual("DocumentManifest", js["resourceType"])
        inst2 = documentmanifest.DocumentManifest(js)
        self.implDocumentManifest1(inst2)

    def implDocumentManifest1(self, inst):
        self.assertEqual(inst.created.value, FHIRDateTime("2004-12-25T23:50:50-05:00").value)
        self.assertEqual(inst.created.as_json(), "2004-12-25T23:50:50-05:00")
        self.assertEqual(inst.description.value, FHIRString("Physical").value)
        self.assertEqual(inst.description.as_json(), "Physical")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/documents").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/documents")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("23425234234-2347").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "23425234234-2347")
        self.assertEqual(inst.masterIdentifier.system.value, FHIRUri("http://example.org/documents").value)
        self.assertEqual(inst.masterIdentifier.system.as_json(), "http://example.org/documents")
        self.assertEqual(inst.masterIdentifier.value.value, FHIRString("23425234234-2346").value)
        self.assertEqual(inst.masterIdentifier.value.as_json(), "23425234234-2346")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.related[0].identifier.system.value, FHIRUri("http://example.org/documents").value)
        self.assertEqual(inst.related[0].identifier.system.as_json(), "http://example.org/documents")
        self.assertEqual(inst.related[0].identifier.value.value, FHIRString("23425234234-9999").value)
        self.assertEqual(inst.related[0].identifier.value.as_json(), "23425234234-9999")
        self.assertEqual(inst.source.value, FHIRUri("urn:oid:1.3.6.1.4.1.21367.2009.1.2.1").value)
        self.assertEqual(inst.source.as_json(), "urn:oid:1.3.6.1.4.1.21367.2009.1.2.1")
        self.assertEqual(inst.status.value, FHIRCode("current").value)
        self.assertEqual(inst.status.as_json(), "current")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Text</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Text</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.text.value, FHIRString("History and Physical").value)
        self.assertEqual(inst.type.text.as_json(), "History and Physical")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRString, FHIRUri, FHIRCode