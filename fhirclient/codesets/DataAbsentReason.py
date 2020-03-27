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

class DataAbsentReason(object):
    """ Used to specify why the normally expected content of the data element is missing.
    URL: http://terminology.hl7.org/CodeSystem/data-absent-reason
    ValueSet: http://hl7.org/fhir/ValueSet/data-absent-reason
    """
    # The value is expected to exist but is not known.
    unknown = "unknown"
    # The source was asked but does not know the value.
    askedUnknown = "asked-unknown"
    # There is reason to expect (from the workflow) that the value may become known.
    tempUnknown = "temp-unknown"
    # The workflow didn't lead to this value being known.
    notAsked = "not-asked"
    # The source was asked but declined to answer.
    askedDeclined = "asked-declined"
    # The information is not available due to security, privacy or related reasons.
    masked = "masked"
    # There is no proper value for this element (e.g. last menstrual period for a male).
    notApplicable = "not-applicable"
    # The source system wasn't capable of supporting this element.
    unsupported = "unsupported"
    # The content of the data is represented in the resource narrative.
    asText = "as-text"
    # Some system or workflow process error means that the information is not available.
    error = "error"
    # The numeric value is undefined or unrepresentable due to a floating point processing error.
    notANumber = "not-a-number"
    # The numeric value is excessively low and unrepresentable due to a floating point processing error.
    negativeInfinity = "negative-infinity"
    # The numeric value is excessively high and unrepresentable due to a floating point processing error.
    positiveInfinity = "positive-infinity"
    # The value is not available because the observation procedure (test, etc.) was not performed.
    notPerformed = "not-performed"
    # The value is not permitted in this context (e.g. due to profiles, or the base data types).
    notPermitted = "not-permitted"