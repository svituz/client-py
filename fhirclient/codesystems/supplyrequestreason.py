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

class SupplyRequestReason(object):
    """ The reason why the supply item was requested.
    URL: http://terminology.hl7.org/CodeSystem/supplyrequest-reason
    ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-reason
    """
    # The supply has been requested for use in direct patient care.
    PATIENTCARE = "patient-care"
    # The supply has been requested for creating or replenishing ward stock.
    WARDSTOCK = "ward-stock"

    allowed_values = [PATIENTCARE, WARDSTOCK]