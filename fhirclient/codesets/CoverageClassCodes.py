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
    # An employee group
    group = "group"
    # A sub-group of an employee group
    subgroup = "subgroup"
    # A specific suite of benefits.
    plan = "plan"
    # A subset of a specific suite of benefits.
    subplan = "subplan"
    # A class of benefits.
    class_fhir = "class"
    # A subset of a class of benefits.
    subclass = "subclass"
    # A sequence number associated with a short-term continuance of the coverage.
    sequence = "sequence"
    # Pharmacy benefit manager's Business Identification Number.
    rxbin = "rxbin"
    # A Pharmacy Benefit Manager specified Processor Control Number.
    rxpcn = "rxpcn"
    # A Pharmacy Benefit Manager specified Member ID.
    rxid = "rxid"
    # A Pharmacy Benefit Manager specified Group number.
    rxgroup = "rxgroup"