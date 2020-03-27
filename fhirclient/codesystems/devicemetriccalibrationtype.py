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

class DeviceMetricCalibrationType(object):
    """ Describes the type of a metric calibration.
    URL: http://hl7.org/fhir/metric-calibration-type
    ValueSet: http://hl7.org/fhir/ValueSet/metric-calibration-type
    """
    """Metric calibration method has not been identified."""
    UNSPECIFIED = "unspecified"
    """Offset metric calibration method."""
    OFFSET = "offset"
    """Gain metric calibration method."""
    GAIN = "gain"
    """Two-point metric calibration method."""
    TWOPOINT = "two-point"
    allowed_values = ['UNSPECIFIED', 'OFFSET', 'GAIN', 'TWOPOINT']