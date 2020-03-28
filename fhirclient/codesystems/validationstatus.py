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

class ValidationStatus(object):
    """ Status of the validation of the target against the primary source
    URL: http://terminology.hl7.org/CodeSystem/validation-status
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-validation-status
    """
    # successful
    SUCCESSFUL = "successful"
    # failed
    FAILED = "failed"
    # The validations status has not been determined yet
    UNKNOWN = "unknown"

    allowed_values = [SUCCESSFUL, FAILED, UNKNOWN]