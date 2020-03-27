#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import requestgroup

class RequestGroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RequestGroup", js["resourceType"])
        return requestgroup.RequestGroup(js)

    def testRequestGroup1(self):
        inst = self.instantiate_from('requestgroup-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a RequestGroup instance')
        self.implRequestGroup1(inst)

        js = inst.as_json()
        self.assertEqual("RequestGroup", js["resourceType"])
        inst2 = requestgroup.RequestGroup(js)
        self.implRequestGroup1(inst2)

    def implRequestGroup1(self, inst):
        self.assertEqual(inst.action[0].action[0].description.value, FHIRString("Administer medication 1").value)
        self.assertEqual(inst.action[0].action[0].description.as_json(), "Administer medication 1")
        self.assertEqual(inst.action[0].action[0].id.value, FHIRString("medication-action-1").value)
        self.assertEqual(inst.action[0].action[0].id.as_json(), "medication-action-1")
        self.assertEqual(inst.action[0].action[0].type.coding[0].code.value, FHIRCode("create").value)
        self.assertEqual(inst.action[0].action[0].type.coding[0].code.as_json(), "create")
        self.assertEqual(inst.action[0].action[1].description.value, FHIRString("Administer medication 2").value)
        self.assertEqual(inst.action[0].action[1].description.as_json(), "Administer medication 2")
        self.assertEqual(inst.action[0].action[1].id.value, FHIRString("medication-action-2").value)
        self.assertEqual(inst.action[0].action[1].id.as_json(), "medication-action-2")
        self.assertEqual(inst.action[0].action[1].relatedAction[0].actionId.value, FHIRId("medication-action-1").value)
        self.assertEqual(inst.action[0].action[1].relatedAction[0].actionId.as_json(), "medication-action-1")
        self.assertEqual(inst.action[0].action[1].relatedAction[0].offsetDuration.unit.value, FHIRString("h").value)
        self.assertEqual(inst.action[0].action[1].relatedAction[0].offsetDuration.unit.as_json(), "h")
        self.assertEqual(inst.action[0].action[1].relatedAction[0].offsetDuration.value, 1)
        self.assertEqual(inst.action[0].action[1].relatedAction[0].relationship.value, FHIRCode("after-end").value)
        self.assertEqual(inst.action[0].action[1].relatedAction[0].relationship.as_json(), "after-end")
        self.assertEqual(inst.action[0].action[1].type.coding[0].code.value, FHIRCode("create").value)
        self.assertEqual(inst.action[0].action[1].type.coding[0].code.as_json(), "create")
        self.assertEqual(inst.action[0].cardinalityBehavior.value, FHIRCode("single").value)
        self.assertEqual(inst.action[0].cardinalityBehavior.as_json(), "single")
        self.assertEqual(inst.action[0].description.value, FHIRString("Administer medications at the appropriate time").value)
        self.assertEqual(inst.action[0].description.as_json(), "Administer medications at the appropriate time")
        self.assertEqual(inst.action[0].groupingBehavior.value, FHIRCode("logical-group").value)
        self.assertEqual(inst.action[0].groupingBehavior.as_json(), "logical-group")
        self.assertEqual(inst.action[0].precheckBehavior.value, FHIRCode("yes").value)
        self.assertEqual(inst.action[0].precheckBehavior.as_json(), "yes")
        self.assertEqual(inst.action[0].prefix.value, FHIRString("1").value)
        self.assertEqual(inst.action[0].prefix.as_json(), "1")
        self.assertEqual(inst.action[0].requiredBehavior.value, FHIRCode("must").value)
        self.assertEqual(inst.action[0].requiredBehavior.as_json(), "must")
        self.assertEqual(inst.action[0].selectionBehavior.value, FHIRCode("all").value)
        self.assertEqual(inst.action[0].selectionBehavior.as_json(), "all")
        self.assertEqual(inst.action[0].textEquivalent.value, FHIRString("Administer medication 1, followed an hour later by medication 2").value)
        self.assertEqual(inst.action[0].textEquivalent.as_json(), "Administer medication 1, followed an hour later by medication 2")
        self.assertEqual(inst.action[0].timingDateTime.value, FHIRDateTime("2017-03-06T19:00:00Z").value)
        self.assertEqual(inst.action[0].timingDateTime.as_json(), "2017-03-06T19:00:00Z")
        self.assertEqual(inst.action[0].title.value, FHIRString("Administer Medications").value)
        self.assertEqual(inst.action[0].title.as_json(), "Administer Medications")
        self.assertEqual(inst.authoredOn.value, FHIRDateTime("2017-03-06T17:31:00Z").value)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-06T17:31:00Z")
        self.assertEqual(inst.contained[0].id.value, FHIRString("medicationrequest-1").value)
        self.assertEqual(inst.contained[0].id.as_json(), "medicationrequest-1")
        self.assertEqual(inst.contained[1].id.value, FHIRString("medicationrequest-2").value)
        self.assertEqual(inst.contained[1].id.as_json(), "medicationrequest-2")
        self.assertEqual(inst.groupIdentifier.system.value, FHIRUri("http://example.org/treatment-group").value)
        self.assertEqual(inst.groupIdentifier.system.as_json(), "http://example.org/treatment-group")
        self.assertEqual(inst.groupIdentifier.value.value, FHIRString("00001").value)
        self.assertEqual(inst.groupIdentifier.value.as_json(), "00001")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("requestgroup-1").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "requestgroup-1")
        self.assertEqual(inst.intent.value, FHIRCode("plan").value)
        self.assertEqual(inst.intent.as_json(), "plan")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown("Additional notes about the request group").value)
        self.assertEqual(inst.note[0].text.as_json(), "Additional notes about the request group")
        self.assertEqual(inst.priority.value, FHIRCode("routine").value)
        self.assertEqual(inst.priority.as_json(), "routine")
        self.assertEqual(inst.reasonCode[0].text.value, FHIRString("Treatment").value)
        self.assertEqual(inst.reasonCode[0].text.as_json(), "Treatment")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Example RequestGroup illustrating related actions to administer medications in sequence with time delay.</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Example RequestGroup illustrating related actions to administer medications in sequence with time delay.</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testRequestGroup2(self):
        inst = self.instantiate_from('requestgroup-kdn5-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a RequestGroup instance')
        self.implRequestGroup2(inst)

        js = inst.as_json()
        self.assertEqual("RequestGroup", js["resourceType"])
        inst2 = requestgroup.RequestGroup(js)
        self.implRequestGroup2(inst2)

    def implRequestGroup2(self, inst):
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].url.value, FHIRUri("day").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].url.as_json(), "day")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[0].valueInteger, 1)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].url.value, FHIRUri("day").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].url.as_json(), "day")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].extension[1].valueInteger, 8)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].extension[0].url.as_json(), "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].id.value, FHIRString("action-1").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].id.as_json(), "action-1")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].textEquivalent.value, FHIRString("Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[0].textEquivalent.as_json(), "Gemcitabine 1250 mg/m² IV over 30 minutes on days 1 and 8")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].url.value, FHIRUri("day").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].url.as_json(), "day")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].extension[0].extension[0].valueInteger, 1)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].extension[0].url.value, FHIRUri("http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].extension[0].url.as_json(), "http://hl7.org/fhir/StructureDefinition/timing-daysOfCycle")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].id.value, FHIRString("action-2").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].id.as_json(), "action-2")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].actionId.value, FHIRId("action-1").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].actionId.as_json(), "action-1")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].relationship.value, FHIRCode("concurrent-with-start").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].relatedAction[0].relationship.as_json(), "concurrent-with-start")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].textEquivalent.value, FHIRString("CARBOplatin AUC 5 IV over 30 minutes on Day 1").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].action[1].textEquivalent.as_json(), "CARBOplatin AUC 5 IV over 30 minutes on Day 1")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].id.value, FHIRString("cycle-definition-1").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].id.as_json(), "cycle-definition-1")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].textEquivalent.value, FHIRString("21-day cycle for 6 cycles").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].textEquivalent.as_json(), "21-day cycle for 6 cycles")
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count.value, FHIRPositiveInt('6').value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.count.as_json(), 6)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.duration, 21)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.durationUnit.value, FHIRCode("d").value)
        self.assertEqual(inst.action[0].action[0].action[0].action[0].timingTiming.repeat.durationUnit.as_json(), "d")
        self.assertEqual(inst.action[0].action[0].action[0].groupingBehavior.value, FHIRCode("sentence-group").value)
        self.assertEqual(inst.action[0].action[0].action[0].groupingBehavior.as_json(), "sentence-group")
        self.assertEqual(inst.action[0].action[0].action[0].selectionBehavior.value, FHIRCode("exactly-one").value)
        self.assertEqual(inst.action[0].action[0].action[0].selectionBehavior.as_json(), "exactly-one")
        self.assertEqual(inst.action[0].action[0].selectionBehavior.value, FHIRCode("all").value)
        self.assertEqual(inst.action[0].action[0].selectionBehavior.as_json(), "all")
        self.assertEqual(inst.action[0].selectionBehavior.value, FHIRCode("exactly-one").value)
        self.assertEqual(inst.action[0].selectionBehavior.as_json(), "exactly-one")
        self.assertEqual(inst.authoredOn.value, FHIRDateTime("2017-03-06T17:31:00Z").value)
        self.assertEqual(inst.authoredOn.as_json(), "2017-03-06T17:31:00Z")
        self.assertEqual(inst.contained[0].id.value, FHIRString("1111").value)
        self.assertEqual(inst.contained[0].id.as_json(), "1111")
        self.assertEqual(inst.contained[1].id.value, FHIRString("2222").value)
        self.assertEqual(inst.contained[1].id.as_json(), "2222")
        self.assertEqual(inst.id.value, FHIRString("kdn5-example").value)
        self.assertEqual(inst.id.as_json(), "kdn5-example")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("requestgroup-kdn5").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "requestgroup-kdn5")
        self.assertEqual(inst.instantiatesCanonical[0].value, FHIRCanonical("PlanDefinition/KDN5").value)
        self.assertEqual(inst.instantiatesCanonical[0].as_json(), "PlanDefinition/KDN5")
        self.assertEqual(inst.intent.value, FHIRCode("plan").value)
        self.assertEqual(inst.intent.as_json(), "plan")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.value, FHIRCode("routine").value)
        self.assertEqual(inst.priority.as_json(), "routine")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">Administer gemcitabine and carboplatin.</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">Administer gemcitabine and carboplatin.</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRId, FHIRDateTime, FHIRUri, FHIRMarkdown, FHIRPositiveInt, FHIRCanonical