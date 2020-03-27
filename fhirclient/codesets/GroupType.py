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
    # Group contains "person" Patient resources.
    person = "person"
    # Group contains "animal" Patient resources.
    animal = "animal"
    # Group contains healthcare practitioner resources (Practitioner or PractitionerRole).
    practitioner = "practitioner"
    # Group contains Device resources.
    device = "device"
    # Group contains Medication resources.
    medication = "medication"
    # Group contains Substance resources.
    substance = "substance"