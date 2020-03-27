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

class MedicationDispenseStatusCodes(object):
    """ MedicationDispense Status Codes
    URL: http://terminology.hl7.org/CodeSystem/medicationdispense-status
    ValueSet: http://hl7.org/fhir/ValueSet/medicationdispense-status
    """
    # The core event has not started yet, but some staging activities have begun (e.g. initial compounding or
	/// packaging of medication). Preparation stages may be tracked for billing purposes.
    preparation = "preparation"
    # The dispensed product is ready for pickup.
    inProgress = "in-progress"
    # The dispensed product was not and will never be picked up by the patient.
    cancelled = "cancelled"
    # The dispense process is paused while waiting for an external event to reactivate the dispense.  For example, new
	/// stock has arrived or the prescriber has called.
    onHold = "on-hold"
    # The dispensed product has been picked up.
    completed = "completed"
    # The dispense was entered in error and therefore nullified.
    enteredInError = "entered-in-error"
    # Actions implied by the dispense have been permanently halted, before all of them occurred.
    stopped = "stopped"
    # The dispense was declined and not performed.
    declined = "declined"
    # The authoring system does not know which of the status values applies for this medication dispense.  Note: this
	/// concept is not to be used for other - one of the listed statuses is presumed to apply, it's just now known which
	/// one.
    unknown = "unknown"