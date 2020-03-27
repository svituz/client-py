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
    quantity = "Quantity"
    # A coded concept from a reference terminology and/or text.
    codeableConcept = "CodeableConcept"
    # A sequence of Unicode characters.
    string = "string"
    # true or false.
    boolean = "boolean"
    # A signed integer.
    integer = "integer"
    # A set of values bounded by low and high.
    range = "Range"
    # A ratio of two Quantity values - a numerator and a denominator.
    ratio = "Ratio"
    # A series of measurements taken by a device.
    sampledData = "SampledData"
    # A time during the day, in the format hh:mm:ss.
    time = "time"
    # A date, date-time or partial date (e.g. just year or year + month) as used in human communication.
    dateTime = "dateTime"
    # A time range defined by start and end date/time.
    period = "Period"