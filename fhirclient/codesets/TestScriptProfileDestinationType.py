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

class TestScriptProfileDestinationType(object):
    """ This value set defines a set of codes that are used to indicate the profile type of a test system when acting as the
destination within a TestScript.
    URL: http://terminology.hl7.org/CodeSystem/testscript-profile-destination-types
    ValueSet: http://hl7.org/fhir/ValueSet/testscript-profile-destination-types
    """
    # General FHIR server used to respond to operations sent from a FHIR client.
    fHIRServer = "FHIR-Server"
    # A FHIR server acting as a Structured Data Capture Form Manager.
    fHIRSDCFormManager = "FHIR-SDC-FormManager"
    # A FHIR server acting as a Structured Data Capture Form Processor.
    fHIRSDCFormProcessor = "FHIR-SDC-FormProcessor"
    # A FHIR server acting as a Structured Data Capture Form Receiver.
    fHIRSDCFormReceiver = "FHIR-SDC-FormReceiver"