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

class FinancialResourceStatusCodes(object):
    """ This value set includes Status codes.
    URL: http://hl7.org/fhir/fm-status
    ValueSet: http://hl7.org/fhir/ValueSet/fm-status
    """
    # The instance is currently in-force.
    active = "active"
    # The instance is withdrawn, rescinded or reversed.
    cancelled = "cancelled"
    # A new instance the contents of which is not complete.
    draft = "draft"
    # The instance was entered in error.
    enteredInError = "entered-in-error"