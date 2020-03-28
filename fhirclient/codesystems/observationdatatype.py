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

class ObservationDataType(object):
    """ Permitted data type for observation value.
    URL: http://hl7.org/fhir/permitted-data-type
    ValueSet: http://hl7.org/fhir/ValueSet/permitted-data-type
    """
    # A measured amount.
    QUANTITY = "Quantity"
    # A coded concept from a reference terminology and/or text.
    CODEABLECONCEPT = "CodeableConcept"
    # A sequence of Unicode characters.
    STRING = "string"
    # true or false.
    BOOLEAN = "boolean"
    # A signed integer.
    INTEGER = "integer"
    # A set of values bounded by low and high.
    RANGE = "Range"
    # A ratio of two Quantity values - a numerator and a denominator.
    RATIO = "Ratio"
    # A series of measurements taken by a device.
    SAMPLEDDATA = "SampledData"
    # A time during the day, in the format hh:mm:ss.
    TIME = "time"
    # A date, date-time or partial date (e.g. just year or year + month) as used in human communication.
    DATETIME = "dateTime"
    # A time range defined by start and end date/time.
    PERIOD = "Period"

    allowed_values = [QUANTITY, CODEABLECONCEPT, STRING, BOOLEAN, INTEGER, RANGE, RATIO, SAMPLEDDATA, TIME, DATETIME, PERIOD]