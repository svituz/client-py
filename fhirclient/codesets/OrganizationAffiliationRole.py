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

class OrganizationAffiliationRole(object):
    """ This example value set defines a set of codes that can be used to indicate the role of one Organization in relation to
another.
    URL: http://hl7.org/fhir/organization-role
    ValueSet: http://hl7.org/fhir/ValueSet/organization-role
    """
    # provider
    provider = "provider"
    # An organization such as a public health agency, community/social services provider, etc.
    agency = "agency"
    # An organization providing research-related services such as conducting research, recruiting research
	/// participants, analyzing data, etc.
    research = "research"
    # An organization providing reimbursement, payment, or related services
    payer = "payer"
    # An organization providing diagnostic testing/laboratory services
    diagnostics = "diagnostics"
    # An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.)
    supplier = "supplier"
    # An organization that facilitates electronic clinical data exchange between entities
    HIEHIO = "HIE/HIO"
    # A type of non-ownership relationship between entities (encompasses partnerships, collaboration, joint ventures,
	/// etc.)
    member = "member"