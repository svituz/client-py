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
    DRAFT = "draft"
    # The consent has been proposed but not yet agreed to by all parties. The negotiation stage.
    PROPOSED = "proposed"
    # The consent is to be followed and enforced.
    ACTIVE = "active"
    # The consent has been rejected by one or more of the parties.
    REJECTED = "rejected"
    # The consent is terminated or replaced.
    INACTIVE = "inactive"
    # The consent was created wrongly (e.g. wrong patient) and should be ignored.
    ENTEREDINERROR = "entered-in-error"

    allowed_values = [DRAFT, PROPOSED, ACTIVE, REJECTED, INACTIVE, ENTEREDINERROR]