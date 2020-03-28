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

class AdjudicationValueCodes(object):
    """ This value set includes a smattering of Adjudication Value codes which includes codes to indicate the amounts eligible
under the plan, the amount of benefit, copays etc.
    URL: http://terminology.hl7.org/CodeSystem/adjudication
    ValueSet: http://hl7.org/fhir/ValueSet/adjudication
    """
    # The total submitted amount for the claim or group or line item.
    SUBMITTED = "submitted"
    # Patient Co-Payment
    COPAY = "copay"
    # Amount of the change which is considered for adjudication.
    ELIGIBLE = "eligible"
    # Amount deducted from the eligible amount prior to adjudication.
    DEDUCTIBLE = "deductible"
    # The amount of deductible which could not allocated to other line items.
    UNALLOCDEDUCT = "unallocdeduct"
    # Eligible Percentage.
    ELIGPERCENT = "eligpercent"
    # The amount of tax.
    TAX = "tax"
    # Amount payable under the coverage
    BENEFIT = "benefit"

    allowed_values = [SUBMITTED, COPAY, ELIGIBLE, DEDUCTIBLE, UNALLOCDEDUCT, ELIGPERCENT, TAX, BENEFIT]