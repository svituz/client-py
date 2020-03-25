#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import chargeitemdefinition

class ChargeItemDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ChargeItemDefinition", js["resourceType"])
        return chargeitemdefinition.ChargeItemDefinition(js)

    def testChargeItemDefinition1(self):
        inst = self.instantiate_from('chargeitemdefinition-device-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ChargeItemDefinition instance')
        self.implChargeItemDefinition1(inst)

        js = inst.as_json()
        self.assertEqual("ChargeItemDefinition", js["resourceType"])
        inst2 = chargeitemdefinition.ChargeItemDefinition(js)
        self.implChargeItemDefinition1(inst2)

    def implChargeItemDefinition1(self, inst):
        self.assertEqual(inst.applicability[0].description.value, FHIRString('Verify ChargeItem pertains to Device 12345').value)
        self.assertEqual(inst.applicability[0].description.as_json(), 'Verify ChargeItem pertains to Device 12345')
        self.assertEqual(inst.applicability[0].expression.value, FHIRString('%context.service.suppliedItem=\'Device/12345\'').value)
        self.assertEqual(inst.applicability[0].expression.as_json(), '%context.service.suppliedItem=\'Device/12345\'')
        self.assertEqual(inst.applicability[0].language.value, FHIRString('text/fhirpath').value)
        self.assertEqual(inst.applicability[0].language.as_json(), 'text/fhirpath')
        self.assertEqual(inst.description.value, FHIRMarkdown('Financial details for  custom made device').value)
        self.assertEqual(inst.description.as_json(), 'Financial details for  custom made device')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.currency.value, FHIRCode('EUR').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.currency.as_json(), 'EUR')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.value, 67.44)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].code.value, FHIRCode('VK').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].code.as_json(), 'VK')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].display.value, FHIRString('Verkaufspreis (netto)').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].display.as_json(), 'Verkaufspreis (netto)')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].system.value, FHIRUri('http://fhir.de/CodeSystem/billing-attributes').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].system.as_json(), 'http://fhir.de/CodeSystem/billing-attributes')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].type.value, FHIRCode('base').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].type.as_json(), 'base')
        self.assertEqual(inst.propertyGroup[1].applicability[0].description.value, FHIRString('Gültigkeit Steuersatz').value)
        self.assertEqual(inst.propertyGroup[1].applicability[0].description.as_json(), 'Gültigkeit Steuersatz')
        self.assertEqual(inst.propertyGroup[1].applicability[0].expression.value, FHIRString('%context.occurenceDateTime > \'2018-04-01\'').value)
        self.assertEqual(inst.propertyGroup[1].applicability[0].expression.as_json(), '%context.occurenceDateTime > \'2018-04-01\'')
        self.assertEqual(inst.propertyGroup[1].applicability[0].language.value, FHIRString('text/fhirpath').value)
        self.assertEqual(inst.propertyGroup[1].applicability[0].language.as_json(), 'text/fhirpath')
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].code.value, FHIRCode('MWST').value)
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].code.as_json(), 'MWST')
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].display.value, FHIRString('Mehrwersteuersatz').value)
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].display.as_json(), 'Mehrwersteuersatz')
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].system.value, FHIRUri('http://fhir.de/CodeSystem/billing-attributes').value)
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].code.coding[0].system.as_json(), 'http://fhir.de/CodeSystem/billing-attributes')
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].factor, 1.19)
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].type.value, FHIRCode('tax').value)
        self.assertEqual(inst.propertyGroup[1].priceComponent[0].type.as_json(), 'tax')
        self.assertEqual(inst.propertyGroup[2].applicability[0].description.value, FHIRString('Gültigkeit Steuersatz').value)
        self.assertEqual(inst.propertyGroup[2].applicability[0].description.as_json(), 'Gültigkeit Steuersatz')
        self.assertEqual(inst.propertyGroup[2].applicability[0].expression.value, FHIRString('%context.occurenceDateTime <= \'2018-04-01\'').value)
        self.assertEqual(inst.propertyGroup[2].applicability[0].expression.as_json(), '%context.occurenceDateTime <= \'2018-04-01\'')
        self.assertEqual(inst.propertyGroup[2].applicability[0].language.value, FHIRString('text/fhirpath').value)
        self.assertEqual(inst.propertyGroup[2].applicability[0].language.as_json(), 'text/fhirpath')
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].code.value, FHIRCode('MWST').value)
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].code.as_json(), 'MWST')
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].display.value, FHIRString('Mehrwersteuersatz').value)
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].display.as_json(), 'Mehrwersteuersatz')
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].system.value, FHIRUri('http://fhir.de/CodeSystem/billing-attributes').value)
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].code.coding[0].system.as_json(), 'http://fhir.de/CodeSystem/billing-attributes')
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].factor, 1.07)
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].type.value, FHIRCode('tax').value)
        self.assertEqual(inst.propertyGroup[2].priceComponent[0].type.as_json(), 'tax')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.url.value, FHIRUri('http://sap.org/ChargeItemDefinition/device-123').value)
        self.assertEqual(inst.url.as_json(), 'http://sap.org/ChargeItemDefinition/device-123')

    def testChargeItemDefinition2(self):
        inst = self.instantiate_from('chargeitemdefinition-ebm-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ChargeItemDefinition instance')
        self.implChargeItemDefinition2(inst)

        js = inst.as_json()
        self.assertEqual("ChargeItemDefinition", js["resourceType"])
        inst2 = chargeitemdefinition.ChargeItemDefinition(js)
        self.implChargeItemDefinition2(inst2)

    def implChargeItemDefinition2(self, inst):
        self.assertEqual(inst.applicability[0].description.value, FHIRString('Excludes billing code 13250 for same Encounter').value)
        self.assertEqual(inst.applicability[0].description.as_json(), 'Excludes billing code 13250 for same Encounter')
        self.assertEqual(inst.applicability[0].expression.value, FHIRString('[some CQL expression]').value)
        self.assertEqual(inst.applicability[0].expression.as_json(), '[some CQL expression]')
        self.assertEqual(inst.applicability[0].language.value, FHIRString('text/cql').value)
        self.assertEqual(inst.applicability[0].language.as_json(), 'text/cql')
        self.assertEqual(inst.applicability[1].description.value, FHIRString('Applies only once per Encounter').value)
        self.assertEqual(inst.applicability[1].description.as_json(), 'Applies only once per Encounter')
        self.assertEqual(inst.applicability[1].expression.value, FHIRString('[some CQL expression]').value)
        self.assertEqual(inst.applicability[1].expression.as_json(), '[some CQL expression]')
        self.assertEqual(inst.applicability[1].language.value, FHIRString('text/CQL').value)
        self.assertEqual(inst.applicability[1].language.as_json(), 'text/CQL')
        self.assertEqual(inst.code.coding[0].code.value, FHIRCode('30110').value)
        self.assertEqual(inst.code.coding[0].code.as_json(), '30110')
        self.assertEqual(inst.code.coding[0].display.value, FHIRString('Allergologiediagnostik I').value)
        self.assertEqual(inst.code.coding[0].display.as_json(), 'Allergologiediagnostik I')
        self.assertEqual(inst.code.coding[0].system.value, FHIRUri('http://fhir.de/CodingSystem/kbv/ebm').value)
        self.assertEqual(inst.code.coding[0].system.as_json(), 'http://fhir.de/CodingSystem/kbv/ebm')
        self.assertEqual(inst.description.value, FHIRMarkdown('Allergologisch-diagnostischer Komplex zur Diagnostik und/oder zum Ausschluss einer (Kontakt-)Allergie vom Spättyp (Typ IV), einschl. Kosten').value)
        self.assertEqual(inst.description.as_json(), 'Allergologisch-diagnostischer Komplex zur Diagnostik und/oder zum Ausschluss einer (Kontakt-)Allergie vom Spättyp (Typ IV), einschl. Kosten')
        self.assertEqual(inst.effectivePeriod.end.value, FHIRDateTime('2018-06-30').value)
        self.assertEqual(inst.effectivePeriod.end.as_json(), '2018-06-30')
        self.assertEqual(inst.effectivePeriod.start.value, FHIRDateTime('2018-04-01').value)
        self.assertEqual(inst.effectivePeriod.start.as_json(), '2018-04-01')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.currency.value, FHIRCode('EUR').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.currency.as_json(), 'EUR')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].amount.value, 67.44)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].code.value, FHIRCode('gesamt-euro').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].code.as_json(), 'gesamt-euro')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].display.value, FHIRString('Gesamt (Euro)').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].display.as_json(), 'Gesamt (Euro)')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].system.value, FHIRUri('http://fhir.de/CodeSystem/kbv/ebm-attribute').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].code.coding[0].system.as_json(), 'http://fhir.de/CodeSystem/kbv/ebm-attribute')
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].type.value, FHIRCode('base').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[0].type.as_json(), 'base')
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].code.value, FHIRCode('gesamt-punkte').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].code.as_json(), 'gesamt-punkte')
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].display.value, FHIRString('Gesamt (Punkte)').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].display.as_json(), 'Gesamt (Punkte)')
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].system.value, FHIRUri('http://fhir.de/CodeSystem/kbv/ebm-attribute').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].code.coding[0].system.as_json(), 'http://fhir.de/CodeSystem/kbv/ebm-attribute')
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].factor, 633)
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].type.value, FHIRCode('informational').value)
        self.assertEqual(inst.propertyGroup[0].priceComponent[1].type.as_json(), 'informational')
        self.assertEqual(inst.status.value, FHIRCode('active').value)
        self.assertEqual(inst.status.as_json(), 'active')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.url.value, FHIRUri('http://fhir.de/ChargeItemDefinition/kbv/ebm-30110').value)
        self.assertEqual(inst.url.as_json(), 'http://fhir.de/ChargeItemDefinition/kbv/ebm-30110')
        self.assertEqual(inst.version.value, FHIRString('2-2018').value)
        self.assertEqual(inst.version.as_json(), '2-2018')


from fhirclient.models.fhirdatatypes import FHIRString, FHIRMarkdown, FHIRCode, FHIRUri, FHIRDateTime