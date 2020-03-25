#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import researchelementdefinition

class ResearchElementDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ResearchElementDefinition", js["resourceType"])
        return researchelementdefinition.ResearchElementDefinition(js)

    def testResearchElementDefinition1(self):
        inst = self.instantiate_from('researchelementdefinition-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ResearchElementDefinition instance')
        self.implResearchElementDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("ResearchElementDefinition", js["resourceType"])
        inst2 = researchelementdefinition.ResearchElementDefinition(js)
        self.implResearchElementDefinition1(inst2)

    def implResearchElementDefinition1(self, inst):
        self.assertEqual(inst.characteristic[0].definitionCodeableConcept.text.value, FHIRString('Diabetic patients over 65').value)
        self.assertEqual(inst.characteristic[0].definitionCodeableConcept.text.as_json(), 'Diabetic patients over 65')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.status.value, FHIRCode('draft').value)
        self.assertEqual(inst.status.as_json(), 'draft')
        self.assertEqual(inst.text.div.value, FHIRString('<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>').value)
        self.assertEqual(inst.text.div.as_json(), '<div xmlns="http://www.w3.org/1999/xhtml">[Put rendering here]</div>')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.type.value, FHIRCode('population').value)
        self.assertEqual(inst.type.as_json(), 'population')


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri