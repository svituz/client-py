#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import schedule

class ScheduleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Schedule", js["resourceType"])
        return schedule.Schedule(js)

    def testSchedule1(self):
        inst = self.instantiate_from('schedule-provider-location1-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Schedule instance')
        self.implSchedule1(inst)

        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule1(inst2)

    def implSchedule1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.comment.value, FHIRString("The slots attached to this schedule are for genetic counselling in the USS Enterprise-D Sickbay.").value)
        self.assertEqual(inst.comment.as_json(), "The slots attached to this schedule are for genetic counselling in the USS Enterprise-D Sickbay.")
        self.assertEqual(inst.id.value, FHIRString("exampleloc1").value)
        self.assertEqual(inst.id.as_json(), "exampleloc1")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/scheduleid").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("usual").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "usual")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("46").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "46")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.planningHorizon.end.value, FHIRDateTime("2017-12-25T09:30:00Z").value)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2017-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.value, FHIRDateTime("2017-12-25T09:15:00Z").value)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2017-12-25T09:15:00Z")
        self.assertEqual(inst.serviceCategory[0].coding[0].code.value, FHIRCode("17").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.as_json(), "17")
        self.assertEqual(inst.serviceCategory[0].coding[0].display.value, FHIRString("General Practice").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].display.as_json(), "General Practice")
        self.assertEqual(inst.serviceType[0].coding[0].code.value, FHIRCode("75").value)
        self.assertEqual(inst.serviceType[0].coding[0].code.as_json(), "75")
        self.assertEqual(inst.serviceType[0].coding[0].display.value, FHIRString("Genetic Counselling").value)
        self.assertEqual(inst.serviceType[0].coding[0].display.as_json(), "Genetic Counselling")
        self.assertEqual(inst.specialty[0].coding[0].code.value, FHIRCode("394580004").value)
        self.assertEqual(inst.specialty[0].coding[0].code.as_json(), "394580004")
        self.assertEqual(inst.specialty[0].coding[0].display.value, FHIRString("Clinical genetics").value)
        self.assertEqual(inst.specialty[0].coding[0].display.as_json(), "Clinical genetics")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testSchedule2(self):
        inst = self.instantiate_from('schedule-provider-location2-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Schedule instance')
        self.implSchedule2(inst)

        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule2(inst2)

    def implSchedule2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.comment.value, FHIRString("The slots attached to this schedule are for neurosurgery operations at Starfleet HQ only.").value)
        self.assertEqual(inst.comment.as_json(), "The slots attached to this schedule are for neurosurgery operations at Starfleet HQ only.")
        self.assertEqual(inst.id.value, FHIRString("exampleloc2").value)
        self.assertEqual(inst.id.as_json(), "exampleloc2")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/scheduleid").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("usual").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "usual")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("47").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "47")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.planningHorizon.end.value, FHIRDateTime("2017-12-25T09:30:00Z").value)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2017-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.value, FHIRDateTime("2017-12-25T09:15:00Z").value)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2017-12-25T09:15:00Z")
        self.assertEqual(inst.serviceCategory[0].coding[0].code.value, FHIRCode("31").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].code.as_json(), "31")
        self.assertEqual(inst.serviceCategory[0].coding[0].display.value, FHIRString("Specialist Surgical").value)
        self.assertEqual(inst.serviceCategory[0].coding[0].display.as_json(), "Specialist Surgical")
        self.assertEqual(inst.serviceType[0].coding[0].code.value, FHIRCode("221").value)
        self.assertEqual(inst.serviceType[0].coding[0].code.as_json(), "221")
        self.assertEqual(inst.serviceType[0].coding[0].display.value, FHIRString("Surgery - General").value)
        self.assertEqual(inst.serviceType[0].coding[0].display.as_json(), "Surgery - General")
        self.assertEqual(inst.specialty[0].coding[0].code.value, FHIRCode("394610002").value)
        self.assertEqual(inst.specialty[0].coding[0].code.as_json(), "394610002")
        self.assertEqual(inst.specialty[0].coding[0].display.value, FHIRString("Surgery-Neurosurgery").value)
        self.assertEqual(inst.specialty[0].coding[0].display.as_json(), "Surgery-Neurosurgery")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testSchedule3(self):
        inst = self.instantiate_from('schedule-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Schedule instance')
        self.implSchedule3(inst)

        js = inst.as_json()
        self.assertEqual("Schedule", js["resourceType"])
        inst2 = schedule.Schedule(js)
        self.implSchedule3(inst2)

    def implSchedule3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.comment.value, FHIRString("The slots attached to this schedule should be specialized to cover immunizations within the clinic").value)
        self.assertEqual(inst.comment.as_json(), "The slots attached to this schedule should be specialized to cover immunizations within the clinic")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/scheduleid").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/scheduleid")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("usual").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "usual")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("45").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "45")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.planningHorizon.end.value, FHIRDateTime("2013-12-25T09:30:00Z").value)
        self.assertEqual(inst.planningHorizon.end.as_json(), "2013-12-25T09:30:00Z")
        self.assertEqual(inst.planningHorizon.start.value, FHIRDateTime("2013-12-25T09:15:00Z").value)
        self.assertEqual(inst.planningHorizon.start.as_json(), "2013-12-25T09:15:00Z")
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
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRUri, FHIRCode, FHIRDateTime