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

class RejectionCriterion(object):
    """ Criterion for rejection of the specimen by laboratory.
    URL: http://terminology.hl7.org/CodeSystem/rejection-criteria
    ValueSet: http://hl7.org/fhir/ValueSet/rejection-criteria
    """
    """blood specimen hemolized."""
    HEMOLIZED = "hemolized"
    """insufficient quantity of specimen."""
    INSUFFICIENT = "insufficient"
    """specimen container broken."""
    BROKEN = "broken"
    """specimen clotted."""
    CLOTTED = "clotted"
    """specimen temperature inappropriate."""
    WRONGTEMPERATURE = "wrong-temperature"
    allowed_values = ['HEMOLIZED', 'INSUFFICIENT', 'BROKEN', 'CLOTTED', 'WRONGTEMPERATURE']