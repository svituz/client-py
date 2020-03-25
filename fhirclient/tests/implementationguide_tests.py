#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.1-9346c8cc45 on 2020-03-25.
#  2020, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import implementationguide

class ImplementationGuideTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ImplementationGuide", js["resourceType"])
        return implementationguide.ImplementationGuide(js)

    def testImplementationGuide1(self):
        inst = self.instantiate_from('implementationguide-example.json')
        self.assertIsNotNone(inst, 'Must have instantiated a ImplementationGuide instance')
        self.implImplementationGuide1(inst)

        js = inst.as_json()
        self.assertEqual("ImplementationGuide", js["resourceType"])
        inst2 = implementationguide.ImplementationGuide(js)
        self.implImplementationGuide1(inst2)

    def implImplementationGuide1(self, inst):
        self.assertEqual(inst.contact[0].name.value, FHIRString('ONC').value)
        self.assertEqual(inst.contact[0].name.as_json(), 'ONC')
        self.assertEqual(inst.contact[0].telecom[0].system.value, FHIRCode('url').value)
        self.assertEqual(inst.contact[0].telecom[0].system.as_json(), 'url')
        self.assertEqual(inst.contact[0].telecom[0].value.value, FHIRString('http://www.healthit.gov').value)
        self.assertEqual(inst.contact[0].telecom[0].value.as_json(), 'http://www.healthit.gov')
        self.assertEqual(inst.contact[1].name.value, FHIRString('HL7').value)
        self.assertEqual(inst.contact[1].name.as_json(), 'HL7')
        self.assertEqual(inst.contact[1].telecom[0].system.value, FHIRCode('url').value)
        self.assertEqual(inst.contact[1].telecom[0].system.as_json(), 'url')
        self.assertEqual(inst.contact[1].telecom[0].value.value, FHIRString('http://hl7.org/fhir').value)
        self.assertEqual(inst.contact[1].telecom[0].value.as_json(), 'http://hl7.org/fhir')
        self.assertEqual(inst.copyright.value, FHIRMarkdown('Published by ONC under the standard FHIR license (CC0)').value)
        self.assertEqual(inst.copyright.as_json(), 'Published by ONC under the standard FHIR license (CC0)')
        self.assertEqual(inst.date.value, FHIRDateTime('2015-01-01').value)
        self.assertEqual(inst.date.as_json(), '2015-01-01')
        self.assertEqual(inst.definition.grouping[0].description.value, FHIRString('Base package (not broken up into multiple packages)').value)
        self.assertEqual(inst.definition.grouping[0].description.as_json(), 'Base package (not broken up into multiple packages)')
        self.assertEqual(inst.definition.grouping[0].name.value, FHIRString('test').value)
        self.assertEqual(inst.definition.grouping[0].name.as_json(), 'test')
        self.assertEqual(inst.definition.page.generation.value, FHIRCode('html').value)
        self.assertEqual(inst.definition.page.generation.as_json(), 'html')
        self.assertEqual(inst.definition.page.nameUrl.value, FHIRUrl('patient-example.html').value)
        self.assertEqual(inst.definition.page.nameUrl.as_json(), 'patient-example.html')
        self.assertEqual(inst.definition.page.page[0].generation.value, FHIRCode('html').value)
        self.assertEqual(inst.definition.page.page[0].generation.as_json(), 'html')
        self.assertEqual(inst.definition.page.page[0].nameUrl.value, FHIRUrl('list.html').value)
        self.assertEqual(inst.definition.page.page[0].nameUrl.as_json(), 'list.html')
        self.assertEqual(inst.definition.page.page[0].title.value, FHIRString('Value Set Page').value)
        self.assertEqual(inst.definition.page.page[0].title.as_json(), 'Value Set Page')
        self.assertEqual(inst.definition.page.title.value, FHIRString('Example Patient Page').value)
        self.assertEqual(inst.definition.page.title.as_json(), 'Example Patient Page')
        self.assertEqual(inst.definition.parameter[0].code.value, FHIRCode('apply').value)
        self.assertEqual(inst.definition.parameter[0].code.as_json(), 'apply')
        self.assertEqual(inst.definition.parameter[0].value.value, FHIRString('version').value)
        self.assertEqual(inst.definition.parameter[0].value.as_json(), 'version')
        self.assertEqual(inst.definition.resource[0].description.value, FHIRString('A test example to show how an implementation guide works').value)
        self.assertEqual(inst.definition.resource[0].description.as_json(), 'A test example to show how an implementation guide works')
        self.assertEqual(inst.definition.resource[0].exampleCanonical.value, FHIRCanonical('http://hl7.org/fhir/us/core/StructureDefinition/patient').value)
        self.assertEqual(inst.definition.resource[0].exampleCanonical.as_json(), 'http://hl7.org/fhir/us/core/StructureDefinition/patient')
        self.assertEqual(inst.definition.resource[0].name.value, FHIRString('Test Example').value)
        self.assertEqual(inst.definition.resource[0].name.as_json(), 'Test Example')
        self.assertEqual(inst.dependsOn[0].uri.value, FHIRCanonical('http://hl7.org/fhir/ImplementationGuide/uscore').value)
        self.assertEqual(inst.dependsOn[0].uri.as_json(), 'http://hl7.org/fhir/ImplementationGuide/uscore')
        self.assertFalse(inst.experimental)
        self.assertEqual(inst.fhirVersion[0].value, FHIRCode('4.0.1').value)
        self.assertEqual(inst.fhirVersion[0].as_json(), '4.0.1')
        self.assertEqual(inst.global_fhir[0].profile.value, FHIRCanonical('http://hl7.org/fhir/us/core/StructureDefinition/patient').value)
        self.assertEqual(inst.global_fhir[0].profile.as_json(), 'http://hl7.org/fhir/us/core/StructureDefinition/patient')
        self.assertEqual(inst.global_fhir[0].type.value, FHIRCode('Patient').value)
        self.assertEqual(inst.global_fhir[0].type.as_json(), 'Patient')
        self.assertEqual(inst.jurisdiction[0].coding[0].code.value, FHIRCode('US').value)
        self.assertEqual(inst.jurisdiction[0].coding[0].code.as_json(), 'US')
        self.assertEqual(inst.jurisdiction[0].coding[0].system.value, FHIRUri('urn:iso:std:iso:3166').value)
        self.assertEqual(inst.jurisdiction[0].coding[0].system.as_json(), 'urn:iso:std:iso:3166')
        self.assertEqual(inst.license.value, FHIRCode('CC0-1.0').value)
        self.assertEqual(inst.license.as_json(), 'CC0-1.0')
        self.assertEqual(inst.manifest.image[0].value, FHIRString('fhir.png').value)
        self.assertEqual(inst.manifest.image[0].as_json(), 'fhir.png')
        self.assertEqual(inst.manifest.other[0].value, FHIRString('fhir.css').value)
        self.assertEqual(inst.manifest.other[0].as_json(), 'fhir.css')
        self.assertEqual(inst.manifest.page[0].anchor[0].value, FHIRString('patient-test').value)
        self.assertEqual(inst.manifest.page[0].anchor[0].as_json(), 'patient-test')
        self.assertEqual(inst.manifest.page[0].anchor[1].value, FHIRString('tx').value)
        self.assertEqual(inst.manifest.page[0].anchor[1].as_json(), 'tx')
        self.assertEqual(inst.manifest.page[0].anchor[2].value, FHIRString('uml').value)
        self.assertEqual(inst.manifest.page[0].anchor[2].as_json(), 'uml')
        self.assertEqual(inst.manifest.page[0].name.value, FHIRString('patient-test.html').value)
        self.assertEqual(inst.manifest.page[0].name.as_json(), 'patient-test.html')
        self.assertEqual(inst.manifest.page[0].title.value, FHIRString('Test Patient Example').value)
        self.assertEqual(inst.manifest.page[0].title.as_json(), 'Test Patient Example')
        self.assertEqual(inst.manifest.rendering.value, FHIRUrl('http://hl7.org/fhir/us/daf').value)
        self.assertEqual(inst.manifest.rendering.as_json(), 'http://hl7.org/fhir/us/daf')
        self.assertEqual(inst.manifest.resource[0].exampleCanonical.value, FHIRCanonical('http://hl7.org/fhir/us/core/StructureDefinition/patient').value)
        self.assertEqual(inst.manifest.resource[0].exampleCanonical.as_json(), 'http://hl7.org/fhir/us/core/StructureDefinition/patient')
        self.assertEqual(inst.manifest.resource[0].relativePath.value, FHIRUrl('patient-test.html#patient-test').value)
        self.assertEqual(inst.manifest.resource[0].relativePath.as_json(), 'patient-test.html#patient-test')
        self.assertEqual(inst.name.value, FHIRString('Data Access Framework (DAF)').value)
        self.assertEqual(inst.name.as_json(), 'Data Access Framework (DAF)')
        self.assertEqual(inst.packageId.value, FHIRId('hl7.fhir.us.daf').value)
        self.assertEqual(inst.packageId.as_json(), 'hl7.fhir.us.daf')
        self.assertEqual(inst.publisher.value, FHIRString('ONC / HL7 Joint project').value)
        self.assertEqual(inst.publisher.as_json(), 'ONC / HL7 Joint project')
        self.assertEqual(inst.status.value, FHIRCode('draft').value)
        self.assertEqual(inst.status.as_json(), 'draft')
        self.assertEqual(inst.text.status.value, FHIRCode('generated').value)
        self.assertEqual(inst.text.status.as_json(), 'generated')
        self.assertEqual(inst.url.value, FHIRUri('http://hl7.org/fhir/us/daf').value)
        self.assertEqual(inst.url.as_json(), 'http://hl7.org/fhir/us/daf')
        self.assertEqual(inst.version.value, FHIRString('0').value)
        self.assertEqual(inst.version.as_json(), '0')


from fhirclient.models.fhirdatatypes import FHIRString, FHIRCode, FHIRMarkdown, FHIRDateTime, FHIRUrl, FHIRCanonical, FHIRUri, FHIRId