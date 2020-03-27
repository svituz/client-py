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

class ClaimCareTeamRoleCodes(object):
    """ This value set includes sample Claim Care Team Role codes.
    URL: http://terminology.hl7.org/CodeSystem/claimcareteamrole
    ValueSet: http://hl7.org/fhir/ValueSet/claim-careteamrole
    """
    # The primary care provider.
    primary = "primary"
    # Assisting care provider.
    assist = "assist"
    # Supervising care provider.
    supervisor = "supervisor"
    # Other role on the care team.
    other = "other"