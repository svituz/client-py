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

class ExceptionCodes(object):
    """ This value set includes sample Exception codes.
    URL: http://terminology.hl7.org/CodeSystem/claim-exception
    ValueSet: http://hl7.org/fhir/ValueSet/claim-exception
    """
    # Fulltime Student
    STUDENT = "student"
    # Disabled
    DISABLED = "disabled"

    allowed_values = [STUDENT, DISABLED]