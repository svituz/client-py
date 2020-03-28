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

class ExampleClaimSubTypeCodes(object):
    """ This value set includes sample Claim SubType codes which are used to distinguish the claim types for example within type
institutional there may be subtypes for emergency services, bed stay and transportation.
    URL: http://terminology.hl7.org/CodeSystem/ex-claimsubtype
    ValueSet: http://hl7.org/fhir/ValueSet/claim-subtype
    """
    # A claim for Orthodontic Services.
    ORTHO = "ortho"
    # A claim for emergency services.
    EMERGENCY = "emergency"

    allowed_values = [ORTHO, EMERGENCY]