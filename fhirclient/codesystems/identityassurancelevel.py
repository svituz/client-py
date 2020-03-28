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

class IdentityAssuranceLevel(object):
    """ The level of confidence that this link represents the same actual person, based on NIST Authentication Levels.
    URL: http://hl7.org/fhir/identity-assuranceLevel
    ValueSet: http://hl7.org/fhir/ValueSet/identity-assuranceLevel
    """
    # Little or no confidence in the asserted identity's accuracy.
    LEVEL1 = "level1"
    # Some confidence in the asserted identity's accuracy.
    LEVEL2 = "level2"
    # High confidence in the asserted identity's accuracy.
    LEVEL3 = "level3"
    # Very high confidence in the asserted identity's accuracy.
    LEVEL4 = "level4"

    allowed_values = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]