#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import parameters

class ParametersTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Parameters", js["resourceType"])
        return parameters.Parameters(js)

    def testParameters1(self):
        inst = self.instantiate_from('parameters-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Parameters instance')
        self.implParameters1(inst)

        js = inst.as_json()
        self.assertEqual("Parameters", js["resourceType"])
        inst2 = parameters.Parameters(js)
        self.implParameters1(inst2)

    def implParameters1(self, inst):
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.parameter[0].name.value, FHIRString('exact').value)
        self.assertEqual(inst.parameter[0].name.as_json(), 'exact')
        self.assertTrue(inst.parameter[0].valueBoolean)
        self.assertEqual(inst.parameter[1].name.value, FHIRString('property').value)
        self.assertEqual(inst.parameter[1].name.as_json(), 'property')
        self.assertEqual(inst.parameter[1].part[0].name.value, FHIRString('code').value)
        self.assertEqual(inst.parameter[1].part[0].name.as_json(), 'code')
        self.assertEqual(inst.parameter[1].part[0].valueCode.value, FHIRCode('focus').value)
        self.assertEqual(inst.parameter[1].part[0].valueCode.as_json(), 'focus')
        self.assertEqual(inst.parameter[1].part[1].name.value, FHIRString('value').value)
        self.assertEqual(inst.parameter[1].part[1].name.as_json(), 'value')
        self.assertEqual(inst.parameter[1].part[1].valueCode.value, FHIRCode('top').value)
        self.assertEqual(inst.parameter[1].part[1].valueCode.as_json(), 'top')
        self.assertEqual(inst.parameter[2].name.value, FHIRString('patient').value)
        self.assertEqual(inst.parameter[2].name.as_json(), 'patient')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri