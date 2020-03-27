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

class MeasureReportType(object):
    """ The type of the measure report.
    URL: http://hl7.org/fhir/measure-report-type
    ValueSet: http://hl7.org/fhir/ValueSet/measure-report-type
    """
    """An individual report that provides information on the performance for a given measure with respect to a single
	/// subject."""
    INDIVIDUAL = "individual"
    """A subject list report that includes a listing of subjects that satisfied each population criteria in the
	/// measure."""
    SUBJECTLIST = "subject-list"
    """A summary report that returns the number of members in each population criteria for the measure."""
    SUMMARY = "summary"
    """A data collection report that contains data-of-interest for the measure."""
    DATACOLLECTION = "data-collection"
    allowed_values = ['INDIVIDUAL', 'SUBJECTLIST', 'SUMMARY', 'DATACOLLECTION']