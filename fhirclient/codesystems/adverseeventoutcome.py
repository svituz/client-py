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

class AdverseEventOutcome(object):
    """ TODO (and should this be required?).
    URL: http://terminology.hl7.org/CodeSystem/adverse-event-outcome
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-outcome
    """
    """resolved"""
    RESOLVED = "resolved"
    """recovering"""
    RECOVERING = "recovering"
    """ongoing"""
    ONGOING = "ongoing"
    """resolvedWithSequelae"""
    RESOLVEDWITHSEQUELAE = "resolvedWithSequelae"
    """fatal"""
    FATAL = "fatal"
    """unknown"""
    UNKNOWN = "unknown"
    allowed_values = ['RESOLVED', 'RECOVERING', 'ONGOING', 'RESOLVEDWITHSEQUELAE', 'FATAL', 'UNKNOWN']