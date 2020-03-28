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

class FHIRDeviceStatus(object):
    """ The availability status of the device.
    URL: http://hl7.org/fhir/device-status
    ValueSet: http://hl7.org/fhir/ValueSet/device-status
    """
    # The device is available for use.  Note: For *implanted devices*  this means that the device is implanted in the
    # patient.
    ACTIVE = "active"
    # The device is no longer available for use (e.g. lost, expired, damaged).  Note: For *implanted devices*  this
    # means that the device has been removed from the patient.
    INACTIVE = "inactive"
    # The device was entered in error and voided.
    ENTEREDINERROR = "entered-in-error"
    # The status of the device has not been determined.
    UNKNOWN = "unknown"

    allowed_values = [ACTIVE, INACTIVE, ENTEREDINERROR, UNKNOWN]