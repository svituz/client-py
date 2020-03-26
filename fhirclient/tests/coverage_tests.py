#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import coverage

class CoverageTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Coverage", js["resourceType"])
        return coverage.Coverage(js)

    def testCoverage1(self):
        inst = self.instantiate_from('coverage-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Coverage instance')
        self.implCoverage1(inst)

        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage1(inst2)

    def implCoverage1(self, inst):
        self.assertEqual(inst.class_fhir[0].name.value, FHIRString("Corporate Baker's Inc. Local #35").value)
        self.assertEqual(inst.class_fhir[0].name.as_json(), "Corporate Baker's Inc. Local #35")
        self.assertEqual(inst.class_fhir[0].type.coding[0].code.value, FHIRCode("group").value)
        self.assertEqual(inst.class_fhir[0].type.coding[0].code.as_json(), "group")
        self.assertEqual(inst.class_fhir[0].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[0].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[0].value.value, FHIRString("CB135").value)
        self.assertEqual(inst.class_fhir[0].value.as_json(), "CB135")
        self.assertEqual(inst.class_fhir[1].name.value, FHIRString("Trainee Part-time Benefits").value)
        self.assertEqual(inst.class_fhir[1].name.as_json(), "Trainee Part-time Benefits")
        self.assertEqual(inst.class_fhir[1].type.coding[0].code.value, FHIRCode("subgroup").value)
        self.assertEqual(inst.class_fhir[1].type.coding[0].code.as_json(), "subgroup")
        self.assertEqual(inst.class_fhir[1].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[1].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[1].value.value, FHIRString("123").value)
        self.assertEqual(inst.class_fhir[1].value.as_json(), "123")
        self.assertEqual(inst.class_fhir[2].name.value, FHIRString("Full Coverage: Medical, Dental, Pharmacy, Vision, EHC").value)
        self.assertEqual(inst.class_fhir[2].name.as_json(), "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC")
        self.assertEqual(inst.class_fhir[2].type.coding[0].code.value, FHIRCode("plan").value)
        self.assertEqual(inst.class_fhir[2].type.coding[0].code.as_json(), "plan")
        self.assertEqual(inst.class_fhir[2].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[2].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[2].value.value, FHIRString("B37FC").value)
        self.assertEqual(inst.class_fhir[2].value.as_json(), "B37FC")
        self.assertEqual(inst.class_fhir[3].name.value, FHIRString("Includes afterlife benefits").value)
        self.assertEqual(inst.class_fhir[3].name.as_json(), "Includes afterlife benefits")
        self.assertEqual(inst.class_fhir[3].type.coding[0].code.value, FHIRCode("subplan").value)
        self.assertEqual(inst.class_fhir[3].type.coding[0].code.as_json(), "subplan")
        self.assertEqual(inst.class_fhir[3].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[3].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[3].value.value, FHIRString("P7").value)
        self.assertEqual(inst.class_fhir[3].value.as_json(), "P7")
        self.assertEqual(inst.class_fhir[4].name.value, FHIRString("Silver: Family Plan spouse only").value)
        self.assertEqual(inst.class_fhir[4].name.as_json(), "Silver: Family Plan spouse only")
        self.assertEqual(inst.class_fhir[4].type.coding[0].code.value, FHIRCode("class").value)
        self.assertEqual(inst.class_fhir[4].type.coding[0].code.as_json(), "class")
        self.assertEqual(inst.class_fhir[4].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[4].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[4].value.value, FHIRString("SILVER").value)
        self.assertEqual(inst.class_fhir[4].value.as_json(), "SILVER")
        self.assertEqual(inst.class_fhir[5].name.value, FHIRString("Low deductable, max $20 copay").value)
        self.assertEqual(inst.class_fhir[5].name.as_json(), "Low deductable, max $20 copay")
        self.assertEqual(inst.class_fhir[5].type.coding[0].code.value, FHIRCode("subclass").value)
        self.assertEqual(inst.class_fhir[5].type.coding[0].code.as_json(), "subclass")
        self.assertEqual(inst.class_fhir[5].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[5].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[5].value.value, FHIRString("Tier2").value)
        self.assertEqual(inst.class_fhir[5].value.as_json(), "Tier2")
        self.assertEqual(inst.class_fhir[6].type.coding[0].code.value, FHIRCode("sequence").value)
        self.assertEqual(inst.class_fhir[6].type.coding[0].code.as_json(), "sequence")
        self.assertEqual(inst.class_fhir[6].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[6].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[6].value.value, FHIRString("9").value)
        self.assertEqual(inst.class_fhir[6].value.as_json(), "9")
        self.assertEqual(inst.class_fhir[7].type.coding[0].code.value, FHIRCode("rxid").value)
        self.assertEqual(inst.class_fhir[7].type.coding[0].code.as_json(), "rxid")
        self.assertEqual(inst.class_fhir[7].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[7].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[7].value.value, FHIRString("MDF12345").value)
        self.assertEqual(inst.class_fhir[7].value.as_json(), "MDF12345")
        self.assertEqual(inst.class_fhir[8].type.coding[0].code.value, FHIRCode("rxbin").value)
        self.assertEqual(inst.class_fhir[8].type.coding[0].code.as_json(), "rxbin")
        self.assertEqual(inst.class_fhir[8].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[8].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[8].value.value, FHIRString("987654").value)
        self.assertEqual(inst.class_fhir[8].value.as_json(), "987654")
        self.assertEqual(inst.class_fhir[9].type.coding[0].code.value, FHIRCode("rxgroup").value)
        self.assertEqual(inst.class_fhir[9].type.coding[0].code.as_json(), "rxgroup")
        self.assertEqual(inst.class_fhir[9].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[9].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[9].value.value, FHIRString("M35PT").value)
        self.assertEqual(inst.class_fhir[9].value.as_json(), "M35PT")
        self.assertEqual(inst.dependent.value, FHIRString("0").value)
        self.assertEqual(inst.dependent.as_json(), "0")
        self.assertEqual(inst.id.value, FHIRString("9876B1").value)
        self.assertEqual(inst.id.as_json(), "9876B1")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://benefitsinc.com/certificate").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://benefitsinc.com/certificate")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("12345").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "12345")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2012-05-23").value)
        self.assertEqual(inst.period.end.as_json(), "2012-05-23")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2011-05-23").value)
        self.assertEqual(inst.period.start.as_json(), "2011-05-23")
        self.assertEqual(inst.relationship.coding[0].code.value, FHIRCode("self").value)
        self.assertEqual(inst.relationship.coding[0].code.as_json(), "self")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("EHCPOL").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "EHCPOL")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("extended healthcare").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "extended healthcare")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")

    def testCoverage2(self):
        inst = self.instantiate_from('coverage-example-2.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Coverage instance')
        self.implCoverage2(inst)

        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage2(inst2)

    def implCoverage2(self, inst):
        self.assertEqual(inst.class_fhir[0].name.value, FHIRString("Western Airlines").value)
        self.assertEqual(inst.class_fhir[0].name.as_json(), "Western Airlines")
        self.assertEqual(inst.class_fhir[0].type.coding[0].code.value, FHIRCode("group").value)
        self.assertEqual(inst.class_fhir[0].type.coding[0].code.as_json(), "group")
        self.assertEqual(inst.class_fhir[0].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[0].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[0].value.value, FHIRString("WESTAIR").value)
        self.assertEqual(inst.class_fhir[0].value.as_json(), "WESTAIR")
        self.assertEqual(inst.class_fhir[1].name.value, FHIRString("Full Coverage: Medical, Dental, Pharmacy, Vision, EHC").value)
        self.assertEqual(inst.class_fhir[1].name.as_json(), "Full Coverage: Medical, Dental, Pharmacy, Vision, EHC")
        self.assertEqual(inst.class_fhir[1].type.coding[0].code.value, FHIRCode("plan").value)
        self.assertEqual(inst.class_fhir[1].type.coding[0].code.as_json(), "plan")
        self.assertEqual(inst.class_fhir[1].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[1].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[1].value.value, FHIRString("BG4352").value)
        self.assertEqual(inst.class_fhir[1].value.as_json(), "BG4352")
        self.assertEqual(inst.class_fhir[2].name.value, FHIRString("Platinum").value)
        self.assertEqual(inst.class_fhir[2].name.as_json(), "Platinum")
        self.assertEqual(inst.class_fhir[2].type.coding[0].code.value, FHIRCode("subplan").value)
        self.assertEqual(inst.class_fhir[2].type.coding[0].code.as_json(), "subplan")
        self.assertEqual(inst.class_fhir[2].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-class").value)
        self.assertEqual(inst.class_fhir[2].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-class")
        self.assertEqual(inst.class_fhir[2].value.value, FHIRString("D15C9").value)
        self.assertEqual(inst.class_fhir[2].value.as_json(), "D15C9")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.end.value, FHIRDateTime("2018-12-31").value)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.end.as_json(), "2018-12-31")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.start.value, FHIRDateTime("2018-01-01").value)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].period.start.as_json(), "2018-01-01")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].type.coding[0].code.value, FHIRCode("retired").value)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].type.coding[0].code.as_json(), "retired")
        self.assertEqual(inst.costToBeneficiary[0].exception[0].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception").value)
        self.assertEqual(inst.costToBeneficiary[0].exception[0].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/ex-coverage-financial-exception")
        self.assertEqual(inst.costToBeneficiary[0].type.coding[0].code.value, FHIRCode("gpvisit").value)
        self.assertEqual(inst.costToBeneficiary[0].type.coding[0].code.as_json(), "gpvisit")
        self.assertEqual(inst.costToBeneficiary[0].type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-copay-type").value)
        self.assertEqual(inst.costToBeneficiary[0].type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-copay-type")
        self.assertEqual(inst.costToBeneficiary[0].valueMoney.currency.value, FHIRCode("USD").value)
        self.assertEqual(inst.costToBeneficiary[0].valueMoney.currency.as_json(), "USD")
        self.assertEqual(inst.costToBeneficiary[0].valueMoney.value, 20.0)
        self.assertEqual(inst.dependent.value, FHIRString("1").value)
        self.assertEqual(inst.dependent.as_json(), "1")
        self.assertEqual(inst.id.value, FHIRString("7546D").value)
        self.assertEqual(inst.id.as_json(), "7546D")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://xyz.com/codes/identifier").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://xyz.com/codes/identifier")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("AB98761").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "AB98761")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.network.value, FHIRString("5").value)
        self.assertEqual(inst.network.as_json(), "5")
        self.assertEqual(inst.order.value, FHIRPositiveInt('2').value)
        self.assertEqual(inst.order.as_json(), 2)
        self.assertEqual(inst.period.end.value, FHIRDateTime("2012-03-17").value)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2011-03-17").value)
        self.assertEqual(inst.period.start.as_json(), "2011-03-17")
        self.assertEqual(inst.relationship.coding[0].code.value, FHIRCode("self").value)
        self.assertEqual(inst.relationship.coding[0].code.as_json(), "self")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.subscriberId.value, FHIRString("AB9876").value)
        self.assertEqual(inst.subscriberId.as_json(), "AB9876")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the coverage</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("EHCPOL").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "EHCPOL")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("extended healthcare").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "extended healthcare")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")

    def testCoverage3(self):
        inst = self.instantiate_from('coverage-example-ehic.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Coverage instance')
        self.implCoverage3(inst)

        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage3(inst2)

    def implCoverage3(self, inst):
        self.assertEqual(inst.id.value, FHIRString("7547E").value)
        self.assertEqual(inst.id.as_json(), "7547E")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://ehic.com/insurer/123456789/member").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://ehic.com/insurer/123456789/member")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("A123456780").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "A123456780")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2012-03-17").value)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.relationship.coding[0].code.value, FHIRCode("self").value)
        self.assertEqual(inst.relationship.coding[0].code.as_json(), "self")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the European Health Insurance Card</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the European Health Insurance Card</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("EHCPOL").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "EHCPOL")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("extended healthcare").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "extended healthcare")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActCode").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActCode")

    def testCoverage4(self):
        inst = self.instantiate_from('coverage-example-selfpay.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Coverage instance')
        self.implCoverage4(inst)

        js = inst.as_json()
        self.assertEqual("Coverage", js["resourceType"])
        inst2 = coverage.Coverage(js)
        self.implCoverage4(inst2)

    def implCoverage4(self, inst):
        self.assertEqual(inst.id.value, FHIRString("SP1234").value)
        self.assertEqual(inst.id.as_json(), "SP1234")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://hospitalx.com/selfpayagreement").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://hospitalx.com/selfpayagreement")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("SP12345678").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "SP12345678")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2012-03-17").value)
        self.assertEqual(inst.period.end.as_json(), "2012-03-17")
        self.assertEqual(inst.relationship.coding[0].code.value, FHIRCode("self").value)
        self.assertEqual(inst.relationship.coding[0].code.as_json(), "self")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.div.value, FHIRString("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of a Self Pay Agreement.</div>").value)
        self.assertEqual(inst.text.div.as_json(), "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of a Self Pay Agreement.</div>")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.type.coding[0].code.value, FHIRCode("pay").value)
        self.assertEqual(inst.type.coding[0].code.as_json(), "pay")
        self.assertEqual(inst.type.coding[0].display.value, FHIRString("PAY").value)
        self.assertEqual(inst.type.coding[0].display.as_json(), "PAY")
        self.assertEqual(inst.type.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/coverage-selfpay").value)
        self.assertEqual(inst.type.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/coverage-selfpay")


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRUri, FHIRDateTime, FHIRPositiveInt