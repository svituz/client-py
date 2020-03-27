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

class CoverageClassCodes(object):
    """ This value set includes Coverage Class codes.
    URL: http://terminology.hl7.org/CodeSystem/coverage-class
    ValueSet: http://hl7.org/fhir/ValueSet/coverage-class
    """
    """An employee group"""
    GROUP = "group"
    """A sub-group of an employee group"""
    SUBGROUP = "subgroup"
    """A specific suite of benefits."""
    PLAN = "plan"
    """A subset of a specific suite of benefits."""
    SUBPLAN = "subplan"
    """A class of benefits."""
    CLASS_FHIR = "class"
    """A subset of a class of benefits."""
    SUBCLASS = "subclass"
    """A sequence number associated with a short-term continuance of the coverage."""
    SEQUENCE = "sequence"
    """Pharmacy benefit manager's Business Identification Number."""
    RXBIN = "rxbin"
    """A Pharmacy Benefit Manager specified Processor Control Number."""
    RXPCN = "rxpcn"
    """A Pharmacy Benefit Manager specified Member ID."""
    RXID = "rxid"
    """A Pharmacy Benefit Manager specified Group number."""
    RXGROUP = "rxgroup"
    allowed_values = ['GROUP', 'SUBGROUP', 'PLAN', 'SUBPLAN', 'CLASS_FHIR', 'SUBCLASS', 'SEQUENCE', 'RXBIN', 'RXPCN', 'RXID', 'RXGROUP']