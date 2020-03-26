#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import bodystructure

class BodyStructureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("BodyStructure", js["resourceType"])
        return bodystructure.BodyStructure(js)

    def testBodyStructure1(self):
        inst = self.instantiate_from('bodystructure-example-tumor.json')
        self.assertIsNotNone(inst, 'Must have instantiated a BodyStructure instance')
        self.implBodyStructure1(inst)

        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure1(inst2)

    def implBodyStructure1(self, inst):
        self.assertEqual(inst.description.value, FHIRString("7 cm maximum diameter").value)
        self.assertEqual(inst.description.as_json(), "7 cm maximum diameter")
        self.assertEqual(inst.id.value, FHIRString("tumor").value)
        self.assertEqual(inst.id.as_json(), "tumor")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://goodhealth.org/bodystructure/identifiers").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.image[0].contentType.value, FHIRCode("application/dicom").value)
        self.assertEqual(inst.image[0].contentType.as_json(), "application/dicom")
        self.assertEqual(inst.image[0].url.value, FHIRUrl("http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details").value)
        self.assertEqual(inst.image[0].url.as_json(), "http://imaging.acme.com/wado/server?requestType=WADO&amp;wado_details")
        self.assertEqual(inst.location.coding[0].code.value, FHIRCode("78961009").value)
        self.assertEqual(inst.location.coding[0].code.as_json(), "78961009")
        self.assertEqual(inst.location.coding[0].display.value, FHIRString("Splenic structure (body structure)").value)
        self.assertEqual(inst.location.coding[0].display.as_json(), "Splenic structure (body structure)")
        self.assertEqual(inst.location.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.location.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.location.text.value, FHIRString("Spleen").value)
        self.assertEqual(inst.location.text.as_json(), "Spleen")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.morphology.coding[0].code.value, FHIRCode("4147007").value)
        self.assertEqual(inst.morphology.coding[0].code.as_json(), "4147007")
        self.assertEqual(inst.morphology.coding[0].display.value, FHIRString("Mass (morphologic abnormality)").value)
        self.assertEqual(inst.morphology.coding[0].display.as_json(), "Mass (morphologic abnormality)")
        self.assertEqual(inst.morphology.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.morphology.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.morphology.text.value, FHIRString("Splenic mass").value)
        self.assertEqual(inst.morphology.text.as_json(), "Splenic mass")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testBodyStructure2(self):
        inst = self.instantiate_from('bodystructure-example-fetus.json')
        self.assertIsNotNone(inst, 'Must have instantiated a BodyStructure instance')
        self.implBodyStructure2(inst)

        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure2(inst2)

    def implBodyStructure2(self, inst):
        self.assertEqual(inst.description.value, FHIRString("EDD 1/1/2017 confirmation by LMP").value)
        self.assertEqual(inst.description.as_json(), "EDD 1/1/2017 confirmation by LMP")
        self.assertEqual(inst.id.value, FHIRString("fetus").value)
        self.assertEqual(inst.id.as_json(), "fetus")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://goodhealth.org/bodystructure/identifiers").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.location.coding[0].code.value, FHIRCode("83418008").value)
        self.assertEqual(inst.location.coding[0].code.as_json(), "83418008")
        self.assertEqual(inst.location.coding[0].display.value, FHIRString("Entire fetus (body structure)").value)
        self.assertEqual(inst.location.coding[0].display.as_json(), "Entire fetus (body structure)")
        self.assertEqual(inst.location.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.location.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.location.text.value, FHIRString("Fetus").value)
        self.assertEqual(inst.location.text.as_json(), "Fetus")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testBodyStructure3(self):
        inst = self.instantiate_from('bodystructure-example-skin-patch.json')
        self.assertIsNotNone(inst, 'Must have instantiated a BodyStructure instance')
        self.implBodyStructure3(inst)

        js = inst.as_json()
        self.assertEqual("BodyStructure", js["resourceType"])
        inst2 = bodystructure.BodyStructure(js)
        self.implBodyStructure3(inst2)

    def implBodyStructure3(self, inst):
        self.assertFalse(inst.active)
        self.assertEqual(inst.description.value, FHIRString("inner surface (volar) of the left forearm").value)
        self.assertEqual(inst.description.as_json(), "inner surface (volar) of the left forearm")
        self.assertEqual(inst.id.value, FHIRString("skin-patch").value)
        self.assertEqual(inst.id.as_json(), "skin-patch")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://goodhealth.org/bodystructure/identifiers").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://goodhealth.org/bodystructure/identifiers")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.location.coding[0].code.value, FHIRCode("14975008").value)
        self.assertEqual(inst.location.coding[0].code.as_json(), "14975008")
        self.assertEqual(inst.location.coding[0].display.value, FHIRString("Forearm").value)
        self.assertEqual(inst.location.coding[0].display.as_json(), "Forearm")
        self.assertEqual(inst.location.coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.location.coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.location.text.value, FHIRString("Forearm").value)
        self.assertEqual(inst.location.text.as_json(), "Forearm")
        self.assertEqual(inst.locationQualifier[0].coding[0].code.value, FHIRCode("419161000").value)
        self.assertEqual(inst.locationQualifier[0].coding[0].code.as_json(), "419161000")
        self.assertEqual(inst.locationQualifier[0].coding[0].display.value, FHIRString("Unilateral left").value)
        self.assertEqual(inst.locationQualifier[0].coding[0].display.as_json(), "Unilateral left")
        self.assertEqual(inst.locationQualifier[0].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.locationQualifier[0].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.locationQualifier[0].text.value, FHIRString("Left").value)
        self.assertEqual(inst.locationQualifier[0].text.as_json(), "Left")
        self.assertEqual(inst.locationQualifier[1].coding[0].code.value, FHIRCode("263929005").value)
        self.assertEqual(inst.locationQualifier[1].coding[0].code.as_json(), "263929005")
        self.assertEqual(inst.locationQualifier[1].coding[0].display.value, FHIRString("Volar").value)
        self.assertEqual(inst.locationQualifier[1].coding[0].display.as_json(), "Volar")
        self.assertEqual(inst.locationQualifier[1].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.locationQualifier[1].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.locationQualifier[1].text.value, FHIRString("Volar").value)
        self.assertEqual(inst.locationQualifier[1].text.as_json(), "Volar")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.morphology.text.value, FHIRString("Skin patch").value)
        self.assertEqual(inst.morphology.text.as_json(), "Skin patch")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRUri, FHIRCode, FHIRUrl