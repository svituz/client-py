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

class FHIRSubstanceStatus(object):
    """ A code to indicate if the substance is actively used.
    URL: http://hl7.org/fhir/substance-status
    ValueSet: http://hl7.org/fhir/ValueSet/substance-status
    """
    # The substance is considered for use or reference.
    ACTIVE = "active"
    # The substance is considered for reference, but not for use.
    INACTIVE = "inactive"
    # The substance was entered in error.
    ENTEREDINERROR = "entered-in-error"

    allowed_values = [ACTIVE, INACTIVE, ENTEREDINERROR]