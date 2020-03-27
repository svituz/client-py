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

class ResearchStudyStatus(object):
    """ Codes that convey the current status of the research study.
    URL: http://hl7.org/fhir/research-study-status
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-status
    """
    """Study is opened for accrual."""
    ACTIVE = "active"
    """Study is completed prematurely and will not resume; patients are no longer examined nor treated."""
    ADMINISTRATIVELYCOMPLETED = "administratively-completed"
    """Protocol is approved by the review board."""
    APPROVED = "approved"
    """Study is closed for accrual; patients can be examined and treated."""
    CLOSEDTOACCRUAL = "closed-to-accrual"
    """Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment or intervention but are still being followed according to the primary objective of the
	/// study."""
    CLOSEDTOACCRUALANDINTERVENTION = "closed-to-accrual-and-intervention"
    """Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment
	/// or intervention but are still being followed according to the primary objective of the study."""
    COMPLETED = "completed"
    """Protocol was disapproved by the review board."""
    DISAPPROVED = "disapproved"
    """Protocol is submitted to the review board for approval."""
    INREVIEW = "in-review"
    """Study is temporarily closed for accrual; can be potentially resumed in the future; patients can be examined and
	/// treated."""
    TEMPORARILYCLOSEDTOACCRUAL = "temporarily-closed-to-accrual"
    """Study is temporarily closed for accrual and intervention and potentially can be resumed in the future."""
    TEMPORARILYCLOSEDTOACCRUALANDINTERVENTION = "temporarily-closed-to-accrual-and-intervention"
    """Protocol was withdrawn by the lead organization."""
    WITHDRAWN = "withdrawn"
    allowed_values = ['ACTIVE', 'ADMINISTRATIVELYCOMPLETED', 'APPROVED', 'CLOSEDTOACCRUAL', 'CLOSEDTOACCRUALANDINTERVENTION', 'COMPLETED', 'DISAPPROVED', 'INREVIEW', 'TEMPORARILYCLOSEDTOACCRUAL', 'TEMPORARILYCLOSEDTOACCRUALANDINTERVENTION', 'WITHDRAWN']