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

class DeviceNameType(object):
    """ The type of name the device is referred by.
    URL: http://hl7.org/fhir/device-nametype
    ValueSet: http://hl7.org/fhir/ValueSet/device-nametype
    """
    # UDI Label name.
    udiLabelName = "udi-label-name"
    # User Friendly name.
    userFriendlyName = "user-friendly-name"
    # Patient Reported name.
    patientReportedName = "patient-reported-name"
    # Manufacturer name.
    manufacturerName = "manufacturer-name"
    # Model name.
    modelName = "model-name"
    # other.
    other = "other"