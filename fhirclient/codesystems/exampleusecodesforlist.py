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

class ExampleUseCodesForList(object):
    """ Example use codes for the List resource - typical kinds of use.
    URL: http://terminology.hl7.org/CodeSystem/list-example-use-codes
    ValueSet: http://hl7.org/fhir/ValueSet/list-example-codes
    """
    """A list of alerts for the patient."""
    ALERTS = "alerts"
    """A list of part adverse reactions."""
    ADVERSERXNS = "adverserxns"
    """A list of Allergies for the patient."""
    ALLERGIES = "allergies"
    """A list of medication statements for the patient."""
    MEDICATIONS = "medications"
    """A list of problems that the patient is known of have (or have had in the past)."""
    PROBLEMS = "problems"
    """A list of items that constitute a set of work to be performed (typically this code would be specialized for more
	/// specific uses, such as a ward round list)."""
    WORKLIST = "worklist"
    """A list of items waiting for an event (perhaps a surgical patient waiting list)."""
    WAITING = "waiting"
    """A set of protocols to be followed."""
    PROTOCOLS = "protocols"
    """A set of care plans that apply in a particular context of care."""
    PLANS = "plans"
    allowed_values = ['ALERTS', 'ADVERSERXNS', 'ALLERGIES', 'MEDICATIONS', 'PROBLEMS', 'WORKLIST', 'WAITING', 'PROTOCOLS', 'PLANS']