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

class DiagnosticReportStatus(object):
    """ The status of the diagnostic report.
    URL: http://hl7.org/fhir/diagnostic-report-status
    ValueSet: http://hl7.org/fhir/ValueSet/diagnostic-report-status
    """
    # The existence of the report is registered, but there is nothing yet available.
    REGISTERED = "registered"
    # This is a partial (e.g. initial, interim or preliminary) report: data in the report may be incomplete or
    # unverified.
    PARTIAL = "partial"
    # Verified early results are available, but not all  results are final.
    PRELIMINARY = "preliminary"
    # The report is complete and verified by an authorized person.
    FINAL = "final"
    # Subsequent to being final, the report has been modified.  This includes any change in the results, diagnosis,
    # narrative text, or other content of a report that has been issued.
    AMENDED = "amended"
    # Subsequent to being final, the report has been modified  to correct an error in the report or referenced
    # results.
    CORRECTED = "corrected"
    # Subsequent to being final, the report has been modified by adding new content. The existing content is
    # unchanged.
    APPENDED = "appended"
    # The report is unavailable because the measurement was not started or not completed (also sometimes called
    # "aborted").
    CANCELLED = "cancelled"
    # The report has been withdrawn following a previous final release.  This electronic record should never have
    # existed, though it is possible that real-world decisions were based on it. (If real-world activity has occurred,
    # the status should be "cancelled" rather than "entered-in-error".).
    ENTEREDINERROR = "entered-in-error"
    # The authoring/source system does not know which of the status values currently applies for this observation.
    # Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the
    # authoring/source system does not know which.
    UNKNOWN = "unknown"

    allowed_values = [REGISTERED, PARTIAL, PRELIMINARY, FINAL, AMENDED, CORRECTED, APPENDED, CANCELLED, ENTEREDINERROR, UNKNOWN]