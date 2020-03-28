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

class OrientationType(object):
    """ Type for orientation.
    URL: http://hl7.org/fhir/orientation-type
    ValueSet: http://hl7.org/fhir/ValueSet/orientation-type
    """
    # Sense orientation of reference sequence.
    SENSE = "sense"
    # Antisense orientation of reference sequence.
    ANTISENSE = "antisense"

    allowed_values = [SENSE, ANTISENSE]