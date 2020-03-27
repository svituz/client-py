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

class ValidationProcess(object):
    """ The primary process by which the target is validated
    URL: http://terminology.hl7.org/CodeSystem/validation-process
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-validation-process
    """
    # editCheck
    editCheck = "edit-check"
    # valueset
    valueset = "valueset"
    # primary
    primary = "primary"
    # multi
    multi = "multi"
    # standalone
    standalone = "standalone"
    # inContext
    inContext = "in-context"