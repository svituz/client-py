#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductpackaged

class MedicinalProductPackagedTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductPackaged", js["resourceType"])
        return medicinalproductpackaged.MedicinalProductPackaged(js)

    def testMedicinalProductPackaged1(self):
        inst = self.instantiate_from('medicinalproductpackaged-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductPackaged instance')
        self.implMedicinalProductPackaged1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductPackaged", js["resourceType"])
        inst2 = medicinalproductpackaged.MedicinalProductPackaged(js)
        self.implMedicinalProductPackaged1(inst2)

    def implMedicinalProductPackaged1(self, inst):
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.value, FHIRDateTime("2016-06-06").value)
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.period.end.as_json(), "2016-06-06")
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.system.value, FHIRUri("http://ema.europa.eu/example/baid1").value)
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.system.as_json(), "http://ema.europa.eu/example/baid1")
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.value.value, FHIRString("AAF5699").value)
        self.assertEqual(inst.batchIdentifier[0].outerPackaging.value.as_json(), "AAF5699")
        self.assertEqual(inst.description.value, FHIRString("ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS. ").value)
        self.assertEqual(inst.description.as_json(), "ALU-PVC/PVDC BLISTERS. CARTONS OF 10 FILM-COATED TABLETS. ")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://ema.europa.eu/example/pcid").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://ema.europa.eu/example/pcid")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("{PCID}").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "{PCID}")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.packageItem[0].material[0].coding[0].code.value, FHIRCode("PVC").value)
        self.assertEqual(inst.packageItem[0].material[0].coding[0].code.as_json(), "PVC")
        self.assertEqual(inst.packageItem[0].material[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/packageItemContainerMaterial").value)
        self.assertEqual(inst.packageItem[0].material[0].coding[0].system.as_json(), "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].material[1].coding[0].code.value, FHIRCode("PVDC").value)
        self.assertEqual(inst.packageItem[0].material[1].coding[0].code.as_json(), "PVDC")
        self.assertEqual(inst.packageItem[0].material[1].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/packageItemContainerMaterial").value)
        self.assertEqual(inst.packageItem[0].material[1].coding[0].system.as_json(), "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].material[2].coding[0].code.value, FHIRCode("alu").value)
        self.assertEqual(inst.packageItem[0].material[2].coding[0].code.as_json(), "alu")
        self.assertEqual(inst.packageItem[0].material[2].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/packageItemContainerMaterial").value)
        self.assertEqual(inst.packageItem[0].material[2].coding[0].system.as_json(), "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].packageItem[0].material[0].coding[0].code.value, FHIRCode("Paperboard").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].material[0].coding[0].code.as_json(), "Paperboard")
        self.assertEqual(inst.packageItem[0].packageItem[0].material[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/packageItemContainerMaterial").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].material[0].coding[0].system.as_json(), "http://ema.europa.eu/example/packageItemContainerMaterial")
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.unit.value, FHIRString("mm").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.unit.as_json(), "mm")
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.height.value, 125)
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.unit.value, FHIRString("mm").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.unit.as_json(), "mm")
        self.assertEqual(inst.packageItem[0].packageItem[0].physicalCharacteristics.width.value, 45)
        self.assertEqual(inst.packageItem[0].packageItem[0].quantity.unit.value, FHIRString("1").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].quantity.unit.as_json(), "1")
        self.assertEqual(inst.packageItem[0].packageItem[0].quantity.value, 1)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.unit.value, FHIRString("a").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.unit.as_json(), "a")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].period.value, 3)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].code.value, FHIRCode("Thismedicinalproductdoesnotrequireanyspecialstoragecondition.").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].code.as_json(), "Thismedicinalproductdoesnotrequireanyspecialstoragecondition.")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/specialprecautionsforstorage").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].specialPrecautionsForStorage[0].coding[0].system.as_json(), "http://ema.europa.eu/example/specialprecautionsforstorage")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].code.value, FHIRCode("ShelfLifeofPackagedMedicinalProduct").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].code.as_json(), "ShelfLifeofPackagedMedicinalProduct")
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/shelfLifeTypePlaceHolder").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].shelfLifeStorage[0].type.coding[0].system.as_json(), "http://ema.europa.eu/example/shelfLifeTypePlaceHolder")
        self.assertEqual(inst.packageItem[0].packageItem[0].type.coding[0].code.value, FHIRCode("Blister").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].type.coding[0].code.as_json(), "Blister")
        self.assertEqual(inst.packageItem[0].packageItem[0].type.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/packageitemcontainertype").value)
        self.assertEqual(inst.packageItem[0].packageItem[0].type.coding[0].system.as_json(), "http://ema.europa.eu/example/packageitemcontainertype")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.depth.unit.value, FHIRString("mm").value)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.depth.unit.as_json(), "mm")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.depth.value, 23.5)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.height.unit.value, FHIRString("mm").value)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.height.unit.as_json(), "mm")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.height.value, 50)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.width.unit.value, FHIRString("mm").value)
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.width.unit.as_json(), "mm")
        self.assertEqual(inst.packageItem[0].physicalCharacteristics.width.value, 136)
        self.assertEqual(inst.packageItem[0].quantity.unit.value, FHIRString("1").value)
        self.assertEqual(inst.packageItem[0].quantity.unit.as_json(), "1")
        self.assertEqual(inst.packageItem[0].quantity.value, 1)
        self.assertEqual(inst.packageItem[0].type.coding[0].code.value, FHIRCode("Carton").value)
        self.assertEqual(inst.packageItem[0].type.coding[0].code.as_json(), "Carton")
        self.assertEqual(inst.packageItem[0].type.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/packageitemcontainertype").value)
        self.assertEqual(inst.packageItem[0].type.coding[0].system.as_json(), "http://ema.europa.eu/example/packageitemcontainertype")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRDateTime, FHIRUri, FHIRString, FHIRCode