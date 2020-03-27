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

class ConsentState(object):
    """ Indicates the state of the consent.
    URL: http://hl7.org/fhir/consent-state-codes
    ValueSet: http://hl7.org/fhir/ValueSet/consent-state-codes
    """
    # The consent is in development or awaiting use but is not yet intended to be acted upon.
    draft = "draft"
    # The consent has been proposed but not yet agreed to by all parties. The negotiation stage.
    proposed = "proposed"
    # The consent is to be followed and enforced.
    active = "active"
    # The consent has been rejected by one or more of the parties.
    rejected = "rejected"
    # The consent is terminated or replaced.
    inactive = "inactive"
    # The consent was created wrongly (e.g. wrong patient) and should be ignored.
    enteredInError = "entered-in-error"