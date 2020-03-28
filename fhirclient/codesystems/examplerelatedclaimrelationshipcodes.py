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

class ExampleRelatedClaimRelationshipCodes(object):
    """ This value set includes sample Related Claim Relationship codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-relatedclaimrelationship
    ValueSet: http://hl7.org/fhir/ValueSet/related-claim-relationship
    """
    # A prior claim instance for the same intended suite of services.
    PRIOR = "prior"
    # A claim for a different suite of services which is related the suite claimed here.
    ASSOCIATED = "associated"

    allowed_values = [PRIOR, ASSOCIATED]