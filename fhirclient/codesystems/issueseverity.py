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

class IssueSeverity(object):
    """ How the issue affects the success of the action.
    URL: http://hl7.org/fhir/issue-severity
    ValueSet: http://hl7.org/fhir/ValueSet/issue-severity
    """
    """The issue caused the action to fail and no further checking could be performed."""
    FATAL = "fatal"
    """The issue is sufficiently important to cause the action to fail."""
    ERROR = "error"
    """The issue is not important enough to cause the action to fail but may cause it to be performed suboptimally or
	/// in a way that is not as desired."""
    WARNING = "warning"
    """The issue has no relation to the degree of success of the action."""
    INFORMATION = "information"
    allowed_values = ['FATAL', 'ERROR', 'WARNING', 'INFORMATION']