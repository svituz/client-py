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

class ClaimProcessingCodes(object):
    """ This value set includes Claim Processing Outcome codes.
    URL: http://hl7.org/fhir/remittance-outcome
    ValueSet: http://hl7.org/fhir/ValueSet/remittance-outcome
    """
    """The Claim/Pre-authorization/Pre-determination has been received but processing has not begun."""
    QUEUED = "queued"
    """The processing has completed without errors"""
    COMPLETE = "complete"
    """One or more errors have been detected in the Claim"""
    ERROR = "error"
    """No errors have been detected in the Claim and some of the adjudication has been performed."""
    PARTIAL = "partial"
    allowed_values = ['QUEUED', 'COMPLETE', 'ERROR', 'PARTIAL']