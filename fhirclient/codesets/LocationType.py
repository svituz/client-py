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

class LocationType(object):
    """ This example value set defines a set of codes that can be used to indicate the physical form of the Location.
    URL: http://terminology.hl7.org/CodeSystem/location-physical-type
    ValueSet: http://hl7.org/fhir/ValueSet/location-physical-type
    """
    # A collection of buildings or other locations such as a site or a campus.
    si = "si"
    # Any Building or structure. This may contain rooms, corridors, wings, etc. It might not have walls, or a roof,
	/// but is considered a defined/allocated space.
    bu = "bu"
    # A Wing within a Building, this often contains levels, rooms and corridors.
    wi = "wi"
    # A Ward is a section of a medical facility that may contain rooms and other types of location.
    wa = "wa"
    # A Level in a multi-level Building/Structure.
    lvl = "lvl"
    # Any corridor within a Building, that may connect rooms.
    co = "co"
    # A space that is allocated as a room, it may have walls/roof etc., but does not require these.
    ro = "ro"
    # A space that is allocated for sleeping/laying on. This is not the physical bed/trolley that may be moved about,
	/// but the space it may occupy.
    bd = "bd"
    # A means of transportation.
    ve = "ve"
    # A residential dwelling. Usually used to reference a location that a person/patient may reside.
    ho = "ho"
    # A container that can store goods, equipment, medications or other items.
    ca = "ca"
    # A defined path to travel between 2 points that has a known name.
    rd = "rd"
    # A defined physical boundary of something, such as a flood risk zone, region, postcode
    area = "area"
    # A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government -
	/// e.g. Ministry of Health),  Province or State (community or Government), Business (throughout the enterprise),
	/// Nation with a business scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an
	/// physical boundary
    jdn = "jdn"