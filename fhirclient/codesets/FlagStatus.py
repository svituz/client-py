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

class FlagStatus(object):
    """ Indicates whether this flag is active and needs to be displayed to a user, or whether it is no longer needed or was
entered in error.
    URL: http://hl7.org/fhir/flag-status
    ValueSet: http://hl7.org/fhir/ValueSet/flag-status
    """
    # A current flag that should be displayed to a user. A system may use the category to determine which user roles
	/// should view the flag.
    active = "active"
    # The flag no longer needs to be displayed.
    inactive = "inactive"
    # The flag was added in error and should no longer be displayed.
    enteredInError = "entered-in-error"