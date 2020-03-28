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

class BenefitCostApplicability(object):
    """ Whether the cost applies to in-network or out-of-network providers.
    URL: http://terminology.hl7.org/CodeSystem/applicability
    ValueSet: http://hl7.org/fhir/ValueSet/insuranceplan-applicability
    """
    # Provider is contracted with the health insurance company to provide services to plan members for specific pre-
    # negotiated rates
    INNETWORK = "in-network"
    # Provider is  not contracted with the health insurance company to provide services to plan members for specific
    # pre-negotiated rates
    OUTOFNETWORK = "out-of-network"
    # Other applicability
    OTHER = "other"

    allowed_values = [INNETWORK, OUTOFNETWORK, OTHER]