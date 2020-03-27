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

class TestReportActionResult(object):
    """ The results of executing an action.
    URL: http://hl7.org/fhir/report-action-result-codes
    ValueSet: http://hl7.org/fhir/ValueSet/report-action-result-codes
    """
    """The action was successful."""
    PASS = "pass"
    """The action was skipped."""
    SKIP = "skip"
    """The action failed."""
    FAIL = "fail"
    """The action passed but with warnings."""
    WARNING = "warning"
    """The action encountered a fatal error and the engine was unable to process."""
    ERROR = "error"
    allowed_values = ['PASS', 'SKIP', 'FAIL', 'WARNING', 'ERROR']