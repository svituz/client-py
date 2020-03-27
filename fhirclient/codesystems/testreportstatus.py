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

class TestReportStatus(object):
    """ The current status of the test report.
    URL: http://hl7.org/fhir/report-status-codes
    ValueSet: http://hl7.org/fhir/ValueSet/report-status-codes
    """
    """All test operations have completed."""
    COMPLETED = "completed"
    """A test operations is currently executing."""
    INPROGRESS = "in-progress"
    """A test operation is waiting for an external client request."""
    WAITING = "waiting"
    """The test script execution was manually stopped."""
    STOPPED = "stopped"
    """This test report was entered or created in error."""
    ENTEREDINERROR = "entered-in-error"
    allowed_values = ['COMPLETED', 'INPROGRESS', 'WAITING', 'STOPPED', 'ENTEREDINERROR']