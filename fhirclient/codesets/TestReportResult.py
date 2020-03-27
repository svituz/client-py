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

class TestReportResult(object):
    """ The reported execution result.
    URL: http://hl7.org/fhir/report-result-codes
    ValueSet: http://hl7.org/fhir/ValueSet/report-result-codes
    """
    # All test operations successfully passed all asserts.
    pass = "pass"
    # One or more test operations failed one or more asserts.
    fail = "fail"
    # One or more test operations is pending execution completion.
    pending = "pending"