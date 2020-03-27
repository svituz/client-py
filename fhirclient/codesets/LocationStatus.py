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

class LocationStatus(object):
    """ Indicates whether the location is still in use.
    URL: http://hl7.org/fhir/location-status
    ValueSet: http://hl7.org/fhir/ValueSet/location-status
    """
    # The location is operational.
    active = "active"
    # The location is temporarily closed.
    suspended = "suspended"
    # The location is no longer used.
    inactive = "inactive"