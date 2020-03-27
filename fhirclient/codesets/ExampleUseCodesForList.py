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
    # A list of alerts for the patient.
    alerts = "alerts"
    # A list of part adverse reactions.
    adverserxns = "adverserxns"
    # A list of Allergies for the patient.
    allergies = "allergies"
    # A list of medication statements for the patient.
    medications = "medications"
    # A list of problems that the patient is known of have (or have had in the past).
    problems = "problems"
    # A list of items that constitute a set of work to be performed (typically this code would be specialized for more
	/// specific uses, such as a ward round list).
    worklist = "worklist"
    # A list of items waiting for an event (perhaps a surgical patient waiting list).
    waiting = "waiting"
    # A set of protocols to be followed.
    protocols = "protocols"
    # A set of care plans that apply in a particular context of care.
    plans = "plans"