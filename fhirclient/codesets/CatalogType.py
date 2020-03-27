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

class CatalogType(object):
    """ The type of catalog.
    URL: http://terminology.hl7.org/CodeSystem/catalogType
    ValueSet: http://hl7.org/fhir/ValueSet/catalogType
    """
    # Medication Catalog.
    medication = "medication"
    # Device Catalog.
    device = "device"
    # Protocol List.
    protocol = "protocol"