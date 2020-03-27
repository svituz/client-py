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

class SupplyItemType(object):
    """ This value sets refers to a specific supply item.
    URL: http://terminology.hl7.org/CodeSystem/supply-item-type
    ValueSet: http://hl7.org/fhir/ValueSet/supplydelivery-type
    """
    """Supply is a kind of medication."""
    MEDICATION = "medication"
    """What is supplied (or requested) is a device."""
    DEVICE = "device"
    allowed_values = ['MEDICATION', 'DEVICE']