#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import communication

class CommunicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Communication", js["resourceType"])
        return communication.Communication(js)

    def testCommunication1(self):
        inst = self.instantiate_from('communication-example-fm-solicited-attachment.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Communication instance')
        self.implCommunication1(inst)

        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication1(inst2)

    def implCommunication1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("SolicitedAttachment").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "SolicitedAttachment")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://acme.org/messagetypes").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://acme.org/messagetypes")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.providerco.com/communication").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.providerco.com/communication")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.payload[0].contentAttachment.contentType.value, FHIRCode("application/pdf").value)
        self.assertEqual(inst.payload[0].contentAttachment.contentType.as_json(), "application/pdf")
        self.assertEqual(inst.payload[0].contentAttachment.creation.value, FHIRDateTime("2010-02-01T11:50:23-05:00").value)
        self.assertEqual(inst.payload[0].contentAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00")
        self.assertEqual(inst.payload[0].contentAttachment.data.value, FHIRBase64Binary("SGVsbG8=").value)
        self.assertEqual(inst.payload[0].contentAttachment.data.as_json(), "SGVsbG8=")
        self.assertEqual(inst.payload[0].contentAttachment.title.value, FHIRString("accident notes 20100201.pdf").value)
        self.assertEqual(inst.payload[0].contentAttachment.title.as_json(), "accident notes 20100201.pdf")
        self.assertEqual(inst.payload[1].contentAttachment.contentType.value, FHIRCode("application/pdf").value)
        self.assertEqual(inst.payload[1].contentAttachment.contentType.as_json(), "application/pdf")
        self.assertEqual(inst.payload[1].contentAttachment.creation.value, FHIRDateTime("2010-02-01T10:57:34+01:00").value)
        self.assertEqual(inst.payload[1].contentAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00")
        self.assertEqual(inst.payload[1].contentAttachment.hash.value, FHIRBase64Binary("SGVsbG8gdGhlcmU=").value)
        self.assertEqual(inst.payload[1].contentAttachment.hash.as_json(), "SGVsbG8gdGhlcmU=")
        self.assertEqual(inst.payload[1].contentAttachment.size.value, FHIRUnsignedInt('104274').value)
        self.assertEqual(inst.payload[1].contentAttachment.size.as_json(), 104274)
        self.assertEqual(inst.payload[1].contentAttachment.url.value, FHIRUrl("http://happyvalley.com/docs/AB12345").value)
        self.assertEqual(inst.payload[1].contentAttachment.url.as_json(), "http://happyvalley.com/docs/AB12345")
        self.assertEqual(inst.sent.value, FHIRDateTime("2016-06-12T18:01:10-08:00").value)
        self.assertEqual(inst.sent.as_json(), "2016-06-12T18:01:10-08:00")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment in response to a Request</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment in response to a Request</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testCommunication2(self):
        inst = self.instantiate_from('communication-example-fm-attachment.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Communication instance')
        self.implCommunication2(inst)

        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication2(inst2)

    def implCommunication2(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("SolicitedAttachment").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "SolicitedAttachment")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://acme.org/messagetypes").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://acme.org/messagetypes")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.providerco.com/communication").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.providerco.com/communication")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.payload[0].contentAttachment.contentType.value, FHIRCode("application/pdf").value)
        self.assertEqual(inst.payload[0].contentAttachment.contentType.as_json(), "application/pdf")
        self.assertEqual(inst.payload[0].contentAttachment.creation.value, FHIRDateTime("2010-02-01T11:50:23-05:00").value)
        self.assertEqual(inst.payload[0].contentAttachment.creation.as_json(), "2010-02-01T11:50:23-05:00")
        self.assertEqual(inst.payload[0].contentAttachment.data.value, FHIRBase64Binary("SGVsbG8=").value)
        self.assertEqual(inst.payload[0].contentAttachment.data.as_json(), "SGVsbG8=")
        self.assertEqual(inst.payload[0].contentAttachment.title.value, FHIRString("accident notes 20100201.pdf").value)
        self.assertEqual(inst.payload[0].contentAttachment.title.as_json(), "accident notes 20100201.pdf")
        self.assertEqual(inst.payload[1].contentAttachment.contentType.value, FHIRCode("application/pdf").value)
        self.assertEqual(inst.payload[1].contentAttachment.contentType.as_json(), "application/pdf")
        self.assertEqual(inst.payload[1].contentAttachment.creation.value, FHIRDateTime("2010-02-01T10:57:34+01:00").value)
        self.assertEqual(inst.payload[1].contentAttachment.creation.as_json(), "2010-02-01T10:57:34+01:00")
        self.assertEqual(inst.payload[1].contentAttachment.hash.value, FHIRBase64Binary("SGVsbG8gdGhlcmU=").value)
        self.assertEqual(inst.payload[1].contentAttachment.hash.as_json(), "SGVsbG8gdGhlcmU=")
        self.assertEqual(inst.payload[1].contentAttachment.size.value, FHIRUnsignedInt('104274').value)
        self.assertEqual(inst.payload[1].contentAttachment.size.as_json(), 104274)
        self.assertEqual(inst.payload[1].contentAttachment.url.value, FHIRUrl("http://example.org/docs/AB12345").value)
        self.assertEqual(inst.payload[1].contentAttachment.url.as_json(), "http://example.org/docs/AB12345")
        self.assertEqual(inst.sent.value, FHIRDateTime("2016-06-12T18:01:10-08:00").value)
        self.assertEqual(inst.sent.as_json(), "2016-06-12T18:01:10-08:00")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment which is unsolicited</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Attachment which is unsolicited</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testCommunication3(self):
        inst = self.instantiate_from('communication-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Communication instance')
        self.implCommunication3(inst)

        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication3(inst2)

    def implCommunication3(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("Alert").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "Alert")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://acme.org/messagetypes").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://acme.org/messagetypes")
        self.assertEqual(inst.category[0].text.value, FHIRString("Alert").value)
        self.assertEqual(inst.category[0].text.as_json(), "Alert")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("urn:oid:1.3.4.5.6.7").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.text.value, FHIRString("Paging System").value)
        self.assertEqual(inst.identifier[0].type.text.as_json(), "Paging System")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("2345678901").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "2345678901")
        self.assertEqual(inst.instantiatesUri[0].value, FHIRUri("http://example.org/hyperkalemia").value)
        self.assertEqual(inst.instantiatesUri[0].as_json(), "http://example.org/hyperkalemia")
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
        self.assertEqual(inst.payload[0].contentString.value, FHIRString("Patient 1 has a very high serum potassium value (7.2 mmol/L on 2014-Dec-12 at 5:55 pm)").value)
        self.assertEqual(inst.payload[0].contentString.as_json(), "Patient 1 has a very high serum potassium value (7.2 mmol/L on 2014-Dec-12 at 5:55 pm)")
        self.assertEqual(inst.received.value, FHIRDateTime("2014-12-12T18:01:11-08:00").value)
        self.assertEqual(inst.received.as_json(), "2014-12-12T18:01:11-08:00")
        self.assertEqual(inst.sent.value, FHIRDateTime("2014-12-12T18:01:10-08:00").value)
        self.assertEqual(inst.sent.as_json(), "2014-12-12T18:01:10-08:00")
        self.assertEqual(inst.status.value, FHIRCode("completed").value)
        self.assertEqual(inst.status.as_json(), "completed")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient has very high serum potassium</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient has very high serum potassium</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString, FHIRDateTime, FHIRBase64Binary, FHIRUnsignedInt, FHIRUrl