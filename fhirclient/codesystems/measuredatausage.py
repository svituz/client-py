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

class MeasureDataUsage(object):
    """ The intended usage for supplemental data elements in the measure.
    URL: http://terminology.hl7.org/CodeSystem/measure-data-usage
    ValueSet: http://hl7.org/fhir/ValueSet/measure-data-usage
    """
    """The data is intended to be provided as additional information alongside the measure results."""
    SUPPLEMENTALDATA = "supplemental-data"
    """The data is intended to be used to calculate and apply a risk adjustment model for the measure."""
    RISKADJUSTMENTFACTOR = "risk-adjustment-factor"
    allowed_values = ['SUPPLEMENTALDATA', 'RISKADJUSTMENTFACTOR']