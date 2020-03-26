#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproduct

class MedicinalProductTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProduct", js["resourceType"])
        return medicinalproduct.MedicinalProduct(js)

    def testMedicinalProduct1(self):
        inst = self.instantiate_from('medicinalproduct-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProduct instance')
        self.implMedicinalProduct1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProduct", js["resourceType"])
        inst2 = medicinalproduct.MedicinalProduct(js)
        self.implMedicinalProduct1(inst2)

    def implMedicinalProduct1(self, inst):
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://ema.europa.eu/example/MPID").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://ema.europa.eu/example/MPID")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("{mpid}").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "{mpid}")
        self.assertEqual(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.system.value, FHIRUri("http://ema.europa.eu/example/manufacturingAuthorisationReferenceNumber").value)
        self.assertEqual(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.system.as_json(), "http://ema.europa.eu/example/manufacturingAuthorisationReferenceNumber")
        self.assertEqual(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.value.value, FHIRString("1324TZ").value)
        self.assertEqual(inst.manufacturingBusinessOperation[0].authorisationReferenceNumber.value.as_json(), "1324TZ")
        self.assertEqual(inst.manufacturingBusinessOperation[0].effectiveDate.value, FHIRDateTime("2013-03-15").value)
        self.assertEqual(inst.manufacturingBusinessOperation[0].effectiveDate.as_json(), "2013-03-15")
        self.assertEqual(inst.manufacturingBusinessOperation[0].operationType.coding[0].code.value, FHIRCode("Batchrelease").value)
        self.assertEqual(inst.manufacturingBusinessOperation[0].operationType.coding[0].code.as_json(), "Batchrelease")
        self.assertEqual(inst.manufacturingBusinessOperation[0].operationType.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/manufacturingOperationType").value)
        self.assertEqual(inst.manufacturingBusinessOperation[0].operationType.coding[0].system.as_json(), "http://ema.europa.eu/example/manufacturingOperationType")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].code.value, FHIRCode("EU").value)
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].code.as_json(), "EU")
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/countryCode").value)
        self.assertEqual(inst.name[0].countryLanguage[0].country.coding[0].system.as_json(), "http://ema.europa.eu/example/countryCode")
        self.assertEqual(inst.name[0].countryLanguage[0].jurisdiction.coding[0].code.value, FHIRCode("EU").value)
        self.assertEqual(inst.name[0].countryLanguage[0].jurisdiction.coding[0].code.as_json(), "EU")
        self.assertEqual(inst.name[0].countryLanguage[0].jurisdiction.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/jurisdictionCode").value)
        self.assertEqual(inst.name[0].countryLanguage[0].jurisdiction.coding[0].system.as_json(), "http://ema.europa.eu/example/jurisdictionCode")
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].code.value, FHIRCode("EN").value)
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].code.as_json(), "EN")
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/languageCode").value)
        self.assertEqual(inst.name[0].countryLanguage[0].language.coding[0].system.as_json(), "http://ema.europa.eu/example/languageCode")
        self.assertEqual(inst.name[0].namePart[0].part.value, FHIRString("Equilidem").value)
        self.assertEqual(inst.name[0].namePart[0].part.as_json(), "Equilidem")
        self.assertEqual(inst.name[0].namePart[0].type.code.value, FHIRCode("INV").value)
        self.assertEqual(inst.name[0].namePart[0].type.code.as_json(), "INV")
        self.assertEqual(inst.name[0].namePart[1].part.value, FHIRString("2.5 mg").value)
        self.assertEqual(inst.name[0].namePart[1].part.as_json(), "2.5 mg")
        self.assertEqual(inst.name[0].namePart[1].type.code.value, FHIRCode("STR").value)
        self.assertEqual(inst.name[0].namePart[1].type.code.as_json(), "STR")
        self.assertEqual(inst.name[0].namePart[2].part.value, FHIRString("film-coated tablets").value)
        self.assertEqual(inst.name[0].namePart[2].part.as_json(), "film-coated tablets")
        self.assertEqual(inst.name[0].namePart[2].type.code.value, FHIRCode("FRM").value)
        self.assertEqual(inst.name[0].namePart[2].type.code.as_json(), "FRM")
        self.assertEqual(inst.name[0].productName.value, FHIRString("Equilidem 2.5 mg film-coated tablets").value)
        self.assertEqual(inst.name[0].productName.as_json(), "Equilidem 2.5 mg film-coated tablets")
        self.assertEqual(inst.productClassification[0].coding[0].code.value, FHIRCode("WHOAnatomicalTherapeuticChemicalATCClassificationSystem|B01AF02").value)
        self.assertEqual(inst.productClassification[0].coding[0].code.as_json(), "WHOAnatomicalTherapeuticChemicalATCClassificationSystem|B01AF02")
        self.assertEqual(inst.productClassification[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemicalATCClassificationSystem").value)
        self.assertEqual(inst.productClassification[0].coding[0].system.as_json(), "http://ema.europa.eu/example/WHOAnatomicalTherapeuticChemicalATCClassificationSystem")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRUri, FHIRDateTime, FHIRCode