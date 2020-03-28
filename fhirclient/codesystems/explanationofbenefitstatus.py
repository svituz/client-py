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

class ExplanationOfBenefitStatus(object):
    """ A code specifying the state of the resource instance.
    URL: http://hl7.org/fhir/explanationofbenefit-status
    ValueSet: http://hl7.org/fhir/ValueSet/explanationofbenefit-status
    """
    # The resource instance is currently in-force.
    ACTIVE = "active"
    # The resource instance is withdrawn, rescinded or reversed.
    CANCELLED = "cancelled"
    # A new resource instance the contents of which is not complete.
    DRAFT = "draft"
    # The resource instance was entered in error.
    ENTEREDINERROR = "entered-in-error"

    allowed_values = [ACTIVE, CANCELLED, DRAFT, ENTEREDINERROR]