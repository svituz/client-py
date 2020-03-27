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

class MedicationAdministrationPerformerFunctionCodes(object):
    """ MedicationAdministration Performer Function Codes
    URL: http://terminology.hl7.org/CodeSystem/med-admin-perform-function
    ValueSet: http://hl7.org/fhir/ValueSet/med-admin-perform-function
    """
    # A person, non-person living subject, organization or device that who actually and principally carries out the
	/// action
    performer = "performer"
    # A person who verifies the correctness and appropriateness of the service (plan, order, event, etc.) and hence
	/// takes on accountability.
    verifier = "verifier"
    # A person witnessing the action happening without doing anything. A witness is not necessarily aware, much less
	/// approves of anything stated in the service event. Example for a witness is students watching an operation or an
	/// advanced directive witness.
    witness = "witness"