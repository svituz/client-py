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

class ListEmptyReasons(object):
    """ General reasons for a list to be empty. Reasons are either related to a summary list (i.e. problem or medication list)
or to a workflow related list (i.e. consultation list).
    URL: http://terminology.hl7.org/CodeSystem/list-empty-reason
    ValueSet: http://hl7.org/fhir/ValueSet/list-empty-reason
    """
    # Clinical judgment that there are no known items for this list after reasonable investigation. Note that this a
    # positive statement by a clinical user, and not a default position asserted by a computer system in the lack of
    # other information. Example uses:  * For allergies: the patient or patient's agent/guardian has asserted that
    # he/she is not aware of any allergies (NKA - nil known allergies)  * For medications: the patient or patient's
    # agent/guardian has asserted that the patient is known to be taking no medications  * For diagnoses, problems and
    # procedures: the patient or patient's agent/guardian has asserted that there is no known event to record.
    NILKNOWN = "nilknown"
    # The investigation to find out whether there are items for this list has not occurred.
    NOTASKED = "notasked"
    # The content of the list was not provided due to privacy or confidentiality concerns. Note that it should not be
    # assumed that this means that the particular information in question was withheld due to its contents - it can
    # also be a policy decision.
    WITHHELD = "withheld"
    # Information to populate this list cannot be obtained; e.g. unconscious patient.
    UNAVAILABLE = "unavailable"
    # The work to populate this list has not yet begun.
    NOTSTARTED = "notstarted"
    # This list has now closed or has ceased to be relevant or useful.
    CLOSED = "closed"

    allowed_values = [NILKNOWN, NOTASKED, WITHHELD, UNAVAILABLE, NOTSTARTED, CLOSED]