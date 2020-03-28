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

class PractitionerRole(object):
    """ This example value set defines a set of codes that can be used to indicate the role of a Practitioner.
    URL: http://terminology.hl7.org/CodeSystem/practitioner-role
    """
    # A qualified/registered medical practitioner
    DOCTOR = "doctor"
    # A practitioner with nursing experience that may be qualified/registered
    NURSE = "nurse"
    # A qualified/registered/licensed pharmacist
    PHARMACIST = "pharmacist"
    # A practitioner that may perform research
    RESEARCHER = "researcher"
    # Someone who is able to provide educational services
    TEACHER = "teacher"
    # Someone who is qualified in Information and Communication Technologies
    ICT = "ict"

    allowed_values = [DOCTOR, NURSE, PHARMACIST, RESEARCHER, TEACHER, ICT]