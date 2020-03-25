#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import allergyintolerance

class AllergyIntoleranceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AllergyIntolerance", js["resourceType"])
        return allergyintolerance.AllergyIntolerance(js)

    def testAllergyIntolerance1(self):
        inst = self.instantiate_from('allergyintolerance-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a AllergyIntolerance instance')
        self.implAllergyIntolerance1(inst)

        js = inst.as_json()
        self.assertEqual("AllergyIntolerance", js["resourceType"])
        inst2 = allergyintolerance.AllergyIntolerance(js)
        self.implAllergyIntolerance1(inst2)

    def implAllergyIntolerance1(self, inst):
        self.assertEqual(inst.category[0].value, FHIRCode('food').value)
        self.assertEqual(inst.category[0].as_json(), 'food')
        self.assertEqual(inst.clinicalStatus.coding[0].code.value, FHIRCode('active').value)
        self.assertEqual(inst.clinicalStatus.coding[0].code.as_json(), 'active')
        self.assertEqual(inst.clinicalStatus.coding[0].display.value, FHIRString('Active').value)
        self.assertEqual(inst.clinicalStatus.coding[0].display.as_json(), 'Active')
        self.assertEqual(inst.clinicalStatus.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical').value)
        self.assertEqual(inst.clinicalStatus.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('227493005').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '227493005')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Cashew nuts').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Cashew nuts')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.criticality.value, FHIRCode('high').value)
        self.assertEqual(inst.criticality.as_json(), 'high')
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://acme.com/ids/patients/risks').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://acme.com/ids/patients/risks')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('49476534').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '49476534')
        self.assertEqual(inst.lastOccurrence.value, FHIRDateTime('2012-06').value)
        self.assertEqual(inst.lastOccurrence.as_json(), '2012-06')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown('The criticality is high becasue of the observed anaphylactic reaction when challenged with cashew extract.').value)
        self.assertEqual(inst.note[0].text.as_json(), 'The criticality is high becasue of the observed anaphylactic reaction when challenged with cashew extract.')
        self.assertEqual(inst.onsetDateTime.value, FHIRDateTime('2004').value)
        self.assertEqual(inst.onsetDateTime.as_json(), '2004')
        self.assertEqual(inst.reaction[0].description.value, FHIRString('Challenge Protocol. Severe reaction to subcutaneous cashew extract. Epinephrine administered').value)
        self.assertEqual(inst.reaction[0].description.as_json(), 'Challenge Protocol. Severe reaction to subcutaneous cashew extract. Epinephrine administered')
        self.assertEqual(inst.reaction[0].exposureRoute.coding[0].code.value, FHIRCode('34206005').value)
        self.assertEqual(inst.reaction[0].exposureRoute.coding[0].code.as_json(), '34206005')
        self.assertEqual(inst.reaction[0].exposureRoute.coding[0].display.value, FHIRString('Subcutaneous route').value)
        self.assertEqual(inst.reaction[0].exposureRoute.coding[0].display.as_json(), 'Subcutaneous route')
        self.assertEqual(inst.reaction[0].exposureRoute.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.reaction[0].exposureRoute.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.reaction[0].manifestation[0].coding[0].code.value, FHIRCode('39579001').value)
        self.assertEqual(inst.reaction[0].manifestation[0].coding[0].code.as_json(), '39579001')
        self.assertEqual(inst.reaction[0].manifestation[0].coding[0].display.value, FHIRString('Anaphylactic reaction').value)
        self.assertEqual(inst.reaction[0].manifestation[0].coding[0].display.as_json(), 'Anaphylactic reaction')
        self.assertEqual(inst.reaction[0].manifestation[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.reaction[0].manifestation[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.reaction[0].onset.value, FHIRDateTime('2012-06-12').value)
        self.assertEqual(inst.reaction[0].onset.as_json(), '2012-06-12')
        self.assertEqual(inst.reaction[0].severity.value, FHIRCode('severe').value)
        self.assertEqual(inst.reaction[0].severity.as_json(), 'severe')
        self.assertEqual(inst.reaction[0].substance.coding[0].code.value, FHIRCode('1160593').value)
        self.assertEqual(inst.reaction[0].substance.coding[0].code.as_json(), '1160593')
        self.assertEqual(inst.reaction[0].substance.coding[0].display.value, FHIRString('cashew nut allergenic extract Injectable Product').value)
        self.assertEqual(inst.reaction[0].substance.coding[0].display.as_json(), 'cashew nut allergenic extract Injectable Product')
        self.assertEqual(inst.reaction[0].substance.coding[0].system.value, FHIRUri('http://www.nlm.nih.gov/research/umls/rxnorm').value)
        self.assertEqual(inst.reaction[0].substance.coding[0].system.as_json(), 'http://www.nlm.nih.gov/research/umls/rxnorm')
        self.assertEqual(inst.reaction[1].manifestation[0].coding[0].code.value, FHIRCode('64305001').value)
        self.assertEqual(inst.reaction[1].manifestation[0].coding[0].code.as_json(), '64305001')
        self.assertEqual(inst.reaction[1].manifestation[0].coding[0].display.value, FHIRString('Urticaria').value)
        self.assertEqual(inst.reaction[1].manifestation[0].coding[0].display.as_json(), 'Urticaria')
        self.assertEqual(inst.reaction[1].manifestation[0].coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.reaction[1].manifestation[0].coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.reaction[1].note[0].text.value, FHIRMarkdown('The patient reports that the onset of urticaria was within 15 minutes of eating cashews.').value)
        self.assertEqual(inst.reaction[1].note[0].text.as_json(), 'The patient reports that the onset of urticaria was within 15 minutes of eating cashews.')
        self.assertEqual(inst.reaction[1].onset.value, FHIRDateTime('2004').value)
        self.assertEqual(inst.reaction[1].onset.as_json(), '2004')
        self.assertEqual(inst.reaction[1].severity.value, FHIRCode('moderate').value)
        self.assertEqual(inst.reaction[1].severity.as_json(), 'moderate')
        self.assertEqual(inst.recordedDate.value, FHIRDateTime('2014-10-09T14:58:00+11:00').value)
        self.assertEqual(inst.recordedDate.as_json(), '2014-10-09T14:58:00+11:00')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.type.value, FHIRCode('allergy').value)
        self.assertEqual(inst.type.as_json(), 'allergy')
        self.assertEqual(inst.verificationStatus.coding[0].code.value, FHIRCode('confirmed').value)
        self.assertEqual(inst.verificationStatus.coding[0].code.as_json(), 'confirmed')
        self.assertEqual(inst.verificationStatus.coding[0].display.value, FHIRString('Confirmed').value)
        self.assertEqual(inst.verificationStatus.coding[0].display.as_json(), 'Confirmed')
        self.assertEqual(inst.verificationStatus.coding[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/allergyintolerance-verification').value)
        self.assertEqual(inst.verificationStatus.coding[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/allergyintolerance-verification')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime, FHIRMarkdown