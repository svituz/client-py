#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import appointmentresponse

class AppointmentResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AppointmentResponse", js["resourceType"])
        return appointmentresponse.AppointmentResponse(js)

    def testAppointmentResponse1(self):
        inst = self.instantiate_from('appointmentresponse-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a AppointmentResponse instance')
        self.implAppointmentResponse1(inst)

        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse1(inst2)

    def implAppointmentResponse1(self, inst):
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participantStatus.value, FHIRCode("accepted").value)
        self.assertEqual(inst.participantStatus.as_json(), "accepted")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testAppointmentResponse2(self):
        inst = self.instantiate_from('appointmentresponse-example-req.json')
        self.assertIsNotNone(inst, 'Must have instantiated a AppointmentResponse instance')
        self.implAppointmentResponse2(inst)

        js = inst.as_json()
        self.assertEqual("AppointmentResponse", js["resourceType"])
        inst2 = appointmentresponse.AppointmentResponse(js)
        self.implAppointmentResponse2(inst2)

    def implAppointmentResponse2(self, inst):
        self.assertEqual(inst.comment.value, FHIRString("can't we try for this time, can't do mornings").value)
        self.assertEqual(inst.comment.as_json(), "can't we try for this time, can't do mornings")
        self.assertEqual(inst.end.value, FHIRInstant("2013-12-25T13:30:00Z").value)
        self.assertEqual(inst.end.as_json(), "2013-12-25T13:30:00Z")
        self.assertEqual(inst.end.date, FHIRInstant('2013-12-25T13:30:00Z').date)
        self.assertEqual(inst.id.value, FHIRString("exampleresp").value)
        self.assertEqual(inst.id.as_json(), "exampleresp")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/sampleappointmentresponse-identifier").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/sampleappointmentresponse-identifier")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("response123").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "response123")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.participantStatus.value, FHIRCode("tentative").value)
        self.assertEqual(inst.participantStatus.as_json(), "tentative")
        self.assertEqual(inst.participantType[0].coding[0].code.value, FHIRCode("ATND").value)
        self.assertEqual(inst.participantType[0].coding[0].code.as_json(), "ATND")
        self.assertEqual(inst.participantType[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ParticipationType").value)
        self.assertEqual(inst.participantType[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ParticipationType")
        self.assertEqual(inst.start.value, FHIRInstant("2013-12-25T13:15:00Z").value)
        self.assertEqual(inst.start.as_json(), "2013-12-25T13:15:00Z")
        self.assertEqual(inst.start.date, FHIRInstant('2013-12-25T13:15:00Z').date)
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Accept Brian MRI results discussion</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri, FHIRInstant