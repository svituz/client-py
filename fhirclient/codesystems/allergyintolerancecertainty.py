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

class AllergyIntoleranceCertainty(object):
    """ Statement about the degree of clinical certainty that a specific substance was the cause of the manifestation in a
reaction event.
    URL: http://terminology.hl7.org/CodeSystem/reaction-event-certainty
    ValueSet: http://hl7.org/fhir/ValueSet/reaction-event-certainty
    """
    # There is a low level of clinical certainty that the reaction was caused by the identified substance.
    UNLIKELY = "unlikely"
    # There is a high level of clinical certainty that the reaction was caused by the identified substance.
    LIKELY = "likely"
    # There is a very high level of clinical certainty that the reaction was due to the identified substance, which
    # may include clinical evidence by testing or rechallenge.
    CONFIRMED = "confirmed"
    # The clinical certainty that the reaction was caused by the identified substance is unknown.  It is an explicit
    # assertion that certainty is not known.
    UNKNOWN = "unknown"

    allowed_values = [UNLIKELY, LIKELY, CONFIRMED, UNKNOWN]