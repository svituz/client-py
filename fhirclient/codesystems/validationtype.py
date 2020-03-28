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

class ValidationType(object):
    """ What the target is validated against
    URL: http://terminology.hl7.org/CodeSystem/validation-type
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-validation-type
    """
    # nothing
    NOTHING = "nothing"
    # primary
    PRIMARY = "primary"
    # multiple
    MULTIPLE = "multiple"

    allowed_values = [NOTHING, PRIMARY, MULTIPLE]