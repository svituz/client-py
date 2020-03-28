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

class MedicationrequestStatus(object):
    """ MedicationRequest Status Codes
    URL: http://hl7.org/fhir/CodeSystem/medicationrequest-status
    ValueSet: http://hl7.org/fhir/ValueSet/medicationrequest-status
    """
    # The prescription is 'actionable', but not all actions that are implied by it have occurred yet.
    ACTIVE = "active"
    # Actions implied by the prescription are to be temporarily halted, but are expected to continue later.  May also
    # be called 'suspended'.
    ONHOLD = "on-hold"
    # The prescription has been withdrawn before any administrations have occurred
    CANCELLED = "cancelled"
    # All actions that are implied by the prescription have occurred.
    COMPLETED = "completed"
    # Some of the actions that are implied by the medication request may have occurred.  For example, the medication
    # may have been dispensed and the patient may have taken some of the medication.  Clinical decision support
    # systems should take this status into account
    ENTEREDINERROR = "entered-in-error"
    # Actions implied by the prescription are to be permanently halted, before all of the administrations occurred.
    # This should not be used if the original order was entered in error
    STOPPED = "stopped"
    # The prescription is not yet 'actionable', e.g. it is a work in progress, requires sign-off,
    # verification or needs to be run through decision support process.
    DRAFT = "draft"
    # The authoring/source system does not know which of the status values currently applies for this observation.
    # Note: This concept is not to be used for 'other' - one of the listed statuses is presumed to apply, but the
    # authoring/source system does not know which.
    UNKNOWN = "unknown"

    allowed_values = [ACTIVE, ONHOLD, CANCELLED, COMPLETED, ENTEREDINERROR, STOPPED, DRAFT, UNKNOWN]