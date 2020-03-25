#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR {{ info.version }} on {{ info.date }}.
#  {{ info.year }}, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import {{ class.module }}

{%- set datatypes = ['FHIRBase64Binary', 'FHIRCanonical', 'FHIRCode', 'FHIRDate', 'FHIRDateTime', 'FHIRId', 'FHIRInstant', 'FHIRMarkdown', 'FHIROid', 'FHIRPositiveInt', 'FHIRTime', 'FHIRUnsignedInt', 'FHIRUri', 'FHIRUrl', 'FHIRUuid', 'FHIRString'] %}
{%- set used_datatypes = [] %}

class {{ class.name }}Tests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("{{ class.name }}", js["resourceType"])
        return {{ class.module }}.{{ class.name }}(js)

{%- for tcase in tests %}

    def test{{ class.name }}{{ loop.index }}(self):
        inst = self.instantiate_from('{{ tcase.filename }}')
        self.assertIsNotNone(inst, 'Must have instantiated a {{ class.name }} instance')
        self.impl{{ class.name }}{{ loop.index }}(inst)

        js = inst.as_json()
        self.assertEqual("{{ class.name }}", js["resourceType"])
        inst2 = {{ class.module }}.{{ class.name }}(js)
        self.impl{{ class.name }}{{ loop.index }}(inst2)

    def impl{{ class.name }}{{ loop.index }}(self, inst):
    {%- for onetest in tcase.tests %}
    {%- if "str" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}, '{{ onetest.value|replace('\\n', '\\\\n')|replace("\"", "\"") }}')
    {%- else %}{% if "int" == onetest.klass.name or "float" == onetest.klass.name or "NSDecimalNumber" == onetest.klass.name %}
        self.assertEqual(inst.{{ onetest.path }}, {{ onetest.value }})
    {%- else %}{% if "bool" == onetest.klass.name %}
        {%- if onetest.value %}
        self.assertTrue(inst.{{ onetest.path }})
        {%- else %}
        self.assertFalse(inst.{{ onetest.path }})
        {%- endif %}
        {%- else %}{% if onetest.klass.name in datatypes %}
        {%- if onetest.klass.name not in used_datatypes %}
        {%- set _ = used_datatypes.append(onetest.klass.name) %}
        {%- endif %}

        {%- if onetest.klass.name in ["FHIRPositiveInt", "FHIRUnsignedInt"] %}
        self.assertEqual(inst.{{onetest.path}}.value, {{onetest.klass.name}}('{{ onetest.value }}').value)
        self.assertEqual(inst.{{ onetest.path }}.as_json(), {{ onetest.value }})
        {%- else %}
        self.assertEqual(inst.{{onetest.path}}.value, {{onetest.klass.name}}('{{ onetest.value|escape }}').value)
        self.assertEqual(inst.{{ onetest.path }}.as_json(), '{{ onetest.value|escape }}')
        {%- endif %}

        {%- if onetest.klass.name in ["FHIRDate", "FHIRDatetime", "FHIRInstant", "FHIRTime"] %}
        self.assertEqual(inst.{{ onetest.path }}.date, {{ onetest.klass.name }}('{{ onetest.value }}').date)
        {%- endif %}
    {%- else %}
        # Don't know how to create unit test for "{{ onetest.path }}", which is a {{ onetest.klass.name }}
    {%- endif %}{% endif %}{% endif %}{% endif %}
    {%- endfor %}
{%- endfor %}


from fhirclient.models.fhirdatatypes import {%- for dt in used_datatypes %} {{ dt }}{% if not loop.last %},{% endif %}{%- endfor %}
