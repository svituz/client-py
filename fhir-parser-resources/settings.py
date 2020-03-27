# These are settings for the FHIR class generator.
# All paths are relative to the `fhir-parser` directory. You may want to use
# os.path.join() if the generator should work on Windows, too.
import os

from Default.settings import *

classmap = {
    'Any': 'Resource',
    'Practitioner.role': 'PractRole',   # to avoid Practinioner.role and PractitionerRole generating the same class
    'base64Binary': 'FHIRBase64Binary',
    'boolean': 'bool',
    'canonical': 'FHIRCanonical',
    'code': 'FHIRCode',      # for now we're not generating enums for these
    'date': 'FHIRDate',
    'dateTime': 'FHIRDateTime',
    'decimal': 'float',
    'id': 'FHIRId',
    'instant': 'FHIRInstant',
    'integer': 'int',
    'markdown': 'FHIRMarkdown',
    'oid': 'FHIROid',
    'positiveInt': 'FHIRPositiveInt',
    'string': 'FHIRString',
    'time': 'FHIRTime',
    'unsignedInt': 'FHIRUnsignedInt',
    'uri': 'FHIRUri',
    'url': 'FHIRUrl',
    'uuid': 'FHIRUuid',
    'xhtml': 'FHIRString',
}

jsonmap = {
    'str': 'str',
    'int': 'int',
    'bool': 'bool',
    'float': 'float',
    'FHIRBase64Binary': 'str',
    'FHIRCanonical': 'str',
    'FHIRCode': 'str',
    'FHIRDate': 'str',
    'FHIRDateTime': 'str',
    'FHIRId': 'str',
    'FHIRInstant': 'str',
    'FHIRMarkdown': 'str',
    'FHIROid': 'str',
    'FHIRPositiveInt': 'int',
    'FHIRTime': 'str',
    'FHIRUnsignedInt': 'int',
    'FHIRUri': 'str',
    'FHIRUrl': 'str',
    'FHIRUuid': 'str',
    'FHIRString': 'str'
}

# Base URL for where to load specification data from
specification_url = 'http://hl7.org/fhir/R4'

# In which directory to find the templates. See below for settings that start with `tpl_`: these are the template names.
tpl_base = '../client-py/fhir-parser-resources'
base_dir = '../client-py/fhirclient/models/'
test_dir = '../client-py/fhirclient/tests/'
codesystem_dir = '../client-py/fhirclient/codesystems/'
# classes/resources
write_resources = True
tpl_resource_target = base_dir    # target directory to write the generated class files to
tpl_codesystems_target = codesystem_dir    # target directory to write the generated class files to
tpl_codesystems_source = 'template-codesystems.py'    # the template to use as source when writing enums for CodeSystems; can be `None`
tpl_codesystems_target_ptrn = '{}.py'
# tpl_codesystems_source = os.path.join(tpl_base, 'template_codesystems.py')     # the template to use as source when writing enums for CodeSystems; can be `None`

# factory methods
write_factory = True
tpl_factory_target = f'{base_dir}/fhirelementfactory.py'    # where to write the generated factory to

# unit tests
write_unittests = True
tpl_unittest_target = test_dir    # target directory to write the generated unit test files to

base_module = 'fhirclient'
base_models_module = f"{base_module}.models"
base_datatypes_module = f"{base_module}.models"
codeset_module = f"{base_module}.codesystems"

manual_profiles = [
    ('../client-py/fhir-parser-resources/fhirdatatypes.py', base_datatypes_module, 'fhirdatatypes', [
        'base64Binary', 'boolean', 'canonical', 'code', 'date', 'dateTime',
        'decimal', 'id', 'instant', 'integer', 'markdown', 'oid',
        'positiveInt', 'string', 'time', 'unsignedInt', 'uri', 'url', 'uuid'
    ]),
    ('../client-py/fhir-parser-resources/fhirabstractbase.py', base_models_module, 'fhirabstractbase', [
        'FHIRAbstractBase',
    ]),
    ('../client-py/fhir-parser-resources/fhirabstractresource.py', base_models_module, 'fhirabstractresource',
        ['FHIRAbstractResource']),
    ('../client-py/fhir-parser-resources/fhirreference.py', base_models_module, 'fhirreference', ['FHIRReference']),
    ('../client-py/fhir-parser-resources/fhirsearch.py', base_models_module, 'fhirsearch', ['FHIRSearch']),
]