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

class SupplyDeliveryStatus(object):
    """ Status of the supply delivery.
    URL: http://hl7.org/fhir/supplydelivery-status
    ValueSet: http://hl7.org/fhir/ValueSet/supplydelivery-status
    """
    # Supply has been requested, but not delivered.
    inProgress = "in-progress"
    # Supply has been delivered ("completed").
    completed = "completed"
    # Delivery was not completed.
    abandoned = "abandoned"
    # This electronic record should never have existed, though it is possible that real-world decisions were based on
	/// it. (If real-world activity has occurred, the status should be "abandoned" rather than "entered-in-error".).
    enteredInError = "entered-in-error"