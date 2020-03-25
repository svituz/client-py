#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import chargeitem

class ChargeItemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItem", js["resourceType"])
        return chargeitem.ChargeItem(js)

    def testChargeItem1(self):
        inst = self.instantiate_from('chargeitem-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ChargeItem instance')
        self.implChargeItem1(inst)

        js = inst.as_json()
        self.assertEqual("ChargeItem", js["resourceType"])
        inst2 = chargeitem.ChargeItem(js)
        self.implChargeItem1(inst2)

    def implChargeItem1(self, inst):
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('01510').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '01510')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Zusatzpauschale für Beobachtung nach diagnostischer Koronarangiografie').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Zusatzpauschale für Beobachtung nach diagnostischer Koronarangiografie')
        self.assertEqual(inst.definitionUri[0].value, FHIRUri('http://www.kbv.de/tools/ebm/html/01520_2904360860826220813632.html').value)
        self.assertEqual(inst.definitionUri[0].as_json(), 'http://www.kbv.de/tools/ebm/html/01520_2904360860826220813632.html')
        self.assertEqual(inst.enteredDate.value, FHIRDateTime('2017-01-25T23:55:04+01:00').value)
        self.assertEqual(inst.enteredDate.as_json(), '2017-01-25T23:55:04+01:00')
        self.assertEqual(inst.factorOverride, 0.8)
        self.assertEqual(inst.identifier[0].system.value, FHIRUri('http://myHospital.org/ChargeItems').value)
        self.assertEqual(inst.identifier[0].system.as_json(), 'http://myHospital.org/ChargeItems')
        self.assertEqual(inst.identifier[0].value.value, FHIRString('654321').value)
        self.assertEqual(inst.identifier[0].value.as_json(), '654321')
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode('HTEST').value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), 'HTEST')
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString('test health data').value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), 'test health data')
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri('http://terminology.hl7.org/CodeSystem/v3-ActReason').value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), 'http://terminology.hl7.org/CodeSystem/v3-ActReason')
        self.assertEqual(inst.note[0].text.value, FHIRMarkdown('The code is only applicable for periods longer than 4h').value)
        self.assertEqual(inst.note[0].text.as_json(), 'The code is only applicable for periods longer than 4h')
        self.assertEqual(inst.note[0].time.value, FHIRDateTime('2017-01-25T23:55:04+01:00').value)
        self.assertEqual(inst.note[0].time.as_json(), '2017-01-25T23:55:04+01:00')
        self.assertEqual(inst.occurrencePeriod.end.value, FHIRDateTime('2017-01-25T12:35:00+01:00').value)
        self.assertEqual(inst.occurrencePeriod.end.as_json(), '2017-01-25T12:35:00+01:00')
        self.assertEqual(inst.occurrencePeriod.start.value, FHIRDateTime('2017-01-25T08:00:00+01:00').value)
        self.assertEqual(inst.occurrencePeriod.start.as_json(), '2017-01-25T08:00:00+01:00')
        self.assertEqual(inst.overrideReason.value, FHIRString('Patient is Cardiologist\'s golf buddy, so he gets a 20% discount!').value)
        self.assertEqual(inst.overrideReason.as_json(), 'Patient is Cardiologist\'s golf buddy, so he gets a 20% discount!')
        self.assertEqual(inst.performer[0].function.coding[0].code.value, FHIRCode('17561000').value)
        self.assertEqual(inst.performer[0].function.coding[0].code.as_json(), '17561000')
        self.assertEqual(inst.performer[0].function.coding[0].display.value, FHIRString('Cardiologist').value)
        self.assertEqual(inst.performer[0].function.coding[0].display.as_json(), 'Cardiologist')
        self.assertEqual(inst.performer[0].function.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.performer[0].function.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.performer[1].function.coding[0].code.value, FHIRCode('224542009').value)
        self.assertEqual(inst.performer[1].function.coding[0].code.as_json(), '224542009')
        self.assertEqual(inst.performer[1].function.coding[0].display.value, FHIRString('Coronary Care Nurse').value)
        self.assertEqual(inst.performer[1].function.coding[0].display.as_json(), 'Coronary Care Nurse')
        self.assertEqual(inst.performer[1].function.coding[0].system.value, FHIRUri('http://snomed.info/sct').value)
        self.assertEqual(inst.performer[1].function.coding[0].system.as_json(), 'http://snomed.info/sct')
        self.assertEqual(inst.priceOverride.currency.value, FHIRCode('EUR').value)
        self.assertEqual(inst.priceOverride.currency.as_json(), 'EUR')
        self.assertEqual(inst.priceOverride.value, 40)
        self.assertEqual(inst.quantity.value, 1)
        self.assertEqual(inst.reason[0].coding[0].code.value, FHIRCode('123456').value)
        self.assertEqual(inst.reason[0].coding[0].code.as_json(), '123456')
        self.assertEqual(inst.reason[0].coding[0].display.value, FHIRString('DIAG-1').value)
        self.assertEqual(inst.reason[0].coding[0].display.as_json(), 'DIAG-1')
        self.assertEqual(inst.reason[0].coding[0].system.value, FHIRUri('http://hl7.org/fhir/sid/icd-10').value)
        self.assertEqual(inst.reason[0].coding[0].system.as_json(), 'http://hl7.org/fhir/sid/icd-10')
        self.assertEqual(inst.status.value, FHIRCode('billable').value)
        self.assertEqual(inst.status.as_json(), 'billable')
        self.assertEqual(inst.text.div.value, FHIRString('<div xmlns="http://www.w3.org/1999/xhtml">Example of ChargeItem Usage in Context of the German EBM Billing code system</div>').value)
        self.assertEqual(inst.text.div.as_json(), '<div xmlns="http://www.w3.org/1999/xhtml">Example of ChargeItem Usage in Context of the German EBM Billing code system</div>')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime, FHIRMarkdown