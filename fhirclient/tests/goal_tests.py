#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import goal

class GoalTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Goal", js["resourceType"])
        return goal.Goal(js)

    def testGoal1(self):
        inst = self.instantiate_from('goal-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Goal instance')
        self.implGoal1(inst)

        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal1(inst2)

    def implGoal1(self, inst):
        self.assertEqual(inst.category[0].coding[0].code.value, FHIRCode("dietary").value)
        self.assertEqual(inst.category[0].coding[0].code.as_json(), "dietary")
        self.assertEqual(inst.category[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/goal-category").value)
        self.assertEqual(inst.category[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/goal-category")
        self.assertEqual(inst.description.text.value, FHIRString("Target weight is 160 to 180 lbs.").value)
        self.assertEqual(inst.description.text.as_json(), "Target weight is 160 to 180 lbs.")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("123").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "123")
        self.assertEqual(inst.lifecycleStatus.value, FHIRCode("on-hold").value)
        self.assertEqual(inst.lifecycleStatus.as_json(), "on-hold")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.priority.coding[0].code.value, FHIRCode("high-priority").value)
        self.assertEqual(inst.priority.coding[0].code.as_json(), "high-priority")
        self.assertEqual(inst.priority.coding[0].display.value, FHIRString("High Priority").value)
        self.assertEqual(inst.priority.coding[0].display.as_json(), "High Priority")
        self.assertEqual(inst.priority.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/goal-priority").value)
        self.assertEqual(inst.priority.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/goal-priority")
        self.assertEqual(inst.priority.text.value, FHIRString("high").value)
        self.assertEqual(inst.priority.text.as_json(), "high")
        self.assertEqual(inst.startDate.value, FHIRDate("2015-04-05").value)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(inst.startDate.date, FHIRDate('2015-04-05').date)
        self.assertEqual(inst.statusDate.value, FHIRDate("2016-02-14").value)
        self.assertEqual(inst.statusDate.as_json(), "2016-02-14")
        self.assertEqual(inst.statusDate.date, FHIRDate('2016-02-14').date)
        self.assertEqual(inst.statusReason.value, FHIRString("Patient wants to defer weight loss until after honeymoon.").value)
        self.assertEqual(inst.statusReason.as_json(), "Patient wants to defer weight loss until after honeymoon.")
        self.assertEqual(inst.target[0].detailRange.high.code.value, FHIRCode("[lb_av]").value)
        self.assertEqual(inst.target[0].detailRange.high.code.as_json(), "[lb_av]")
        self.assertEqual(inst.target[0].detailRange.high.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.target[0].detailRange.high.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.target[0].detailRange.high.unit.value, FHIRString("lbs").value)
        self.assertEqual(inst.target[0].detailRange.high.unit.as_json(), "lbs")
        self.assertEqual(inst.target[0].detailRange.high.value, 180)
        self.assertEqual(inst.target[0].detailRange.low.code.value, FHIRCode("[lb_av]").value)
        self.assertEqual(inst.target[0].detailRange.low.code.as_json(), "[lb_av]")
        self.assertEqual(inst.target[0].detailRange.low.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.target[0].detailRange.low.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.target[0].detailRange.low.unit.value, FHIRString("lbs").value)
        self.assertEqual(inst.target[0].detailRange.low.unit.as_json(), "lbs")
        self.assertEqual(inst.target[0].detailRange.low.value, 160)
        self.assertEqual(inst.target[0].dueDate.value, FHIRDate("2016-04-05").value)
        self.assertEqual(inst.target[0].dueDate.as_json(), "2016-04-05")
        self.assertEqual(inst.target[0].dueDate.date, FHIRDate('2016-04-05').date)
        self.assertEqual(inst.target[0].measure.coding[0].code.value, FHIRCode("3141-9").value)
        self.assertEqual(inst.target[0].measure.coding[0].code.as_json(), "3141-9")
        self.assertEqual(inst.target[0].measure.coding[0].display.value, FHIRString("Weight Measured").value)
        self.assertEqual(inst.target[0].measure.coding[0].display.as_json(), "Weight Measured")
        self.assertEqual(inst.target[0].measure.coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.target[0].measure.coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.text.status.value, FHIRCode("additional").value)
        self.assertEqual(inst.text.status.as_json(), "additional")

    def testGoal2(self):
        inst = self.instantiate_from('goal-example-stop-smoking.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Goal instance')
        self.implGoal2(inst)

        js = inst.as_json()
        self.assertEqual("Goal", js["resourceType"])
        inst2 = goal.Goal(js)
        self.implGoal2(inst2)

    def implGoal2(self, inst):
        self.assertEqual(inst.achievementStatus.coding[0].code.value, FHIRCode("achieved").value)
        self.assertEqual(inst.achievementStatus.coding[0].code.as_json(), "achieved")
        self.assertEqual(inst.achievementStatus.coding[0].display.value, FHIRString("Achieved").value)
        self.assertEqual(inst.achievementStatus.coding[0].display.as_json(), "Achieved")
        self.assertEqual(inst.achievementStatus.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/goal-achievement").value)
        self.assertEqual(inst.achievementStatus.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/goal-achievement")
        self.assertEqual(inst.achievementStatus.text.value, FHIRString("Achieved").value)
        self.assertEqual(inst.achievementStatus.text.as_json(), "Achieved")
        self.assertEqual(inst.description.text.value, FHIRString("Stop smoking").value)
        self.assertEqual(inst.description.text.as_json(), "Stop smoking")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("123").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "123")
        self.assertEqual(inst.lifecycleStatus.value, FHIRCode("completed").value)
        self.assertEqual(inst.lifecycleStatus.as_json(), "completed")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcomeCode[0].coding[0].code.value, FHIRCode("8517006").value)
        self.assertEqual(inst.outcomeCode[0].coding[0].code.as_json(), "8517006")
        self.assertEqual(inst.outcomeCode[0].coding[0].display.value, FHIRString("Ex-smoker (finding)").value)
        self.assertEqual(inst.outcomeCode[0].coding[0].display.as_json(), "Ex-smoker (finding)")
        self.assertEqual(inst.outcomeCode[0].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.outcomeCode[0].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.outcomeCode[0].text.value, FHIRString("Former smoker").value)
        self.assertEqual(inst.outcomeCode[0].text.as_json(), "Former smoker")
        self.assertEqual(inst.startDate.value, FHIRDate("2015-04-05").value)
        self.assertEqual(inst.startDate.as_json(), "2015-04-05")
        self.assertEqual(inst.startDate.date, FHIRDate('2015-04-05').date)
        self.assertEqual(inst.text.status.value, FHIRCode("additional").value)
        self.assertEqual(inst.text.status.as_json(), "additional")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRString, FHIRDate