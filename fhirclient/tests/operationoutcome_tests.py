#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import operationoutcome

class OperationOutcomeTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OperationOutcome", js["resourceType"])
        return operationoutcome.OperationOutcome(js)

    def testOperationOutcome1(self):
        inst = self.instantiate_from('operationoutcome-example-searchfail.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationOutcome instance')
        self.implOperationOutcome1(inst)

        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome1(inst2)

    def implOperationOutcome1(self, inst):
        self.assertEqual(inst.id.value, FHIRString("searchfail").value)
        self.assertEqual(inst.id.as_json(), "searchfail")
        self.assertEqual(inst.issue[0].code.value, FHIRCode("code-invalid").value)
        self.assertEqual(inst.issue[0].code.as_json(), "code-invalid")
        self.assertEqual(inst.issue[0].details.text.value, FHIRString("The \"name\" parameter has the modifier \"exact\" which is not supported by this server").value)
        self.assertEqual(inst.issue[0].details.text.as_json(), "The \"name\" parameter has the modifier \"exact\" which is not supported by this server")
        self.assertEqual(inst.issue[0].location[0].value, FHIRString("http.name:exact").value)
        self.assertEqual(inst.issue[0].location[0].as_json(), "http.name:exact")
        self.assertEqual(inst.issue[0].severity.value, FHIRCode("fatal").value)
        self.assertEqual(inst.issue[0].severity.as_json(), "fatal")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOperationOutcome2(self):
        inst = self.instantiate_from('operationoutcome-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationOutcome instance')
        self.implOperationOutcome2(inst)

        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome2(inst2)

    def implOperationOutcome2(self, inst):
        self.assertEqual(inst.id.value, FHIRString("101").value)
        self.assertEqual(inst.id.as_json(), "101")
        self.assertEqual(inst.issue[0].code.value, FHIRCode("code-invalid").value)
        self.assertEqual(inst.issue[0].code.as_json(), "code-invalid")
        self.assertEqual(inst.issue[0].details.text.value, FHIRString("The code \"W\" is not known and not legal in this context").value)
        self.assertEqual(inst.issue[0].details.text.as_json(), "The code \"W\" is not known and not legal in this context")
        self.assertEqual(inst.issue[0].diagnostics.value, FHIRString("Acme.Interop.FHIRProcessors.Patient.processGender line 2453").value)
        self.assertEqual(inst.issue[0].diagnostics.as_json(), "Acme.Interop.FHIRProcessors.Patient.processGender line 2453")
        self.assertEqual(inst.issue[0].expression[0].value, FHIRString("Patient.gender").value)
        self.assertEqual(inst.issue[0].expression[0].as_json(), "Patient.gender")
        self.assertEqual(inst.issue[0].location[0].value, FHIRString("/f:Patient/f:gender").value)
        self.assertEqual(inst.issue[0].location[0].as_json(), "/f:Patient/f:gender")
        self.assertEqual(inst.issue[0].severity.value, FHIRCode("error").value)
        self.assertEqual(inst.issue[0].severity.as_json(), "error")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOperationOutcome3(self):
        inst = self.instantiate_from('operationoutcome-example-allok.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationOutcome instance')
        self.implOperationOutcome3(inst)

        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome3(inst2)

    def implOperationOutcome3(self, inst):
        self.assertEqual(inst.id.value, FHIRString("allok").value)
        self.assertEqual(inst.id.as_json(), "allok")
        self.assertEqual(inst.issue[0].code.value, FHIRCode("informational").value)
        self.assertEqual(inst.issue[0].code.as_json(), "informational")
        self.assertEqual(inst.issue[0].details.text.value, FHIRString("All OK").value)
        self.assertEqual(inst.issue[0].details.text.as_json(), "All OK")
        self.assertEqual(inst.issue[0].severity.value, FHIRCode("information").value)
        self.assertEqual(inst.issue[0].severity.as_json(), "information")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOperationOutcome4(self):
        inst = self.instantiate_from('operationoutcome-example-exception.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationOutcome instance')
        self.implOperationOutcome4(inst)

        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome4(inst2)

    def implOperationOutcome4(self, inst):
        self.assertEqual(inst.id.value, FHIRString("exception").value)
        self.assertEqual(inst.id.as_json(), "exception")
        self.assertEqual(inst.issue[0].code.value, FHIRCode("exception").value)
        self.assertEqual(inst.issue[0].code.as_json(), "exception")
        self.assertEqual(inst.issue[0].details.text.value, FHIRString("SQL Link Communication Error (dbx = 34234)").value)
        self.assertEqual(inst.issue[0].details.text.as_json(), "SQL Link Communication Error (dbx = 34234)")
        self.assertEqual(inst.issue[0].severity.value, FHIRCode("error").value)
        self.assertEqual(inst.issue[0].severity.as_json(), "error")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOperationOutcome5(self):
        inst = self.instantiate_from('operationoutcome-example-validationfail.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationOutcome instance')
        self.implOperationOutcome5(inst)

        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome5(inst2)

    def implOperationOutcome5(self, inst):
        self.assertEqual(inst.id.value, FHIRString("validationfail").value)
        self.assertEqual(inst.id.as_json(), "validationfail")
        self.assertEqual(inst.issue[0].code.value, FHIRCode("structure").value)
        self.assertEqual(inst.issue[0].code.as_json(), "structure")
        self.assertEqual(inst.issue[0].details.text.value, FHIRString("Error parsing resource XML (Unknown Content \"label\"").value)
        self.assertEqual(inst.issue[0].details.text.as_json(), "Error parsing resource XML (Unknown Content \"label\"")
        self.assertEqual(inst.issue[0].expression[0].value, FHIRString("Patient.identifier").value)
        self.assertEqual(inst.issue[0].expression[0].as_json(), "Patient.identifier")
        self.assertEqual(inst.issue[0].location[0].value, FHIRString("/f:Patient/f:identifier").value)
        self.assertEqual(inst.issue[0].location[0].as_json(), "/f:Patient/f:identifier")
        self.assertEqual(inst.issue[0].severity.value, FHIRCode("error").value)
        self.assertEqual(inst.issue[0].severity.as_json(), "error")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOperationOutcome6(self):
        inst = self.instantiate_from('operationoutcome-example-break-the-glass.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OperationOutcome instance')
        self.implOperationOutcome6(inst)

        js = inst.as_json()
        self.assertEqual("OperationOutcome", js["resourceType"])
        inst2 = operationoutcome.OperationOutcome(js)
        self.implOperationOutcome6(inst2)

    def implOperationOutcome6(self, inst):
        self.assertEqual(inst.id.value, FHIRString("break-the-glass").value)
        self.assertEqual(inst.id.as_json(), "break-the-glass")
        self.assertEqual(inst.issue[0].code.value, FHIRCode("suppressed").value)
        self.assertEqual(inst.issue[0].code.as_json(), "suppressed")
        self.assertEqual(inst.issue[0].details.coding[0].code.value, FHIRCode("ETREAT").value)
        self.assertEqual(inst.issue[0].details.coding[0].code.as_json(), "ETREAT")
        self.assertEqual(inst.issue[0].details.coding[0].display.value, FHIRString("Emergency Treatment").value)
        self.assertEqual(inst.issue[0].details.coding[0].display.as_json(), "Emergency Treatment")
        self.assertEqual(inst.issue[0].details.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.issue[0].details.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.issue[0].details.text.value, FHIRString("Additional information may be available using the Break-The-Glass Protocol").value)
        self.assertEqual(inst.issue[0].details.text.as_json(), "Additional information may be available using the Break-The-Glass Protocol")
        self.assertEqual(inst.issue[0].severity.value, FHIRCode("information").value)
        self.assertEqual(inst.issue[0].severity.as_json(), "information")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri