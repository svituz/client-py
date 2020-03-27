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

class DeviceMetricColor(object):
    """ Describes the typical color of representation.
    URL: http://hl7.org/fhir/metric-color
    ValueSet: http://hl7.org/fhir/ValueSet/metric-color
    """
    """Color for representation - black."""
    BLACK = "black"
    """Color for representation - red."""
    RED = "red"
    """Color for representation - green."""
    GREEN = "green"
    """Color for representation - yellow."""
    YELLOW = "yellow"
    """Color for representation - blue."""
    BLUE = "blue"
    """Color for representation - magenta."""
    MAGENTA = "magenta"
    """Color for representation - cyan."""
    CYAN = "cyan"
    """Color for representation - white."""
    WHITE = "white"
    allowed_values = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']