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

class SubscriberRelationshipCodes(object):
    """ This value set includes codes for the relationship between the Subscriber and the Beneficiary (insured/covered
party/patient).
    URL: http://terminology.hl7.org/CodeSystem/subscriber-relationship
    ValueSet: http://hl7.org/fhir/ValueSet/subscriber-relationship
    """
    """The Beneficiary is a child of the Subscriber"""
    CHILD = "child"
    """The Beneficiary is a parent of the Subscriber"""
    PARENT = "parent"
    """The Beneficiary is a spouse or equivalent of the Subscriber"""
    SPOUSE = "spouse"
    """The Beneficiary is a common law spouse or equivalent of the Subscriber"""
    COMMON = "common"
    """The Beneficiary has some other relationship the Subscriber"""
    OTHER = "other"
    """The Beneficiary is the Subscriber"""
    SELF = "self"
    """The Beneficiary is covered under insurance of the subscriber due to an injury."""
    INJURED = "injured"
    allowed_values = ['CHILD', 'PARENT', 'SPOUSE', 'COMMON', 'OTHER', 'SELF', 'INJURED']