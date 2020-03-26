#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-26.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import measure

class MeasureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Measure", js["resourceType"])
        return measure.Measure(js)

    def testMeasure1(self):
        inst = self.instantiate_from('measure-composite-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Measure instance')
        self.implMeasure1(inst)

        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure1(inst2)

    def implMeasure1(self, inst):
        self.assertEqual(inst.compositeScoring.coding[0].code.value, FHIRCode("opportunity").value)
        self.assertEqual(inst.compositeScoring.coding[0].code.as_json(), "opportunity")
        self.assertEqual(inst.id.value, FHIRString("composite-example").value)
        self.assertEqual(inst.id.as_json(), "composite-example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.relatedArtifact[0].resource.value, FHIRCanonical("Measure/component-a-example").value)
        self.assertEqual(inst.relatedArtifact[0].resource.as_json(), "Measure/component-a-example")
        self.assertEqual(inst.relatedArtifact[0].type.value, FHIRCode("composed-of").value)
        self.assertEqual(inst.relatedArtifact[0].type.as_json(), "composed-of")
        self.assertEqual(inst.relatedArtifact[1].resource.value, FHIRCanonical("Measure/component-b-example").value)
        self.assertEqual(inst.relatedArtifact[1].resource.as_json(), "Measure/component-b-example")
        self.assertEqual(inst.relatedArtifact[1].type.value, FHIRCode("composed-of").value)
        self.assertEqual(inst.relatedArtifact[1].type.as_json(), "composed-of")
        self.assertEqual(inst.scoring.coding[0].code.value, FHIRCode("proportion").value)
        self.assertEqual(inst.scoring.coding[0].code.as_json(), "proportion")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Behavioral Assessment Composite Measure").value)
        self.assertEqual(inst.title.as_json(), "Behavioral Assessment Composite Measure")

    def testMeasure2(self):
        inst = self.instantiate_from('measure-cms146-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Measure instance')
        self.implMeasure2(inst)

        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure2(inst2)

    def implMeasure2(self, inst):
        self.assertEqual(inst.approvalDate.value, FHIRDate("2016-01-01").value)
        self.assertEqual(inst.approvalDate.as_json(), "2016-01-01")
        self.assertEqual(inst.approvalDate.date, FHIRDate('2016-01-01').date)
        self.assertEqual(inst.author[0].name.value, FHIRString("National Committee for Quality Assurance").value)
        self.assertEqual(inst.author[0].name.as_json(), "National Committee for Quality Assurance")
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode("url").value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), "url")
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString("http://www.ncqa.org/").value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), "http://www.ncqa.org/")
        self.assertEqual(inst.date.value, FHIRDateTime("2017-03-10").value)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(inst.description.value, FHIRMarkdown("Percentage of children 3-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode.").value)
        self.assertEqual(inst.description.as_json(), "Percentage of children 3-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode.")
        self.assertEqual(inst.effectivePeriod.end.value, FHIRDateTime("2017-12-31").value)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.value, FHIRDateTime("2017-01-01").value)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2017-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(inst.group[0].id.value, FHIRString("CMS146-group-1").value)
        self.assertEqual(inst.group[0].id.as_json(), "CMS146-group-1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.value, FHIRCode("initial-population").value)
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.as_json(), "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression.value, FHIRString("CMS146.InInitialPopulation").value)
        self.assertEqual(inst.group[0].population[0].criteria.expression.as_json(), "CMS146.InInitialPopulation")
        self.assertEqual(inst.group[0].population[0].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[0].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.value, FHIRCode("numerator").value)
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.as_json(), "numerator")
        self.assertEqual(inst.group[0].population[1].criteria.expression.value, FHIRString("CMS146.InNumerator").value)
        self.assertEqual(inst.group[0].population[1].criteria.expression.as_json(), "CMS146.InNumerator")
        self.assertEqual(inst.group[0].population[1].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[1].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.value, FHIRCode("denominator").value)
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.as_json(), "denominator")
        self.assertEqual(inst.group[0].population[2].criteria.expression.value, FHIRString("CMS146.InDenominator").value)
        self.assertEqual(inst.group[0].population[2].criteria.expression.as_json(), "CMS146.InDenominator")
        self.assertEqual(inst.group[0].population[2].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[2].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code.value, FHIRCode("denominator-exclusion").value)
        self.assertEqual(inst.group[0].population[3].code.coding[0].code.as_json(), "denominator-exclusion")
        self.assertEqual(inst.group[0].population[3].criteria.expression.value, FHIRString("CMS146.InDenominatorExclusions").value)
        self.assertEqual(inst.group[0].population[3].criteria.expression.as_json(), "CMS146.InDenominatorExclusions")
        self.assertEqual(inst.group[0].population[3].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[3].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].stratifier[0].code.text.value, FHIRString("stratifier-ages-up-to-9").value)
        self.assertEqual(inst.group[0].stratifier[0].code.text.as_json(), "stratifier-ages-up-to-9")
        self.assertEqual(inst.group[0].stratifier[0].criteria.expression.value, FHIRString("CMS146.AgesUpToNine").value)
        self.assertEqual(inst.group[0].stratifier[0].criteria.expression.as_json(), "CMS146.AgesUpToNine")
        self.assertEqual(inst.group[0].stratifier[0].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].stratifier[0].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].stratifier[1].code.text.value, FHIRString("stratifier-ages-10-plus").value)
        self.assertEqual(inst.group[0].stratifier[1].code.text.as_json(), "stratifier-ages-10-plus")
        self.assertEqual(inst.group[0].stratifier[1].criteria.expression.value, FHIRString("CMS146.AgesTenPlus").value)
        self.assertEqual(inst.group[0].stratifier[1].criteria.expression.as_json(), "CMS146.AgesTenPlus")
        self.assertEqual(inst.group[0].stratifier[1].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].stratifier[1].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].stratifier[2].code.text.value, FHIRString("stratifier-gender").value)
        self.assertEqual(inst.group[0].stratifier[2].code.text.as_json(), "stratifier-gender")
        self.assertEqual(inst.group[0].stratifier[2].criteria.expression.value, FHIRString("Patient.gender").value)
        self.assertEqual(inst.group[0].stratifier[2].criteria.expression.as_json(), "Patient.gender")
        self.assertEqual(inst.group[0].stratifier[2].criteria.language.value, FHIRCode("text/fhirpath").value)
        self.assertEqual(inst.group[0].stratifier[2].criteria.language.as_json(), "text/fhirpath")
        self.assertEqual(inst.guidance.value, FHIRMarkdown("This is an episode of care measure that examines all eligible episodes for the patient during the measurement period. If the patient has more than one episode, include all episodes in the measure").value)
        self.assertEqual(inst.guidance.as_json(), "This is an episode of care measure that examines all eligible episodes for the patient during the measurement period. If the patient has more than one episode, include all episodes in the measure")
        self.assertEqual(inst.id.value, FHIRString("measure-cms146-example").value)
        self.assertEqual(inst.id.as_json(), "measure-cms146-example")
        self.assertEqual(inst.identifier[0].system.value, FHIRUri("http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms").value)
        self.assertEqual(inst.identifier[0].system.as_json(), "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("official").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "official")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("146").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "146")
        self.assertEqual(inst.identifier[1].system.value, FHIRUri("http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf").value)
        self.assertEqual(inst.identifier[1].system.as_json(), "http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf")
        self.assertEqual(inst.identifier[1].use.value, FHIRCode("official").value)
        self.assertEqual(inst.identifier[1].use.as_json(), "official")
        self.assertEqual(inst.identifier[1].value.value, FHIRString("0002").value)
        self.assertEqual(inst.identifier[1].value.as_json(), "0002")
        self.assertEqual(inst.improvementNotation.coding[0].code.value, FHIRCode("increase").value)
        self.assertEqual(inst.improvementNotation.coding[0].code.as_json(), "increase")
        self.assertEqual(inst.improvementNotation.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/measure-improvement-notation").value)
        self.assertEqual(inst.improvementNotation.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/measure-improvement-notation")
        self.assertEqual(inst.jurisdiction[0].coding[0].code.value, FHIRCode("US").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.as_json(), "US")
        self.assertEqual(inst.jurisdiction[0].coding[0].system.value, FHIRUri("urn:iso:std:iso:3166").value)
        self.assertEqual(inst.jurisdiction[0].coding[0].system.as_json(), "urn:iso:std:iso:3166")
        self.assertEqual(inst.lastReviewDate.value, FHIRDate("2016-09-01").value)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-09-01")
        self.assertEqual(inst.lastReviewDate.date, FHIRDate('2016-09-01').date)
        self.assertEqual(inst.library[0].value, FHIRCanonical("Library/library-cms146-example").value)
        self.assertEqual(inst.library[0].as_json(), "Library/library-cms146-example")
        self.assertEqual(inst.name.value, FHIRString("CMS146").value)
        self.assertEqual(inst.name.as_json(), "CMS146")
        self.assertEqual(inst.publisher.value, FHIRString("National Committee for Quality Assurance").value)
        self.assertEqual(inst.publisher.as_json(), "National Committee for Quality Assurance")
        self.assertEqual(inst.purpose.value, FHIRMarkdown("Measure of children with a group A streptococcus test in the 7-day period from 3 days prior through 3 days after the diagnosis of pharyngitis").value)
        self.assertEqual(inst.purpose.as_json(), "Measure of children with a group A streptococcus test in the 7-day period from 3 days prior through 3 days after the diagnosis of pharyngitis")
        self.assertEqual(inst.relatedArtifact[0].citation.value, FHIRMarkdown("Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. _Antibiotic treatment of children with sore throat._ JAMA 294(18):2315-2322. ").value)
        self.assertEqual(inst.relatedArtifact[0].citation.as_json(), "Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. _Antibiotic treatment of children with sore throat._ JAMA 294(18):2315-2322. ")
        self.assertEqual(inst.relatedArtifact[0].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[0].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[1].citation.value, FHIRMarkdown("Infectious Diseases Society of America. 2012. _Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update._ ").value)
        self.assertEqual(inst.relatedArtifact[1].citation.as_json(), "Infectious Diseases Society of America. 2012. _Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update._ ")
        self.assertEqual(inst.relatedArtifact[1].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[1].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[2].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[2].type.as_json(), "documentation")
        self.assertEqual(inst.scoring.coding[0].code.value, FHIRCode("proportion").value)
        self.assertEqual(inst.scoring.coding[0].code.as_json(), "proportion")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.supplementalData[0].code.text.value, FHIRString("supplemental-data-gender").value)
        self.assertEqual(inst.supplementalData[0].code.text.as_json(), "supplemental-data-gender")
        self.assertEqual(inst.supplementalData[0].criteria.expression.value, FHIRString("Patient.gender").value)
        self.assertEqual(inst.supplementalData[0].criteria.expression.as_json(), "Patient.gender")
        self.assertEqual(inst.supplementalData[0].criteria.language.value, FHIRCode("text/fhirpath").value)
        self.assertEqual(inst.supplementalData[0].criteria.language.as_json(), "text/fhirpath")
        self.assertEqual(inst.supplementalData[1].code.text.value, FHIRString("supplemental-data-deceased").value)
        self.assertEqual(inst.supplementalData[1].code.text.as_json(), "supplemental-data-deceased")
        self.assertEqual(inst.supplementalData[1].criteria.expression.value, FHIRString("deceasedBoolean").value)
        self.assertEqual(inst.supplementalData[1].criteria.expression.as_json(), "deceasedBoolean")
        self.assertEqual(inst.supplementalData[1].criteria.language.value, FHIRCode("text/fhirpath").value)
        self.assertEqual(inst.supplementalData[1].criteria.language.as_json(), "text/fhirpath")
        self.assertEqual(inst.text.status.value, FHIRCode("additional").value)
        self.assertEqual(inst.text.status.as_json(), "additional")
        self.assertEqual(inst.title.value, FHIRString("Appropriate Testing for Children with Pharyngitis").value)
        self.assertEqual(inst.title.as_json(), "Appropriate Testing for Children with Pharyngitis")
        self.assertEqual(inst.topic[0].coding[0].code.value, FHIRCode("57024-2").value)
        self.assertEqual(inst.topic[0].coding[0].code.as_json(), "57024-2")
        self.assertEqual(inst.topic[0].coding[0].system.value, FHIRUri("http://loinc.org").value)
        self.assertEqual(inst.topic[0].coding[0].system.as_json(), "http://loinc.org")
        self.assertEqual(inst.type[0].coding[0].code.value, FHIRCode("process").value)
        self.assertEqual(inst.type[0].coding[0].code.as_json(), "process")
        self.assertEqual(inst.url.value, FHIRUri("http://hl7.org/fhir/Measure/measure-cms146-example").value)
        self.assertEqual(inst.url.as_json(), "http://hl7.org/fhir/Measure/measure-cms146-example")
        self.assertEqual(inst.useContext[0].code.code.value, FHIRCode("program").value)
        self.assertEqual(inst.useContext[0].code.code.as_json(), "program")
        self.assertEqual(inst.useContext[0].valueCodeableConcept.text.value, FHIRString("eligibile-provider").value)
        self.assertEqual(inst.useContext[0].valueCodeableConcept.text.as_json(), "eligibile-provider")
        self.assertEqual(inst.useContext[1].code.code.value, FHIRCode("age").value)
        self.assertEqual(inst.useContext[1].code.code.as_json(), "age")
        self.assertEqual(inst.useContext[1].code.system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/usage-context-type").value)
        self.assertEqual(inst.useContext[1].code.system.as_json(), "http://terminology.hl7.org/CodeSystem/usage-context-type")
        self.assertEqual(inst.useContext[1].valueRange.high.unit.value, FHIRString("a").value)
        self.assertEqual(inst.useContext[1].valueRange.high.unit.as_json(), "a")
        self.assertEqual(inst.useContext[1].valueRange.high.value, 18)
        self.assertEqual(inst.useContext[1].valueRange.low.unit.value, FHIRString("a").value)
        self.assertEqual(inst.useContext[1].valueRange.low.unit.as_json(), "a")
        self.assertEqual(inst.useContext[1].valueRange.low.value, 3)
        self.assertEqual(inst.version.value, FHIRString("1.0.0").value)
        self.assertEqual(inst.version.as_json(), "1.0.0")

    def testMeasure3(self):
        inst = self.instantiate_from('measure-component-b-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Measure instance')
        self.implMeasure3(inst)

        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure3(inst2)

    def implMeasure3(self, inst):
        self.assertEqual(inst.group[0].id.value, FHIRString("Main").value)
        self.assertEqual(inst.group[0].id.as_json(), "Main")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.value, FHIRCode("initial-population").value)
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.as_json(), "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression.value, FHIRString("Initial Population").value)
        self.assertEqual(inst.group[0].population[0].criteria.expression.as_json(), "Initial Population")
        self.assertEqual(inst.group[0].population[0].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[0].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.value, FHIRCode("denominator").value)
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.as_json(), "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression.value, FHIRString("Denominator").value)
        self.assertEqual(inst.group[0].population[1].criteria.expression.as_json(), "Denominator")
        self.assertEqual(inst.group[0].population[1].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[1].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.value, FHIRCode("numerator").value)
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.as_json(), "numerator")
        self.assertEqual(inst.group[0].population[2].criteria.expression.value, FHIRString("Numerator").value)
        self.assertEqual(inst.group[0].population[2].criteria.expression.as_json(), "Numerator")
        self.assertEqual(inst.group[0].population[2].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[2].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.id.value, FHIRString("component-b-example").value)
        self.assertEqual(inst.id.as_json(), "component-b-example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.scoring.coding[0].code.value, FHIRCode("proportion").value)
        self.assertEqual(inst.scoring.coding[0].code.as_json(), "proportion")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Screening for Depression").value)
        self.assertEqual(inst.title.as_json(), "Screening for Depression")

    def testMeasure4(self):
        inst = self.instantiate_from('measure-component-a-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Measure instance')
        self.implMeasure4(inst)

        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure4(inst2)

    def implMeasure4(self, inst):
        self.assertEqual(inst.group[0].id.value, FHIRString("Main").value)
        self.assertEqual(inst.group[0].id.as_json(), "Main")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.value, FHIRCode("initial-population").value)
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.as_json(), "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression.value, FHIRString("Initial Population").value)
        self.assertEqual(inst.group[0].population[0].criteria.expression.as_json(), "Initial Population")
        self.assertEqual(inst.group[0].population[0].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[0].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.value, FHIRCode("denominator").value)
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.as_json(), "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression.value, FHIRString("Denominator").value)
        self.assertEqual(inst.group[0].population[1].criteria.expression.as_json(), "Denominator")
        self.assertEqual(inst.group[0].population[1].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[1].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.value, FHIRCode("numerator").value)
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.as_json(), "numerator")
        self.assertEqual(inst.group[0].population[2].criteria.expression.value, FHIRString("Numerator").value)
        self.assertEqual(inst.group[0].population[2].criteria.expression.as_json(), "Numerator")
        self.assertEqual(inst.group[0].population[2].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[2].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.id.value, FHIRString("component-a-example").value)
        self.assertEqual(inst.id.as_json(), "component-a-example")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.scoring.coding[0].code.value, FHIRCode("proportion").value)
        self.assertEqual(inst.scoring.coding[0].code.as_json(), "proportion")
        self.assertEqual(inst.status.value, FHIRCode("draft").value)
        self.assertEqual(inst.status.as_json(), "draft")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Screening for Alcohol Misuse").value)
        self.assertEqual(inst.title.as_json(), "Screening for Alcohol Misuse")

    def testMeasure5(self):
        inst = self.instantiate_from('measure-predecessor-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a Measure instance')
        self.implMeasure5(inst)

        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure5(inst2)

    def implMeasure5(self, inst):
        self.assertEqual(inst.date.value, FHIRDateTime("2014-03-08").value)
        self.assertEqual(inst.date.as_json(), "2014-03-08")
        self.assertEqual(inst.description.value, FHIRMarkdown("Exclusive breastfeeding measure of outcomes for exclusive breastmilk feeding of newborns.").value)
        self.assertEqual(inst.description.as_json(), "Exclusive breastfeeding measure of outcomes for exclusive breastmilk feeding of newborns.")
        self.assertEqual(inst.group[0].id.value, FHIRString("PopulationGroup1").value)
        self.assertEqual(inst.group[0].id.as_json(), "PopulationGroup1")
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.value, FHIRCode("initial-population").value)
        self.assertEqual(inst.group[0].population[0].code.coding[0].code.as_json(), "initial-population")
        self.assertEqual(inst.group[0].population[0].criteria.expression.value, FHIRString("InitialPopulation1").value)
        self.assertEqual(inst.group[0].population[0].criteria.expression.as_json(), "InitialPopulation1")
        self.assertEqual(inst.group[0].population[0].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[0].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.value, FHIRCode("denominator").value)
        self.assertEqual(inst.group[0].population[1].code.coding[0].code.as_json(), "denominator")
        self.assertEqual(inst.group[0].population[1].criteria.expression.value, FHIRString("Denominator1").value)
        self.assertEqual(inst.group[0].population[1].criteria.expression.as_json(), "Denominator1")
        self.assertEqual(inst.group[0].population[1].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[1].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.value, FHIRCode("denominator-exclusions").value)
        self.assertEqual(inst.group[0].population[2].code.coding[0].code.as_json(), "denominator-exclusions")
        self.assertEqual(inst.group[0].population[2].criteria.expression.value, FHIRString("DenominatorExclusions1").value)
        self.assertEqual(inst.group[0].population[2].criteria.expression.as_json(), "DenominatorExclusions1")
        self.assertEqual(inst.group[0].population[2].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[2].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[0].population[3].code.coding[0].code.value, FHIRCode("numerator").value)
        self.assertEqual(inst.group[0].population[3].code.coding[0].code.as_json(), "numerator")
        self.assertEqual(inst.group[0].population[3].criteria.expression.value, FHIRString("Numerator1").value)
        self.assertEqual(inst.group[0].population[3].criteria.expression.as_json(), "Numerator1")
        self.assertEqual(inst.group[0].population[3].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[0].population[3].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[1].id.value, FHIRString("PopulationGroup2").value)
        self.assertEqual(inst.group[1].id.as_json(), "PopulationGroup2")
        self.assertEqual(inst.group[1].population[0].code.coding[0].code.value, FHIRCode("initial-population").value)
        self.assertEqual(inst.group[1].population[0].code.coding[0].code.as_json(), "initial-population")
        self.assertEqual(inst.group[1].population[0].criteria.expression.value, FHIRString("InitialPopulation2").value)
        self.assertEqual(inst.group[1].population[0].criteria.expression.as_json(), "InitialPopulation2")
        self.assertEqual(inst.group[1].population[0].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[1].population[0].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[1].population[1].code.coding[0].code.value, FHIRCode("denominator").value)
        self.assertEqual(inst.group[1].population[1].code.coding[0].code.as_json(), "denominator")
        self.assertEqual(inst.group[1].population[1].criteria.expression.value, FHIRString("Denominator2").value)
        self.assertEqual(inst.group[1].population[1].criteria.expression.as_json(), "Denominator2")
        self.assertEqual(inst.group[1].population[1].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[1].population[1].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[1].population[2].code.coding[0].code.value, FHIRCode("denominator-exclusion").value)
        self.assertEqual(inst.group[1].population[2].code.coding[0].code.as_json(), "denominator-exclusion")
        self.assertEqual(inst.group[1].population[2].criteria.expression.value, FHIRString("DenominatorExclusions2").value)
        self.assertEqual(inst.group[1].population[2].criteria.expression.as_json(), "DenominatorExclusions2")
        self.assertEqual(inst.group[1].population[2].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[1].population[2].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.group[1].population[3].code.coding[0].code.value, FHIRCode("numerator").value)
        self.assertEqual(inst.group[1].population[3].code.coding[0].code.as_json(), "numerator")
        self.assertEqual(inst.group[1].population[3].criteria.expression.value, FHIRString("Numerator2").value)
        self.assertEqual(inst.group[1].population[3].criteria.expression.as_json(), "Numerator2")
        self.assertEqual(inst.group[1].population[3].criteria.language.value, FHIRCode("text/cql").value)
        self.assertEqual(inst.group[1].population[3].criteria.language.as_json(), "text/cql")
        self.assertEqual(inst.id.value, FHIRString("measure-predecessor-example").value)
        self.assertEqual(inst.id.as_json(), "measure-predecessor-example")
        self.assertEqual(inst.identifier[0].use.value, FHIRCode("official").value)
        self.assertEqual(inst.identifier[0].use.as_json(), "official")
        self.assertEqual(inst.identifier[0].value.value, FHIRString("exclusive-breastfeeding-measure").value)
        self.assertEqual(inst.identifier[0].value.as_json(), "exclusive-breastfeeding-measure")
        self.assertEqual(inst.improvementNotation.coding[0].code.value, FHIRCode("increase").value)
        self.assertEqual(inst.improvementNotation.coding[0].code.as_json(), "increase")
        self.assertEqual(inst.improvementNotation.coding[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/measure-improvement-notation").value)
        self.assertEqual(inst.improvementNotation.coding[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/measure-improvement-notation")
        self.assertEqual(inst.library[0].value, FHIRCanonical("Library/library-exclusive-breastfeeding-cqm-logic").value)
        self.assertEqual(inst.library[0].as_json(), "Library/library-exclusive-breastfeeding-cqm-logic")
        self.assertEqual(inst.meta.tag[0].code.value, FHIRCode("HTEST").value)
        self.assertEqual(inst.meta.tag[0].code.as_json(), "HTEST")
        self.assertEqual(inst.meta.tag[0].display.value, FHIRString("test health data").value)
        self.assertEqual(inst.meta.tag[0].display.as_json(), "test health data")
        self.assertEqual(inst.meta.tag[0].system.value, FHIRUri("http://terminology.hl7.org/CodeSystem/v3-ActReason").value)
        self.assertEqual(inst.meta.tag[0].system.as_json(), "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.purpose.value, FHIRMarkdown("Measure of newborns who were fed breast milk only since birth").value)
        self.assertEqual(inst.purpose.as_json(), "Measure of newborns who were fed breast milk only since birth")
        self.assertEqual(inst.relatedArtifact[0].citation.value, FHIRMarkdown("American Academy of Pediatrics. (2005). Section on Breastfeeding. Policy Statement:Breastfeeding and the Use of Human Milk. Pediatrics.115:496-506.").value)
        self.assertEqual(inst.relatedArtifact[0].citation.as_json(), "American Academy of Pediatrics. (2005). Section on Breastfeeding. Policy Statement:Breastfeeding and the Use of Human Milk. Pediatrics.115:496-506.")
        self.assertEqual(inst.relatedArtifact[0].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[0].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[1].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[1].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[2].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[2].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[3].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[3].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[4].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[4].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[5].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[5].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[6].citation.value, FHIRMarkdown("Kramer, M.S. & Kakuma, R. (2002).Optimal duration of exclusive breastfeeding. [107 refs] Cochrane Database of Systematic Reviews. (1):CD003517.").value)
        self.assertEqual(inst.relatedArtifact[6].citation.as_json(), "Kramer, M.S. & Kakuma, R. (2002).Optimal duration of exclusive breastfeeding. [107 refs] Cochrane Database of Systematic Reviews. (1):CD003517.")
        self.assertEqual(inst.relatedArtifact[6].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[6].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[7].citation.value, FHIRMarkdown("Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal race/ethnicity and one-month exclusive breastfeeding in association with the in-hospital feeding modality. Breastfeeding Medicine. 2(2):92-8.").value)
        self.assertEqual(inst.relatedArtifact[7].citation.as_json(), "Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal race/ethnicity and one-month exclusive breastfeeding in association with the in-hospital feeding modality. Breastfeeding Medicine. 2(2):92-8.")
        self.assertEqual(inst.relatedArtifact[7].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[7].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[8].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[8].type.as_json(), "documentation")
        self.assertEqual(inst.relatedArtifact[9].type.value, FHIRCode("documentation").value)
        self.assertEqual(inst.relatedArtifact[9].type.as_json(), "documentation")
        self.assertEqual(inst.scoring.coding[0].code.value, FHIRCode("proportion").value)
        self.assertEqual(inst.scoring.coding[0].code.as_json(), "proportion")
        self.assertEqual(inst.status.value, FHIRCode("active").value)
        self.assertEqual(inst.status.as_json(), "active")
        self.assertEqual(inst.text.status.value, FHIRCode("generated").value)
        self.assertEqual(inst.text.status.as_json(), "generated")
        self.assertEqual(inst.title.value, FHIRString("Exclusive Breastfeeding Measure").value)
        self.assertEqual(inst.title.as_json(), "Exclusive Breastfeeding Measure")
        self.assertEqual(inst.topic[0].text.value, FHIRString("Exclusive Breastfeeding").value)
        self.assertEqual(inst.topic[0].text.as_json(), "Exclusive Breastfeeding")
        self.assertEqual(inst.type[0].coding[0].code.value, FHIRCode("process").value)
        self.assertEqual(inst.type[0].coding[0].code.as_json(), "process")
        self.assertEqual(inst.version.value, FHIRString("4.0.1").value)
        self.assertEqual(inst.version.as_json(), "4.0.1")


from fhirclient.models.fhirdatatypes import FHIRCode, FHIRString, FHIRUri, FHIRCanonical, FHIRDate, FHIRDateTime, FHIRMarkdown