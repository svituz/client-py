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

class ProcedureDeviceActionCodes(object):
    """ Example codes indicating the change that happened to the device during the procedure.  Note that these are in no way
complete and might not even be appropriate for some uses.
    URL: http://hl7.org/fhir/device-action
    """
    # The device was implanted in the patient during the procedure.
    implanted = "implanted"
    # The device was explanted from the patient during the procedure.
    explanted = "explanted"
    # The device remains in the patient, but its location, settings, or functionality was changed.
    manipulated = "manipulated"