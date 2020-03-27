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

class VisionBase(object):
    """ A coded concept listing the base codes.
    URL: http://hl7.org/fhir/vision-base-codes
    ValueSet: http://hl7.org/fhir/ValueSet/vision-base-codes
    """
    """top."""
    UP = "up"
    """bottom."""
    DOWN = "down"
    """inner edge."""
    IN = "in"
    """outer edge."""
    OUT = "out"
    allowed_values = ['UP', 'DOWN', 'IN', 'OUT']