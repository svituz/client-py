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

class ImplantStatus(object):
    """ A set codes that define the functional status of an implanted device.
    URL: http://terminology.hl7.org/CodeSystem/implantStatus
    ValueSet: http://hl7.org/fhir/ValueSet/implantStatus
    """
    # The implanted device is working normally.
    functional = "functional"
    # The implanted device is not working.
    nonFunctional = "non-functional"
    # The implanted device has been turned off.
    disabled = "disabled"
    # the functional status of the implant has not been determined.
    unknown = "unknown"