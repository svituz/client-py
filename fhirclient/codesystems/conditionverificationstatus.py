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

class ConditionVerificationStatus(object):
    """ The verification status to support or decline the clinical status of the condition or diagnosis.
    URL: http://terminology.hl7.org/CodeSystem/condition-ver-status
    ValueSet: http://hl7.org/fhir/ValueSet/condition-ver-status
    """
    """There is not sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition."""
    UNCONFIRMED = "unconfirmed"
    """This is a tentative diagnosis - still a candidate that is under consideration."""
    PROVISIONAL = "provisional"
    """One of a set of potential (and typically mutually exclusive) diagnoses asserted to further guide the diagnostic
	/// process and preliminary treatment."""
    DIFFERENTIAL = "differential"
    """There is sufficient diagnostic and/or clinical evidence to treat this as a confirmed condition."""
    CONFIRMED = "confirmed"
    """This condition has been ruled out by diagnostic and clinical evidence."""
    REFUTED = "refuted"
    """The statement was entered in error and is not valid."""
    ENTEREDINERROR = "entered-in-error"
    allowed_values = ['UNCONFIRMED', 'PROVISIONAL', 'DIFFERENTIAL', 'CONFIRMED', 'REFUTED', 'ENTEREDINERROR']