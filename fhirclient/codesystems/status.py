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

class Status(object):
    """ The validation status of the target
    URL: http://hl7.org/fhir/CodeSystem/status
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-status
    """
    """***TODO***"""
    ATTESTED = "attested"
    """***TODO***"""
    VALIDATED = "validated"
    """***TODO***"""
    INPROCESS = "in-process"
    """***TODO***"""
    REQREVALID = "req-revalid"
    """***TODO***"""
    VALFAIL = "val-fail"
    """***TODO***"""
    REVALFAIL = "reval-fail"
    allowed_values = ['ATTESTED', 'VALIDATED', 'INPROCESS', 'REQREVALID', 'VALFAIL', 'REVALFAIL']