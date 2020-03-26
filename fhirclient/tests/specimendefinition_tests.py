#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import specimendefinition

class SpecimenDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SpecimenDefinition", js["resourceType"])
        return specimendefinition.SpecimenDefinition(js)

    def testSpecimenDefinition1(self):
        inst = self.instantiate_from('specimendefinition-example-serum-plasma.json')
        self.assertIsNotNone(inst, 'Must have instantiated a SpecimenDefinition instance')
        self.implSpecimenDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("SpecimenDefinition", js["resourceType"])
        inst2 = specimendefinition.SpecimenDefinition(js)
        self.implSpecimenDefinition1(inst2)

    def implSpecimenDefinition1(self, inst):
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.patientPreparation[0].text.value, FHIRString("12 hour fasting").value)
        self.assertEqual(inst.patientPreparation[0].text.as_json(), "12 hour fasting")
        self.assertEqual(inst.patientPreparation[1].coding[0].code.value, FHIRCode("263678003").value)
        self.assertEqual(inst.patientPreparation[1].coding[0].code.as_json(), "263678003")
        self.assertEqual(inst.patientPreparation[1].coding[0].display.value, FHIRString("At rest").value)
        self.assertEqual(inst.patientPreparation[1].coding[0].display.as_json(), "At rest")
        self.assertEqual(inst.patientPreparation[1].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.patientPreparation[1].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.timeAspect.value, FHIRString("preferrably morning time").value)
        self.assertEqual(inst.timeAspect.as_json(), "preferrably morning time")
        self.assertEqual(inst.typeCollected.coding[0].code.value, FHIRCode("122555007").value)
        self.assertEqual(inst.typeCollected.coding[0].code.as_json(), "122555007")
        self.assertEqual(inst.typeCollected.coding[0].display.value, FHIRString("Venous blood specimen").value)
        self.assertEqual(inst.typeCollected.coding[0].display.as_json(), "Venous blood specimen")
        self.assertEqual(inst.typeCollected.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeCollected.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].code.value, FHIRCode("yellow").value)
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].code.as_json(), "yellow")
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].display.value, FHIRString("yellow cap").value)
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].display.as_json(), "yellow cap")
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].system.value, FHIRUri("urn:iso:std:iso:6710:2017").value)
        self.assertEqual(inst.typeTested[0].container.cap.coding[0].system.as_json(), "urn:iso:std:iso:6710:2017")
        self.assertEqual(inst.typeTested[0].container.material.coding[0].code.value, FHIRCode("61088005").value)
        self.assertEqual(inst.typeTested[0].container.material.coding[0].code.as_json(), "61088005")
        self.assertEqual(inst.typeTested[0].container.material.coding[0].display.value, FHIRString("plastic").value)
        self.assertEqual(inst.typeTested[0].container.material.coding[0].display.as_json(), "plastic")
        self.assertEqual(inst.typeTested[0].container.material.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeTested[0].container.material.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.code.value, FHIRCode("mL").value)
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.code.as_json(), "mL")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.unit.value, FHIRString("ml").value)
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.unit.as_json(), "ml")
        self.assertEqual(inst.typeTested[0].container.minimumVolumeQuantity.value, 2)
        self.assertEqual(inst.typeTested[0].container.type.coding[0].code.value, FHIRCode("702281005").value)
        self.assertEqual(inst.typeTested[0].container.type.coding[0].code.as_json(), "702281005")
        self.assertEqual(inst.typeTested[0].container.type.coding[0].display.value, FHIRString("Evacuated blood collection tube, thrombin/clot activator/gel separator").value)
        self.assertEqual(inst.typeTested[0].container.type.coding[0].display.as_json(), "Evacuated blood collection tube, thrombin/clot activator/gel separator")
        self.assertEqual(inst.typeTested[0].container.type.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeTested[0].container.type.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.code.value, FHIRCode("min").value)
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.code.as_json(), "min")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.unit.value, FHIRString("minute").value)
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.unit.as_json(), "minute")
        self.assertEqual(inst.typeTested[0].handling[0].maxDuration.value, 60)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureQualifier.text.value, FHIRString("Ambient temperature").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureQualifier.text.as_json(), "Ambient temperature")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.high.value, 25)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[0].handling[0].temperatureRange.low.value, 15)
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.code.value, FHIRCode("h").value)
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.code.as_json(), "h")
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.unit.value, FHIRString("hour").value)
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.unit.as_json(), "hour")
        self.assertEqual(inst.typeTested[0].handling[1].maxDuration.value, 8)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureQualifier.text.value, FHIRString("Refrigerated temperature").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureQualifier.text.as_json(), "Refrigerated temperature")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.high.value, 8)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[0].handling[1].temperatureRange.low.value, 2)
        self.assertEqual(inst.typeTested[0].preference.value, FHIRCode("preferred").value)
        self.assertEqual(inst.typeTested[0].preference.as_json(), "preferred")
        self.assertEqual(inst.typeTested[0].type.coding[0].code.value, FHIRCode("119364003").value)
        self.assertEqual(inst.typeTested[0].type.coding[0].code.as_json(), "119364003")
        self.assertEqual(inst.typeTested[0].type.coding[0].display.value, FHIRString("Serum specimen").value)
        self.assertEqual(inst.typeTested[0].type.coding[0].display.as_json(), "Serum specimen")
        self.assertEqual(inst.typeTested[0].type.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeTested[0].type.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].code.value, FHIRCode("green").value)
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].code.as_json(), "green")
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].display.value, FHIRString("green cap").value)
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].display.as_json(), "green cap")
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].system.value, FHIRUri("urn:iso:std:iso:6710:2017").value)
        self.assertEqual(inst.typeTested[1].container.cap.coding[0].system.as_json(), "urn:iso:std:iso:6710:2017")
        self.assertEqual(inst.typeTested[1].container.material.coding[0].code.value, FHIRCode("32039001").value)
        self.assertEqual(inst.typeTested[1].container.material.coding[0].code.as_json(), "32039001")
        self.assertEqual(inst.typeTested[1].container.material.coding[0].display.value, FHIRString("glass").value)
        self.assertEqual(inst.typeTested[1].container.material.coding[0].display.as_json(), "glass")
        self.assertEqual(inst.typeTested[1].container.material.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeTested[1].container.material.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.code.value, FHIRCode("mL").value)
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.code.as_json(), "mL")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.unit.value, FHIRString("ml").value)
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.unit.as_json(), "ml")
        self.assertEqual(inst.typeTested[1].container.minimumVolumeQuantity.value, 2)
        self.assertEqual(inst.typeTested[1].container.type.coding[0].code.value, FHIRCode("767390000").value)
        self.assertEqual(inst.typeTested[1].container.type.coding[0].code.as_json(), "767390000")
        self.assertEqual(inst.typeTested[1].container.type.coding[0].display.value, FHIRString("Evacuated blood collection tube with heparin lithium and gel separator").value)
        self.assertEqual(inst.typeTested[1].container.type.coding[0].display.as_json(), "Evacuated blood collection tube with heparin lithium and gel separator")
        self.assertEqual(inst.typeTested[1].container.type.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeTested[1].container.type.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.code.value, FHIRCode("min").value)
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.code.as_json(), "min")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.unit.value, FHIRString("minute").value)
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.unit.as_json(), "minute")
        self.assertEqual(inst.typeTested[1].handling[0].maxDuration.value, 60)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureQualifier.text.value, FHIRString("Ambient temperature").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureQualifier.text.as_json(), "Ambient temperature")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.high.value, 25)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[1].handling[0].temperatureRange.low.value, 15)
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.code.value, FHIRCode("h").value)
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.code.as_json(), "h")
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.unit.value, FHIRString("hour").value)
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.unit.as_json(), "hour")
        self.assertEqual(inst.typeTested[1].handling[1].maxDuration.value, 8)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureQualifier.text.value, FHIRString("Refrigerated temperature").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureQualifier.text.as_json(), "Refrigerated temperature")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.high.value, 8)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.code.value, FHIRCode("Cel").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.code.as_json(), "Cel")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.system.value, FHIRUri("http://unitsofmeasure.org").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.system.as_json(), "http://unitsofmeasure.org")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.unit.value, FHIRString("°C").value)
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.unit.as_json(), "°C")
        self.assertEqual(inst.typeTested[1].handling[1].temperatureRange.low.value, 2)
        self.assertEqual(inst.typeTested[1].preference.value, FHIRCode("alternate").value)
        self.assertEqual(inst.typeTested[1].preference.as_json(), "alternate")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].code.value, FHIRCode("insufficient").value)
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].code.as_json(), "insufficient")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].display.value, FHIRString("insufficient specimen volume").value)
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].display.as_json(), "insufficient specimen volume")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/rejection-criteria").value)
        self.assertEqual(inst.typeTested[1].rejectionCriterion[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/rejection-criteria")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].code.value, FHIRCode("hemolized").value)
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].code.as_json(), "hemolized")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].display.value, FHIRString("hemolized specimen").value)
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].display.as_json(), "hemolized specimen")
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/rejection-criteria").value)
        self.assertEqual(inst.typeTested[1].rejectionCriterion[1].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/rejection-criteria")
        self.assertEqual(inst.typeTested[1].type.coding[0].code.value, FHIRCode("119361006").value)
        self.assertEqual(inst.typeTested[1].type.coding[0].code.as_json(), "119361006")
        self.assertEqual(inst.typeTested[1].type.coding[0].display.value, FHIRString("Plasma specimen").value)
        self.assertEqual(inst.typeTested[1].type.coding[0].display.as_json(), "Plasma specimen")
        self.assertEqual(inst.typeTested[1].type.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.typeTested[1].type.coding[0].system.as_json(), "http://snomed.info/sct")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri