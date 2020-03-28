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

class MedicationRequestCourseOfTherapyCodes(object):
    """ MedicationRequest Course of Therapy Codes
    URL: http://terminology.hl7.org/CodeSystem/medicationrequest-course-of-therapy
    ValueSet: http://hl7.org/fhir/ValueSet/medicationrequest-course-of-therapy
    """
    # A medication which is expected to be continued beyond the present order and which the patient should be assumed
    # to be taking unless explicitly stopped.
    CONTINUOUS = "continuous"
    # A medication which the patient is only expected to consume for the duration of the current order and which is
    # not expected to be renewed.
    ACUTE = "acute"
    # A medication which is expected to be used on a part time basis at certain times of the year
    SEASONAL = "seasonal"

    allowed_values = [CONTINUOUS, ACUTE, SEASONAL]