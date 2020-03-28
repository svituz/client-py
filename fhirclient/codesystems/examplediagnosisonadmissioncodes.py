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

class ExampleDiagnosisOnAdmissionCodes(object):
    """ This value set includes example Diagnosis on Admission codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-diagnosis-on-admission
    ValueSet: http://hl7.org/fhir/ValueSet/ex-diagnosis-on-admission
    """
    # Diagnosis was present at time of inpatient admission.
    Y = "y"
    # Diagnosis was not present at time of inpatient admission.
    N = "n"
    # Documentation insufficient to determine if condition was present at the time of inpatient admission.
    U = "u"
    # Clinically undetermined. Provider unable to clinically determine whether the condition was present at the time
    # of inpatient admission.
    W = "w"

    allowed_values = [Y, N, U, W]