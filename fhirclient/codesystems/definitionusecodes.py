#
#  CodeSystems.py
#  client-py
#
#  Generated from FHIR 4.0.1-9346c8cc45
#  2020, SMART Health IT.
#
#  THIS HAS BEEN ADAPTED FROM Swift Enums WITHOUT EVER BEING IMPLEMENTED IN
#  Python, FOR DEMONSTRATION PURPOSES ONLY.
#

class DefinitionUseCodes(object):
    """ Structure Definition Use Codes / Keywords
    URL: http://terminology.hl7.org/CodeSystem/definition-use
    ValueSet: http://hl7.org/fhir/ValueSet/definition-use
    """
    # This structure is defined as part of the base FHIR Specification
    FHIRSTRUCTURE = "fhir-structure"
    # This structure is intended to be treated like a FHIR resource (e.g. on the FHIR API)
    CUSTOMRESOURCE = "custom-resource"
    # This structure captures an analysis of a domain
    DAM = "dam"
    # This structure represents and existing structure (e.g. CDA, HL7 v2)
    WIREFORMAT = "wire-format"
    # This structure captures an analysis of a domain
    ARCHETYPE = "archetype"
    # This structure is a template (n.b: 'template' has many meanings)
    TEMPLATE = "template"

    allowed_values = [FHIRSTRUCTURE, CUSTOMRESOURCE, DAM, WIREFORMAT, ARCHETYPE, TEMPLATE]