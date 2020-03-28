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
    UDILABELNAME = "udi-label-name"
    # User Friendly name.
    USERFRIENDLYNAME = "user-friendly-name"
    # Patient Reported name.
    PATIENTREPORTEDNAME = "patient-reported-name"
    # Manufacturer name.
    MANUFACTURERNAME = "manufacturer-name"
    # Model name.
    MODELNAME = "model-name"
    # other.
    OTHER = "other"

    allowed_values = [UDILABELNAME, USERFRIENDLYNAME, PATIENTREPORTEDNAME, MANUFACTURERNAME, MODELNAME, OTHER]