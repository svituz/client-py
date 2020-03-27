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

class DeviceMetricOperationalStatus(object):
    """ Describes the operational status of the DeviceMetric.
    URL: http://hl7.org/fhir/metric-operational-status
    ValueSet: http://hl7.org/fhir/ValueSet/metric-operational-status
    """
    # The DeviceMetric is operating and will generate DeviceObservations.
    on = "on"
    # The DeviceMetric is not operating.
    off = "off"
    # The DeviceMetric is operating, but will not generate any DeviceObservations.
    standby = "standby"
    # The DeviceMetric was entered in error.
    enteredInError = "entered-in-error"