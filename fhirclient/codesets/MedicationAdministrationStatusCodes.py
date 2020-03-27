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

class MedicationAdministrationStatusCodes(object):
    """ MedicationAdministration Status Codes
    URL: http://terminology.hl7.org/CodeSystem/medication-admin-status
    ValueSet: http://hl7.org/fhir/ValueSet/medication-admin-status
    """
    # The administration has started but has not yet completed.
    inProgress = "in-progress"
    # The administration was terminated prior to any impact on the subject (though preparatory actions may have been
	/// taken)
    notDone = "not-done"
    # Actions implied by the administration have been temporarily halted, but are expected to continue later. May also
	/// be called 'suspended'.
    onHold = "on-hold"
    # All actions that are implied by the administration have occurred.
    completed = "completed"
    # The administration was entered in error and therefore nullified.
    enteredInError = "entered-in-error"
    # Actions implied by the administration have been permanently halted, before all of them occurred.
    stopped = "stopped"
    # The authoring system does not know which of the status values currently applies for this request. Note: This
	/// concept is not to be used for 'other' - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    unknown = "unknown"