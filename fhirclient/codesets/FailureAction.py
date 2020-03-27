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

class FailureAction(object):
    """ The result if validation fails
    URL: http://terminology.hl7.org/CodeSystem/failure-action
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-failure-action
    """
    # fatal
    fatal = "fatal"
    # warn
    warn = "warn"
    # recOnly
    recOnly = "rec-only"
    # none
    none = "none"