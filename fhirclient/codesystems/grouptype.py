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

class GroupType(object):
    """ Types of resources that are part of group.
    URL: http://hl7.org/fhir/group-type
    ValueSet: http://hl7.org/fhir/ValueSet/group-type
    """
    """Group contains "person" Patient resources."""
    PERSON = "person"
    """Group contains "animal" Patient resources."""
    ANIMAL = "animal"
    """Group contains healthcare practitioner resources (Practitioner or PractitionerRole)."""
    PRACTITIONER = "practitioner"
    """Group contains Device resources."""
    DEVICE = "device"
    """Group contains Medication resources."""
    MEDICATION = "medication"
    """Group contains Substance resources."""
    SUBSTANCE = "substance"
    allowed_values = ['PERSON', 'ANIMAL', 'PRACTITIONER', 'DEVICE', 'MEDICATION', 'SUBSTANCE']