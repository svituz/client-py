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

class OrganizationType(object):
    """ This example value set defines a set of codes that can be used to indicate a type of organization.
    URL: http://terminology.hl7.org/CodeSystem/organization-type
    ValueSet: http://hl7.org/fhir/ValueSet/organization-type
    """
    """An organization that provides healthcare services."""
    PROV = "prov"
    """A department or ward within a hospital (Generally is not applicable to top level organizations)"""
    DEPT = "dept"
    """An organizational team is usually a grouping of practitioners that perform a specific function within an
	/// organization (which could be a top level organization, or a department)."""
    TEAM = "team"
    """A political body, often used when including organization records for government bodies such as a Federal
	/// Government, State or Local Government."""
    GOVT = "govt"
    """A company that provides insurance to its subscribers that may include healthcare related policies."""
    INS = "ins"
    """A company, charity, or governmental organization, which processes claims and/or issues payments to providers on
	/// behalf of patients or groups of patients."""
    PAY = "pay"
    """An educational institution that provides education or research facilities."""
    EDU = "edu"
    """An organization that is identified as a part of a religious institution."""
    RELI = "reli"
    """An organization that is identified as a Pharmaceutical/Clinical Research Sponsor."""
    CRS = "crs"
    """An un-incorporated community group."""
    CG = "cg"
    """An organization that is a registered business or corporation but not identified by other types."""
    BUS = "bus"
    """Other type of organization not already specified."""
    OTHER = "other"
    allowed_values = ['PROV', 'DEPT', 'TEAM', 'GOVT', 'INS', 'PAY', 'EDU', 'RELI', 'CRS', 'CG', 'BUS', 'OTHER']