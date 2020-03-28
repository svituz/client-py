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

class ObservationRangeCategory(object):
    """ Codes identifying the category of observation range.
    URL: http://hl7.org/fhir/observation-range-category
    ValueSet: http://hl7.org/fhir/ValueSet/observation-range-category
    """
    # Reference (Normal) Range for Ordinal and Continuous Observations.
    REFERENCE = "reference"
    # Critical Range for Ordinal and Continuous Observations.
    CRITICAL = "critical"
    # Absolute Range for Ordinal and Continuous Observations. Results outside this range are not possible.
    ABSOLUTE = "absolute"

    allowed_values = [REFERENCE, CRITICAL, ABSOLUTE]