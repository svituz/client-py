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

class AccountStatus(object):
    """ Indicates whether the account is available to be used.
    URL: http://hl7.org/fhir/account-status
    ValueSet: http://hl7.org/fhir/ValueSet/account-status
    """
    """This account is active and may be used."""
    ACTIVE = "active"
    """This account is inactive and should not be used to track financial information."""
    INACTIVE = "inactive"
    """This instance should not have been part of this patient's medical record."""
    ENTEREDINERROR = "entered-in-error"
    """This account is on hold."""
    ONHOLD = "on-hold"
    """The account status is unknown."""
    UNKNOWN = "unknown"
    allowed_values = ['ACTIVE', 'INACTIVE', 'ENTEREDINERROR', 'ONHOLD', 'UNKNOWN']