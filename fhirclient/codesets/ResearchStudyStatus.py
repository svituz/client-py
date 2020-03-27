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
    # Study is opened for accrual.
    active = "active"
    # Study is completed prematurely and will not resume; patients are no longer examined nor treated.
    administrativelyCompleted = "administratively-completed"
    # Protocol is approved by the review board.
    approved = "approved"
    # Study is closed for accrual; patients can be examined and treated.
    closedToAccrual = "closed-to-accrual"
    # Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment or intervention but are still being followed according to the primary objective of the
	/// study.
    closedToAccrualAndIntervention = "closed-to-accrual-and-intervention"
    # Study is closed to accrual and intervention, i.e. the study is closed to enrollment, all study subjects have
	/// completed treatment
	/// or intervention but are still being followed according to the primary objective of the study.
    completed = "completed"
    # Protocol was disapproved by the review board.
    disapproved = "disapproved"
    # Protocol is submitted to the review board for approval.
    inReview = "in-review"
    # Study is temporarily closed for accrual; can be potentially resumed in the future; patients can be examined and
	/// treated.
    temporarilyClosedToAccrual = "temporarily-closed-to-accrual"
    # Study is temporarily closed for accrual and intervention and potentially can be resumed in the future.
    temporarilyClosedToAccrualAndIntervention = "temporarily-closed-to-accrual-and-intervention"
    # Protocol was withdrawn by the lead organization.
    withdrawn = "withdrawn"