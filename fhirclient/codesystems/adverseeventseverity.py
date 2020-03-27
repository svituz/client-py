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

class AdverseEventSeverity(object):
    """ The severity of the adverse event itself, in direct relation to the subject.
    URL: http://terminology.hl7.org/CodeSystem/adverse-event-severity
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-severity
    """
    """mild"""
    MILD = "mild"
    """moderate"""
    MODERATE = "moderate"
    """severe"""
    SEVERE = "severe"
    allowed_values = ['MILD', 'MODERATE', 'SEVERE']