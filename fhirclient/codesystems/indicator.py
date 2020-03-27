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

class Indicator(object):
    """ This value set captures the set of indicator codes defined by the CDS Hooks specification.
    URL: http://cds-hooks.hl7.org/CodeSystem/indicator
    ValueSet: http://hl7.org/fhir/ValueSet/cdshooks-indicator
    """
    """info"""
    INFO = "info"
    """warning"""
    WARNING = "warning"
    """critical"""
    CRITICAL = "critical"
    allowed_values = ['INFO', 'WARNING', 'CRITICAL']