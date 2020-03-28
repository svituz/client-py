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

class SupplyType(object):
    """ This value sets refers to a Category of supply.
    URL: http://terminology.hl7.org/CodeSystem/supply-kind
    ValueSet: http://hl7.org/fhir/ValueSet/supplyrequest-kind
    """
    # Supply is stored and requested from central supply.
    CENTRAL = "central"
    # Supply is not onsite and must be requested from an outside vendor using a non-stock requisition.
    NONSTOCK = "nonstock"

    allowed_values = [CENTRAL, NONSTOCK]