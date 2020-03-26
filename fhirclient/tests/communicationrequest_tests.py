#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import communicationrequest

class CommunicationRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CommunicationRequest", js["resourceType"])
        return communicationrequest.CommunicationRequest(js)

    def testCommunicationRequest1(self):
        inst = self.instantiate_from('communicationrequest-example-fm-solicit-attachment.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CommunicationRequest instance')
        self.implCommunicationRequest1(inst)

        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest1(inst2)

    def implCommunicationRequest1(self, inst):
        self.assertEqual(inst.authoredOn.value, FHIRDateTime("2016-06-10T11:01:10-08:00").value)
        self.assertEqual(inst.authoredOn.as_json(), "2016-06-10T11:01:10-08:00")
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("SolicitedAttachmentRequest").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "SolicitedAttachmentRequest")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://acme.org/messagetypes").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://acme.org/messagetypes")
        self.assertEqual(inst.groupIdentifier.value.value, FHIRString("12345").value)
        self.assertEqual(inst.groupIdentifier.value.as_json(), "12345")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.jurisdiction.com/insurer/123456").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.jurisdiction.com/insurer/123456")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("ABC123").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "ABC123")
        self.assertEqual(inst.medium[0].coding[0].code.value, FHIRCode("WRITTEN").value)
        self.assertEqual(inst.medium[0].coding[0].code.as_json(), "WRITTEN")
        self.assertEqual(inst.medium[0].coding[0].display.value, FHIRString("written").value)
        self.assertEqual(inst.medium[0].coding[0].display.as_json(), "written")
        self.assertEqual(inst.medium[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ParticipationMode").value)
        self.assertEqual(inst.medium[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ParticipationMode")
        self.assertEqual(inst.medium[0].text.value, FHIRString("written").value)
        self.assertEqual(inst.medium[0].text.as_json(), "written")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.value, FHIRDateTime("2016-06-10T11:01:10-08:00").value)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-06-10T11:01:10-08:00")
        self.assertEqual(inst.payload[0].contentString.value, FHIRString("Please provide the accident report and any associated pictures to support your Claim# DEF5647.").value)
        self.assertEqual(inst.payload[0].contentString.as_json(), "Please provide the accident report and any associated pictures to support your Claim# DEF5647.")
        self.assertEqual(inst.priority.value, FHIRCode("routine").value)
        self.assertEqual(inst.priority.as_json(), "routine")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Request for Accident Report</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Request for Accident Report</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testCommunicationRequest2(self):
        inst = self.instantiate_from('communicationrequest-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a CommunicationRequest instance')
        self.implCommunicationRequest2(inst)

        js = inst.as_json()
        self.assertEqual("CommunicationRequest", js["resourceType"])
        inst2 = communicationrequest.CommunicationRequest(js)
        self.implCommunicationRequest2(inst2)

    def implCommunicationRequest2(self, inst):
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">To be filled out at a later time</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">To be filled out at a later time</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRCode, FHIRUri, FHIRString