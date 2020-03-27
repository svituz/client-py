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

class DeviceMetricCalibrationState(object):
    """ Describes the state of a metric calibration.
    URL: http://hl7.org/fhir/metric-calibration-state
    ValueSet: http://hl7.org/fhir/ValueSet/metric-calibration-state
    """
    """The metric has not been calibrated."""
    NOTCALIBRATED = "not-calibrated"
    """The metric needs to be calibrated."""
    CALIBRATIONREQUIRED = "calibration-required"
    """The metric has been calibrated."""
    CALIBRATED = "calibrated"
    """The state of calibration of this metric is unspecified."""
    UNSPECIFIED = "unspecified"
    allowed_values = ['NOTCALIBRATED', 'CALIBRATIONREQUIRED', 'CALIBRATED', 'UNSPECIFIED']