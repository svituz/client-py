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

class FHIRDeviceStatusReason(object):
    """ The availability status reason of the device.
    URL: http://terminology.hl7.org/CodeSystem/device-status-reason
    ValueSet: http://hl7.org/fhir/ValueSet/device-status-reason
    """
    # The device is off.
    ONLINE = "online"
    # The device is paused.
    PAUSED = "paused"
    # The device is ready but not actively operating.
    STANDBY = "standby"
    # The device is offline.
    OFFLINE = "offline"
    # The device is not ready.
    NOTREADY = "not-ready"
    # The device transducer is disconnected.
    TRANSDUCDISCON = "transduc-discon"
    # The device hardware is disconnected.
    HWDISCON = "hw-discon"
    # The device is off.
    OFF = "off"

    allowed_values = [ONLINE, PAUSED, STANDBY, OFFLINE, NOTREADY, TRANSDUCDISCON, HWDISCON, OFF]