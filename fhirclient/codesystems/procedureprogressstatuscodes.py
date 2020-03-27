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

class ProcedureProgressStatusCodes(object):
    """ This value set is provided as an example. The value set to instantiate this attribute should be drawn from a robust
terminology code system that consists of or contains concepts to support the procedure performance process.
    URL: http://hl7.org/fhir/procedure-progress-status-code
    ValueSet: http://hl7.org/fhir/ValueSet/procedure-progress-status-codes
    """
    """A patient is in the Operating Room."""
    INOPERATINGROOM = "in-operating-room"
    """The patient is prepared for a procedure."""
    PREPARED = "prepared"
    """The patient is under anesthesia."""
    ANESTHESIAINDUCED = "anesthesia-induced"
    """The patient has open incision(s)."""
    OPENINCISION = "open-incision"
    """The patient has incision(s) closed."""
    CLOSEDINCISION = "closed-incision"
    """The patient is in the recovery room."""
    INRECOVERYROOM = "in-recovery-room"
    allowed_values = ['INOPERATINGROOM', 'PREPARED', 'ANESTHESIAINDUCED', 'OPENINCISION', 'CLOSEDINCISION', 'INRECOVERYROOM']