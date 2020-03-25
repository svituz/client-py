#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import observationdefinition

class ObservationDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ObservationDefinition", js["resourceType"])
        return observationdefinition.ObservationDefinition(js)

    def testObservationDefinition1(self):
        inst = self.instantiate_from('observationdefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ObservationDefinition instance')
        self.implObservationDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("ObservationDefinition", js["resourceType"])
        inst2 = observationdefinition.ObservationDefinition(js)
        self.implObservationDefinition1(inst2)

    def implObservationDefinition1(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('15074-8').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '15074-8')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Glucose [Moles/volume] in Blood').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Glucose [Moles/volume] in Blood')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://loinc.org').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://loinc.org')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri