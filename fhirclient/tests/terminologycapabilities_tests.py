#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import terminologycapabilities

class TerminologyCapabilitiesTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("TerminologyCapabilities", js["resourceType"])
        return terminologycapabilities.TerminologyCapabilities(js)

    def testTerminologyCapabilities1(self):
        inst = self.instantiate_from('terminologycapabilities-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a TerminologyCapabilities instance')
        self.implTerminologyCapabilities1(inst)

        js = inst.as_json()
        self.assertEqual("TerminologyCapabilities", js["resourceType"])
        inst2 = terminologycapabilities.TerminologyCapabilities(js)
        self.implTerminologyCapabilities1(inst2)

    def implTerminologyCapabilities1(self, inst):
        self.assertEqual(inst.codeSearch.value, FHIRCode("explicit").value)
        self.assertEqual(inst.codeSearch.as_json(), "explicit")
        self.assertEqual(inst.contact[0].name.value, FHIRString("System Administrator").value)
        self.assertEqual(inst.contact[0].name.as_json(), "System Administrator")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("email").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "email")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("wile@acme.org").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "wile@acme.org")
        self.assertEqual(inst.date.value, FHIRDateTime("2012-01-04").value)
        self.assertEqual(inst.date.as_json(), "2012-01-04")
        self.assertEqual(inst.description.value, FHIRMarkdown("This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface").value)
        self.assertEqual(inst.description.as_json(), "This is the FHIR capability statement for the main EHR at ACME for the private interface - it does not describe the public interface")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.implementation.description.value, FHIRString("Acme Terminology Server").value)
        self.assertEqual(inst.implementation.description.as_json(), "Acme Terminology Server")
        self.assertEqual(inst.implementation.url.value, FHIRUrl("http://example.org/tx").value)
        self.assertEqual(inst.implementation.url.as_json(), "http://example.org/tx")
        self.assertEqual(inst.kind.value, FHIRCode("instance").value)
        self.assertEqual(inst.kind.as_json(), "instance")
        self.assertEqual(inst.name.value, FHIRString("ACME-EHR").value)
        self.assertEqual(inst.name.as_json(), "ACME-EHR")
        self.assertEqual(inst.publisher.value, FHIRString("ACME Corporation").value)
        self.assertEqual(inst.publisher.as_json(), "ACME Corporation")
        self.assertEqual(inst.software.name.value, FHIRString("TxServer").value)
        self.assertEqual(inst.software.name.as_json(), "TxServer")
        self.assertEqual(inst.software.version.value, FHIRString("0.1.2").value)
        self.assertEqual(inst.software.version.as_json(), "0.1.2")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("ACME EHR capability statement").value)
        self.assertEqual(inst.title.as_json(), "ACME EHR capability statement")
        self.assertEqual(inst.url.value, FHIRUri("urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311").value)
        self.assertEqual(inst.url.as_json(), "urn:uuid:68D043B5-9ECF-4559-A57A-396E0D452311")
        self.assertEqual(inst.version.value, FHIRString("20130510").value)
        self.assertEqual(inst.version.as_json(), "20130510")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRDateTime, FHIRMarkdown, FHIRUrl, FHIRUri