#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import organizationaffiliation

class OrganizationAffiliationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OrganizationAffiliation", js["resourceType"])
        return organizationaffiliation.OrganizationAffiliation(js)

    def testOrganizationAffiliation1(self):
        inst = self.instantiate_from('orgrole-example-hie.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OrganizationAffiliation instance')
        self.implOrganizationAffiliation1(inst)

        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation1(inst2)

    def implOrganizationAffiliation1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code.value, FHIRCode("member").value)
        self.assertEqual(inst.code[0].coding[0].code.as_json(), "member")
        self.assertEqual(inst.code[0].coding[0].display.value, FHIRString("Member").value)
        self.assertEqual(inst.code[0].coding[0].display.as_json(), "Member")
        self.assertEqual(inst.code[0].coding[0].system.value, FHIRUri("http://hl7.org/fhir/organization-role").value)
        self.assertEqual(inst.code[0].coding[0].system.as_json(), "http://hl7.org/fhir/organization-role")
        self.assertEqual(inst.code[0].text.value, FHIRString("Hospital member").value)
        self.assertEqual(inst.code[0].text.as_json(), "Hospital member")
        self.assertEqual(inst.id.value, FHIRString("orgrole2").value)
        self.assertEqual(inst.id.as_json(), "orgrole2")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/www.monumentHIE.com").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/www.monumentHIE.com")
        self.assertEqual(inst.identifier[0].type.text.value, FHIRString("member hospital").value)
        self.assertEqual(inst.identifier[0].type.text.as_json(), "member hospital")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("secondary").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "secondary")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("hosp32").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "hosp32")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOrganizationAffiliation2(self):
        inst = self.instantiate_from('orgrole-example-services.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OrganizationAffiliation instance')
        self.implOrganizationAffiliation2(inst)

        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation2(inst2)

    def implOrganizationAffiliation2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code.value, FHIRCode("provider").value)
        self.assertEqual(inst.code[0].coding[0].code.as_json(), "provider")
        self.assertEqual(inst.code[0].coding[0].display.value, FHIRString("Provider").value)
        self.assertEqual(inst.code[0].coding[0].display.as_json(), "Provider")
        self.assertEqual(inst.code[0].coding[0].system.value, FHIRUri("http://hl7.org/fhir/organization-role").value)
        self.assertEqual(inst.code[0].coding[0].system.as_json(), "http://hl7.org/fhir/organization-role")
        self.assertTrue(inst.code[0].coding[0].userSelected)
        self.assertEqual(inst.code[0].text.value, FHIRString("Provider of rehabilitation services").value)
        self.assertEqual(inst.code[0].text.as_json(), "Provider of rehabilitation services")
        self.assertEqual(inst.id.value, FHIRString("orgrole1").value)
        self.assertEqual(inst.id.as_json(), "orgrole1")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://example.org/www.foundingfathersmemorial.com").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://example.org/www.foundingfathersmemorial.com")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("secondary").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "secondary")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("service002").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "service002")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2022-02-01").value)
        self.assertEqual(inst.period.end.as_json(), "2022-02-01")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2018-02-09").value)
        self.assertEqual(inst.period.start.as_json(), "2018-02-09")
        self.assertEqual(inst.specialty[0].coding[0].code.value, FHIRCode("394602003").value)
        self.assertEqual(inst.specialty[0].coding[0].code.as_json(), "394602003")
        self.assertEqual(inst.specialty[0].coding[0].display.value, FHIRString("Rehabilitation - specialty").value)
        self.assertEqual(inst.specialty[0].coding[0].display.as_json(), "Rehabilitation - specialty")
        self.assertEqual(inst.specialty[0].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.specialty[0].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.specialty[0].text.value, FHIRString("Rehabilitation").value)
        self.assertEqual(inst.specialty[0].text.as_json(), "Rehabilitation")
        self.assertEqual(inst.telecom[0].system.value, FHIRCode("phone").value)
        self.assertEqual(inst.telecom[0].system.as_json(), "phone")
        self.assertEqual(inst.telecom[0].use.value, FHIRCode("work").value)
        self.assertEqual(inst.telecom[0].use.as_json(), "work")
        self.assertEqual(inst.telecom[0].value.value, FHIRString("202-109-8765").value)
        self.assertEqual(inst.telecom[0].value.as_json(), "202-109-8765")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")

    def testOrganizationAffiliation3(self):
        inst = self.instantiate_from('organizationaffiliation-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a OrganizationAffiliation instance')
        self.implOrganizationAffiliation3(inst)

        js = inst.as_json()
        self.assertEqual("OrganizationAffiliation", js["resourceType"])
        inst2 = organizationaffiliation.OrganizationAffiliation(js)
        self.implOrganizationAffiliation3(inst2)

    def implOrganizationAffiliation3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.code[0].coding[0].code.value, FHIRCode("provider").value)
        self.assertEqual(inst.code[0].coding[0].code.as_json(), "provider")
        self.assertEqual(inst.code[0].coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/organization-role").value)
        self.assertEqual(inst.code[0].coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/organization-role")
        self.assertEqual(inst.id.value, FHIRString("example").value)
        self.assertEqual(inst.id.as_json(), "example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://www.acme.org/practitioners").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://www.acme.org/practitioners")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("23").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "23")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.period.end.value, FHIRDateTime("2012-03-31").value)
        self.assertEqual(inst.period.end.as_json(), "2012-03-31")
        self.assertEqual(inst.period.start.value, FHIRDateTime("2012-01-01").value)
        self.assertEqual(inst.period.start.as_json(), "2012-01-01")
        self.assertEqual(inst.specialty[0].coding[0].code.value, FHIRCode("408443003").value)
        self.assertEqual(inst.specialty[0].coding[0].code.as_json(), "408443003")
        self.assertEqual(inst.specialty[0].coding[0].display.value, FHIRString("General medical practice").value)
        self.assertEqual(inst.specialty[0].coding[0].display.as_json(), "General medical practice")
        self.assertEqual(inst.specialty[0].coding[0].system.value, FHIRUri("http://snomed.info/sct").value)
        self.assertEqual(inst.specialty[0].coding[0].system.as_json(), "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system.value, FHIRCode("email").value)
        self.assertEqual(inst.telecom[0].system.as_json(), "email")
        self.assertEqual(inst.telecom[0].use.value, FHIRCode("work").value)
        self.assertEqual(inst.telecom[0].use.as_json(), "work")
        self.assertEqual(inst.telecom[0].value.value, FHIRString("general.practice@example.org").value)
        self.assertEqual(inst.telecom[0].value.as_json(), "general.practice@example.org")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRDateTime