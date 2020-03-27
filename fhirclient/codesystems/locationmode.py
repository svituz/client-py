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

class LocationMode(object):
    """ Indicates whether a resource instance represents a specific location or a class of locations.
    URL: http://hl7.org/fhir/location-mode
    ValueSet: http://hl7.org/fhir/ValueSet/location-mode
    """
    """The Location resource represents a specific instance of a location (e.g. Operating Theatre 1A)."""
    INSTANCE = "instance"
    """The Location represents a class of locations (e.g. Any Operating Theatre) although this class of locations could
	/// be constrained within a specific boundary (such as organization, or parent location, address etc.)."""
    KIND = "kind"
    allowed_values = ['INSTANCE', 'KIND']