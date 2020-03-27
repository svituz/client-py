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

class TestScriptProfileOriginType(object):
    """ This value set defines a set of codes that are used to indicate the profile type of a test system when acting as the
origin within a TestScript.
    URL: http://terminology.hl7.org/CodeSystem/testscript-profile-origin-types
    ValueSet: http://hl7.org/fhir/ValueSet/testscript-profile-origin-types
    """
    # General FHIR client used to initiate operations against a FHIR server.
    fHIRClient = "FHIR-Client"
    # A FHIR client acting as a Structured Data Capture Form Filler.
    fHIRSDCFormFiller = "FHIR-SDC-FormFiller"