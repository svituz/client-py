#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import medicinalproductauthorization

class MedicinalProductAuthorizationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductAuthorization", js["resourceType"])
        return medicinalproductauthorization.MedicinalProductAuthorization(js)

    def testMedicinalProductAuthorization1(self):
        inst = self.instantiate_from('medicinalproductauthorization-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a MedicinalProductAuthorization instance')
        self.implMedicinalProductAuthorization1(inst)

        js = inst.as_json()
        self.assertEqual("MedicinalProductAuthorization", js["resourceType"])
        inst2 = medicinalproductauthorization.MedicinalProductAuthorization(js)
        self.implMedicinalProductAuthorization1(inst2)

    def implMedicinalProductAuthorization1(self, inst):
        self.assertEqual(inst.country[0].coding[0].code.value, FHIRCode("EU").value)
        self.assertEqual(inst.country[0].coding[0].code.as_json(), "EU")
        self.assertEqual(inst.country[0].coding[0].system.value, FHIRUri("http://ema.europa.eu/example/country").value)
        self.assertEqual(inst.country[0].coding[0].system.as_json(), "http://ema.europa.eu/example/country")
        self.assertEqual(inst.dataExclusivityPeriod.end.value, FHIRDateTime("2020-08-15").value)
        self.assertEqual(inst.dataExclusivityPeriod.end.as_json(), "2020-08-15")
        self.assertEqual(inst.dataExclusivityPeriod.start.value, FHIRDateTime("2010-08-15").value)
        self.assertEqual(inst.dataExclusivityPeriod.start.as_json(), "2010-08-15")
        self.assertEqual(inst.dateOfFirstAuthorization.value, FHIRDateTime("2010-08-15").value)
        self.assertEqual(inst.dateOfFirstAuthorization.as_json(), "2010-08-15")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://ema.europa.eu/example/marketingAuthorisationNumber").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://ema.europa.eu/example/marketingAuthorisationNumber")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("EU/1/11/999/001").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "EU/1/11/999/001")
        self.assertEqual(inst.internationalBirthDate.value, FHIRDateTime("2010-08-15").value)
        self.assertEqual(inst.internationalBirthDate.as_json(), "2010-08-15")
        self.assertEqual(inst.jurisdictionalAuthorization[0].country.coding[0].code.value, FHIRCode("NO").value)
        self.assertEqual(inst.jurisdictionalAuthorization[0].country.coding[0].code.as_json(), "NO")
        self.assertEqual(inst.jurisdictionalAuthorization[0].country.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/countryCode").value)
        self.assertEqual(inst.jurisdictionalAuthorization[0].country.coding[0].system.as_json(), "http://ema.europa.eu/example/countryCode")
        self.assertEqual(inst.jurisdictionalAuthorization[0].identifier[0].system.value, FHIRUri("http://ema.europa.eu/example/marketingauthorisationnumber").value)
        self.assertEqual(inst.jurisdictionalAuthorization[0].identifier[0].system.as_json(), "http://ema.europa.eu/example/marketingauthorisationnumber")
        self.assertEqual(inst.jurisdictionalAuthorization[0].identifier[0].value.value, FHIRString("123-456-789").value)
        self.assertEqual(inst.jurisdictionalAuthorization[0].identifier[0].value.as_json(), "123-456-789")
        self.assertEqual(inst.jurisdictionalAuthorization[1].country.coding[0].code.value, FHIRCode("NO").value)
        self.assertEqual(inst.jurisdictionalAuthorization[1].country.coding[0].code.as_json(), "NO")
        self.assertEqual(inst.jurisdictionalAuthorization[1].country.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/countryCode").value)
        self.assertEqual(inst.jurisdictionalAuthorization[1].country.coding[0].system.as_json(), "http://ema.europa.eu/example/countryCode")
        self.assertEqual(inst.jurisdictionalAuthorization[1].identifier[0].system.value, FHIRUri("http://ema.europa.eu/example/marketingauthorisationnumber").value)
        self.assertEqual(inst.jurisdictionalAuthorization[1].identifier[0].system.as_json(), "http://ema.europa.eu/example/marketingauthorisationnumber")
        self.assertEqual(inst.jurisdictionalAuthorization[1].identifier[0].value.value, FHIRString("123-456-123").value)
        self.assertEqual(inst.jurisdictionalAuthorization[1].identifier[0].value.as_json(), "123-456-123")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.procedure.application[0].dateDateTime.value, FHIRDateTime("2015-08-01").value)
        self.assertEqual(inst.procedure.application[0].dateDateTime.as_json(), "2015-08-01")
        self.assertEqual(inst.procedure.application[0].identifier.system.value, FHIRUri("http://ema.europa.eu/example/applicationidentifier-number").value)
        self.assertEqual(inst.procedure.application[0].identifier.system.as_json(), "http://ema.europa.eu/example/applicationidentifier-number")
        self.assertEqual(inst.procedure.application[0].identifier.value.value, FHIRString("IA38G").value)
        self.assertEqual(inst.procedure.application[0].identifier.value.as_json(), "IA38G")
        self.assertEqual(inst.procedure.application[0].type.coding[0].code.value, FHIRCode("GroupTypeIAVariationNotification").value)
        self.assertEqual(inst.procedure.application[0].type.coding[0].code.as_json(), "GroupTypeIAVariationNotification")
        self.assertEqual(inst.procedure.application[0].type.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/marketingAuthorisationApplicationType").value)
        self.assertEqual(inst.procedure.application[0].type.coding[0].system.as_json(), "http://ema.europa.eu/example/marketingAuthorisationApplicationType")
        self.assertEqual(inst.procedure.datePeriod.end.value, FHIRDateTime("2015-08-21").value)
        self.assertEqual(inst.procedure.datePeriod.end.as_json(), "2015-08-21")
        self.assertEqual(inst.procedure.datePeriod.start.value, FHIRDateTime("2015-08-02").value)
        self.assertEqual(inst.procedure.datePeriod.start.as_json(), "2015-08-02")
        self.assertEqual(inst.procedure.identifier.system.value, FHIRUri("http://ema.europa.eu/example/procedureidentifier-number").value)
        self.assertEqual(inst.procedure.identifier.system.as_json(), "http://ema.europa.eu/example/procedureidentifier-number")
        self.assertEqual(inst.procedure.identifier.value.value, FHIRString("EMEA/H/C/009999/IA/0099/G").value)
        self.assertEqual(inst.procedure.identifier.value.as_json(), "EMEA/H/C/009999/IA/0099/G")
        self.assertEqual(inst.procedure.type.coding[0].code.value, FHIRCode("VariationTypeIA").value)
        self.assertEqual(inst.procedure.type.coding[0].code.as_json(), "VariationTypeIA")
        self.assertEqual(inst.procedure.type.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/marketingAuthorisationProcedureType").value)
        self.assertEqual(inst.procedure.type.coding[0].system.as_json(), "http://ema.europa.eu/example/marketingAuthorisationProcedureType")
        self.assertEqual(inst.status.coding[0].code.value, FHIRCode("active").value)
        self.assertEqual(inst.status.coding[0].code.as_json(), "active")
        self.assertEqual(inst.status.coding[0].system.value, FHIRUri("http://ema.europa.eu/example/authorisationstatus").value)
        self.assertEqual(inst.status.coding[0].system.as_json(), "http://ema.europa.eu/example/authorisationstatus")
        self.assertEqual(inst.statusDate.value, FHIRDateTime("2015-01-14").value)
        self.assertEqual(inst.statusDate.as_json(), "2015-01-14")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.validityPeriod.end.value, FHIRDateTime("2020-05-20").value)
        self.assertEqual(inst.validityPeriod.end.as_json(), "2020-05-20")
        self.assertEqual(inst.validityPeriod.start.value, FHIRDateTime("2015-08-16").value)
        self.assertEqual(inst.validityPeriod.start.as_json(), "2015-08-16")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRUri, FHIRDateTime, FHIRString