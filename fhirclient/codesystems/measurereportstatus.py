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

class MeasureReportStatus(object):
    """ The status of the measure report.
    URL: http://hl7.org/fhir/measure-report-status
    ValueSet: http://hl7.org/fhir/ValueSet/measure-report-status
    """
    """The report is complete and ready for use."""
    COMPLETE = "complete"
    """The report is currently being generated."""
    PENDING = "pending"
    """An error occurred attempting to generate the report."""
    ERROR = "error"
    allowed_values = ['COMPLETE', 'PENDING', 'ERROR']