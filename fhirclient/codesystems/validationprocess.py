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
    """editCheck"""
    EDITCHECK = "edit-check"
    """valueset"""
    VALUESET = "valueset"
    """primary"""
    PRIMARY = "primary"
    """multi"""
    MULTI = "multi"
    """standalone"""
    STANDALONE = "standalone"
    """inContext"""
    INCONTEXT = "in-context"
    allowed_values = ['EDITCHECK', 'VALUESET', 'PRIMARY', 'MULTI', 'STANDALONE', 'INCONTEXT']