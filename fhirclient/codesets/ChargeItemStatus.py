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

class ChargeItemStatus(object):
    """ Codes identifying the lifecycle stage of a ChargeItem.
    URL: http://hl7.org/fhir/chargeitem-status
    ValueSet: http://hl7.org/fhir/ValueSet/chargeitem-status
    """
    # The charge item has been entered, but the charged service is not  yet complete, so it shall not be billed yet
	/// but might be used in the context of pre-authorization.
    planned = "planned"
    # The charge item is ready for billing.
    billable = "billable"
    # The charge item has been determined to be not billable (e.g. due to rules associated with the billing code).
    notBillable = "not-billable"
    # The processing of the charge was aborted.
    aborted = "aborted"
    # The charge item has been billed (e.g. a billing engine has generated financial transactions by applying the
	/// associated ruled for the charge item to the context of the Encounter, and placed them into Claims/Invoices.
    billed = "billed"
    # The charge item has been entered in error and should not be processed for billing.
    enteredInError = "entered-in-error"
    # The authoring system does not know which of the status values currently applies for this charge item  Note: This
	/// concept is not to be used for "other" - one of the listed statuses is presumed to apply, it's just not known
	/// which one.
    unknown = "unknown"