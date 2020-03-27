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

class DeviceUseStatementStatus(object):
    """ A coded concept indicating the current status of the Device Usage.
    URL: http://hl7.org/fhir/device-statement-status
    ValueSet: http://hl7.org/fhir/ValueSet/device-statement-status
    """
    # The device is still being used.
    active = "active"
    # The device is no longer being used.
    completed = "completed"
    # The statement was recorded incorrectly.
    enteredInError = "entered-in-error"
    # The device may be used at some time in the future.
    intended = "intended"
    # Actions implied by the statement have been permanently halted, before all of them occurred.
    stopped = "stopped"
    # Actions implied by the statement have been temporarily halted, but are expected to continue later. May also be
	/// called "suspended".
    onHold = "on-hold"