#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import slot

class SlotTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Slot", js["resourceType"])
        return slot.Slot(js)

    def testSlot1(self):
        inst = self.instantiate_from('slot-example-tentative.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Slot instance')
        self.implSlot1(inst)

        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot1(inst2)

    def implSlot1(self, inst):
        self.assertEqual(inst.comment.value, FHIRString("Dr Careful is out of the office").value)
        self.assertEqual(inst.comment.as_json(), "Dr Careful is out of the office")
        self.assertEqual(inst.end.value, FHIRInstant("2013-12-25T10:00:00Z").value)
        self.assertEqual(inst.end.as_json(), "2013-12-25T10:00:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2013-12-25T10:00:00Z').date)
        self.assertEqual(inst.id.value, FHIRString("2").value)
        self.assertEqual(inst.id.as_json(), "2")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.serviceCategory[0].coding[0].code.value, FHIRCode("17").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.as_json(), "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display.value, FHIRString("General Practice").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].display.as_json(), "General Practice")
        self.assertEqual(inst.start.value, FHIRInstant("2013-12-25T09:45:00Z").value)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(inst.start.date, FHIRInstant('2013-12-25T09:45:00Z').date)
        self.assertEqual(inst.status.value, FHIRCode("busy-tentative").value)
        self.assertEqual(inst.status.as_json(), "busy-tentative")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testSlot2(self):
        inst = self.instantiate_from('slot-example-busy.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Slot instance')
        self.implSlot2(inst)

        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot2(inst2)

    def implSlot2(self, inst):
        self.assertEqual(inst.comment.value, FHIRString("Assessments should be performed before requesting appointments in this slot.").value)
        self.assertEqual(inst.comment.as_json(), "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.value, FHIRInstant("2013-12-25T09:15:00Z").value)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2013-12-25T09:15:00Z').date)
        self.assertEqual(inst.id.value, FHIRString("1").value)
        self.assertEqual(inst.id.as_json(), "1")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/identifiers/slots").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/identifiers/slots")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("123132").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "123132")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertTrue(inst.overbooked)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.value, FHIRCode("17").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.as_json(), "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display.value, FHIRString("General Practice").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].display.as_json(), "General Practice")
        self.assertEqual(inst.start.value, FHIRInstant("2013-12-25T09:00:00Z").value)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:00:00Z")
        self.assertEqual(inst.start.date, FHIRInstant('2013-12-25T09:00:00Z').date)
        self.assertEqual(inst.status.value, FHIRCode("busy").value)
        self.assertEqual(inst.status.as_json(), "busy")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testSlot3(self):
        inst = self.instantiate_from('slot-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Slot instance')
        self.implSlot3(inst)

        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot3(inst2)

    def implSlot3(self, inst):
        self.assertEqual(inst.appointmentType.coding[0].code.value, FHIRCode("WALKIN").value)
        self.assertEqual(inst.appointmentType.coding[0].code.as_json(), "WALKIN")
        self.assertEqual(inst.appointmentType.coding[0].display.value, FHIRString("A previously unscheduled walk-in visit").value)
        self.assertEqual(inst.appointmentType.coding[0].display.as_json(), "A previously unscheduled walk-in visit")
        self.assertEqual(inst.appointmentType.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v2-0276").value)
        self.assertEqual(inst.appointmentType.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v2-0276")
        self.assertEqual(inst.comment.value, FHIRString("Assessments should be performed before requesting appointments in this slot.").value)
        self.assertEqual(inst.comment.as_json(), "Assessments should be performed before requesting appointments in this slot.")
        self.assertEqual(inst.end.value, FHIRInstant("2013-12-25T09:30:00Z").value)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2013-12-25T09:30:00Z').date)
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.serviceCategory[0].coding[0].code.value, FHIRCode("17").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.as_json(), "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display.value, FHIRString("General Practice").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].display.as_json(), "General Practice")
        self.assertEqual(inst.serviceType[0].coding[0].code.value, FHIRCode("57").value)
        self.assertEqual(inst.serviceType[0].coding[0].code.as_json(), "57")
        self.assertEqual(inst.serviceType[0].coding[0].display.value, FHIRString("Immunization").value)
        self.assertEqual(inst.serviceType[0].coding[0].display.as_json(), "Immunization")
        self.assertEqual(inst.specialty[0].coding[0].code.value, FHIRCode("408480009").value)
        self.assertEqual(inst.specialty[0].coding[0].code.as_json(), "408480009")
        self.assertEqual(inst.specialty[0].coding[0].display.value, FHIRString("Clinical immunology").value)
        self.assertEqual(inst.specialty[0].coding[0].display.as_json(), "Clinical immunology")
        self.assertEqual(inst.start.value, FHIRInstant("2013-12-25T09:15:00Z").value)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:15:00Z")
        self.assertEqual(inst.start.date, FHIRInstant('2013-12-25T09:15:00Z').date)
        self.assertEqual(inst.status.value, FHIRCode("free").value)
        self.assertEqual(inst.status.as_json(), "free")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testSlot4(self):
        inst = self.instantiate_from('slot-example-unavailable.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Slot instance')
        self.implSlot4(inst)

        js = inst.as_json()
        self.assertEqual("Slot", js["resourceType"])
        inst2 = slot.Slot(js)
        self.implSlot4(inst2)

    def implSlot4(self, inst):
        self.assertEqual(inst.comment.value, FHIRString("Dr Careful is out of the office").value)
        self.assertEqual(inst.comment.as_json(), "Dr Careful is out of the office")
        self.assertEqual(inst.end.value, FHIRInstant("2013-12-25T09:45:00Z").value)
        self.assertEqual(inst.end.as_json(), "2013-12-25T09:45:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2013-12-25T09:45:00Z').date)
        self.assertEqual(inst.id.value, FHIRString("3").value)
        self.assertEqual(inst.id.as_json(), "3")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.serviceCategory[0].coding[0].code.value, FHIRCode("17").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.as_json(), "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display.value, FHIRString("General Practice").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].display.as_json(), "General Practice")
        self.assertEqual(inst.start.value, FHIRInstant("2013-12-25T09:30:00Z").value)
        self.assertEqual(inst.start.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.start.date, FHIRInstant('2013-12-25T09:30:00Z').date)
        self.assertEqual(inst.status.value, FHIRCode("busy-unavailable").value)
        self.assertEqual(inst.status.as_json(), "busy-unavailable")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRInstant, FHIRCode, FHIRUri