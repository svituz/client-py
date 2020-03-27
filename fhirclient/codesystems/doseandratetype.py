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

class DoseAndRateType(object):
    """ The kind of dose or rate specified.
    URL: http://terminology.hl7.org/CodeSystem/dose-rate-type
    ValueSet: http://hl7.org/fhir/ValueSet/dose-rate-type
    """
    """The dose specified is calculated by the prescriber or the system."""
    CALCULATED = "calculated"
    """The dose specified is as ordered by the prescriber."""
    ORDERED = "ordered"
    allowed_values = ['CALCULATED', 'ORDERED']