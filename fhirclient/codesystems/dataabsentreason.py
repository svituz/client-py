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
    UNKNOWN = "unknown"
    # The source was asked but does not know the value.
    ASKEDUNKNOWN = "asked-unknown"
    # There is reason to expect (from the workflow) that the value may become known.
    TEMPUNKNOWN = "temp-unknown"
    # The workflow didn't lead to this value being known.
    NOTASKED = "not-asked"
    # The source was asked but declined to answer.
    ASKEDDECLINED = "asked-declined"
    # The information is not available due to security, privacy or related reasons.
    MASKED = "masked"
    # There is no proper value for this element (e.g. last menstrual period for a male).
    NOTAPPLICABLE = "not-applicable"
    # The source system wasn't capable of supporting this element.
    UNSUPPORTED = "unsupported"
    # The content of the data is represented in the resource narrative.
    ASTEXT = "as-text"
    # Some system or workflow process error means that the information is not available.
    ERROR = "error"
    # The numeric value is undefined or unrepresentable due to a floating point processing error.
    NOTANUMBER = "not-a-number"
    # The numeric value is excessively low and unrepresentable due to a floating point processing error.
    NEGATIVEINFINITY = "negative-infinity"
    # The numeric value is excessively high and unrepresentable due to a floating point processing error.
    POSITIVEINFINITY = "positive-infinity"
    # The value is not available because the observation procedure (test, etc.) was not performed.
    NOTPERFORMED = "not-performed"
    # The value is not permitted in this context (e.g. due to profiles, or the base data types).
    NOTPERMITTED = "not-permitted"

    allowed_values = [UNKNOWN, ASKEDUNKNOWN, TEMPUNKNOWN, NOTASKED, ASKEDDECLINED, MASKED, NOTAPPLICABLE, UNSUPPORTED, ASTEXT, ERROR, NOTANUMBER, NEGATIVEINFINITY, POSITIVEINFINITY, NOTPERFORMED, NOTPERMITTED]