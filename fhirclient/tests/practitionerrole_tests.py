#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import practitionerrole

class PractitionerRoleTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("PractitionerRole", js["resourceType"])
        return practitionerrole.PractitionerRole(js)

    def testPractitionerRole1(self):
        inst = self.instantiate_from('practitionerrole-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a PractitionerRole instance')
        self.implPractitionerRole1(inst)

        js = inst.as_json()
        self.assertEqual("PractitionerRole", js["resourceType"])
        inst2 = practitionerrole.PractitionerRole(js)
        self.implPractitionerRole1(inst2)

    def implPractitionerRole1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.availabilityExceptions.value, FHIRString("Adam is generally unavailable on public holidays and during the Christmas/New Year break").value)
        self.assertEqual(inst.availabilityExceptions.as_json(), "Adam is generally unavailable on public holidays and during the Christmas/New Year break")
        self.assertEqual(inst.availableTime[0].availableEndTime.value, FHIRTime("16:30:00").value)
        self.assertEqual(inst.availableTime[0].availableEndTime.as_json(), "16:30:00")
        self.assertEqual(inst.availableTime[0].availableEndTime.date, FHIRTime('16:30:00').date)
        self.assertEqual(inst.availableTime[0].availableStartTime.value, FHIRTime("09:00:00").value)
        self.assertEqual(inst.availableTime[0].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(inst.availableTime[0].availableStartTime.date, FHIRTime('09:00:00').date)
        self.assertEqual(inst.availableTime[0].daysOfWeek[0].value, FHIRCode("mon").value)
        self.assertEqual(inst.availableTime[0].daysOfWeek[0].as_json(), "mon")
        self.assertEqual(inst.availableTime[0].daysOfWeek[1].value, FHIRCode("tue").value)
        self.assertEqual(inst.availableTime[0].daysOfWeek[1].as_json(), "tue")
        self.assertEqual(inst.availableTime[0].daysOfWeek[2].value, FHIRCode("wed").value)
        self.assertEqual(inst.availableTime[0].daysOfWeek[2].as_json(), "wed")
        self.assertEqual(inst.availableTime[1].availableEndTime.value, FHIRTime("12:00:00").value)
        self.assertEqual(inst.availableTime[1].availableEndTime.as_json(), "12:00:00")
        self.assertEqual(inst.availableTime[1].availableEndTime.date, FHIRTime('12:00:00').date)
        self.assertEqual(inst.availableTime[1].availableStartTime.value, FHIRTime("09:00:00").value)
        self.assertEqual(inst.availableTime[1].availableStartTime.as_json(), "09:00:00")
        self.assertEqual(inst.availableTime[1].availableStartTime.date, FHIRTime('09:00:00').date)
        self.assertEqual(inst.availableTime[1].daysOfWeek[0].value, FHIRCode("thu").value)
        self.assertEqual(inst.availableTime[1].daysOfWeek[0].as_json(), "thu")
        self.assertEqual(inst.availableTime[1].daysOfWeek[1].value, FHIRCode("fri").value)
        self.assertEqual(inst.availableTime[1].daysOfWeek[1].as_json(), "fri")
        self.assertEqual(inst.code[0].coding[0].code.value, FHIRCode("RP").value)
        self.assertEqual(inst.code[0].coding[0].code.as_json(), "RP")
        self.assertEqual(inst.code[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v2-0286").value)
        self.assertEqual(inst.code[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v2-0286")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.acme.org/practitioners").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("23").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "23")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.notAvailable[0].description.value, FHIRString("Adam will be on extended leave during May 2017").value)
        self.assertEqual(inst.notAvailable[0].description.as_json(), "Adam will be on extended leave during May 2017")
        self.assertEqual(inst.notAvailable[0].during.end.value, FHIRDateTime("2017-05-20").value)
        self.assertEqual(inst.notAvailable[0].during.end.as_json(), "2017-05-20")
        self.assertEqual(inst.notAvailable[0].during.start.value, FHIRDateTime("2017-05-01").value)
        self.assertEqual(inst.notAvailable[0].during.start.as_json(), "2017-05-01")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2012-03-31").value)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2012-01-01").value)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(inst.specialty[0].coding[0].code.value, FHIRCode("408443003").value)
        self.assertEqual(inst.specialty[0].coding[0].code.as_json(), "408443003")
        self.assertEqual(inst.specialty[0].coding[0].display.value, FHIRString("General medical practice").value)
        self.assertEqual(inst.specialty[0].coding[0].display.as_json(), "General medical practice")
        self.assertEqual(inst.specialty[0].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.specialty[0].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system.value, FHIRCode("phone").value)
        self.assertEqual(inst.telecom[0].system.as_json(), "phone")
        self.assertEqual(inst.telecom[0].use.value, FHIRCode("work").value)
        self.assertEqual(inst.telecom[0].use.as_json(), "work")
        self.assertEqual(inst.telecom[0].value.value, FHIRString("(03) 5555 6473").value)
        self.assertEqual(inst.telecom[0].value.as_json(), "(03) 5555 6473")
        self.assertEqual(inst.telecom[1].system.value, FHIRCode("email").value)
        self.assertEqual(inst.telecom[1].system.as_json(), "email")
        self.assertEqual(inst.telecom[1].use.value, FHIRCode("work").value)
        self.assertEqual(inst.telecom[1].use.as_json(), "work")
        self.assertEqual(inst.telecom[1].value.value, FHIRString("adam.southern@example.org").value)
        self.assertEqual(inst.telecom[1].value.as_json(), "adam.southern@example.org")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRTime, FHIRCode, FHIRUri, FHIRDateTime