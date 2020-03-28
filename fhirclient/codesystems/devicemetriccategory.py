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

class DeviceMetricCategory(object):
    """ Describes the category of the metric.
    URL: http://hl7.org/fhir/metric-category
    ValueSet: http://hl7.org/fhir/ValueSet/metric-category
    """
    # DeviceObservations generated for this DeviceMetric are measured.
    MEASUREMENT = "measurement"
    # DeviceObservations generated for this DeviceMetric is a setting that will influence the behavior of the Device.
    SETTING = "setting"
    # DeviceObservations generated for this DeviceMetric are calculated.
    CALCULATION = "calculation"
    # The category of this DeviceMetric is unspecified.
    UNSPECIFIED = "unspecified"

    allowed_values = [MEASUREMENT, SETTING, CALCULATION, UNSPECIFIED]