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

class Use(object):
    """ The purpose of the Claim: predetermination, preauthorization, claim.
    URL: http://hl7.org/fhir/claim-use
    ValueSet: http://hl7.org/fhir/ValueSet/claim-use
    """
    # The treatment is complete and this represents a Claim for the services.
    claim = "claim"
    # The treatment is proposed and this represents a Pre-authorization for the services.
    preauthorization = "preauthorization"
    # The treatment is proposed and this represents a Pre-determination for the services.
    predetermination = "predetermination"