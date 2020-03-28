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

class ModifierTypeCodes(object):
    """ This value set includes sample Modifier type codes.
    URL: http://terminology.hl7.org/CodeSystem/modifiers
    ValueSet: http://hl7.org/fhir/ValueSet/claim-modifiers
    """
    # Repair of prior service or installation.
    A = "a"
    # Temporary service or installation.
    B = "b"
    # Treatment associated with TMJ.
    C = "c"
    # Implant or associated with an implant.
    E = "e"
    # A Rush service or service performed outside of normal office hours.
    ROOH = "rooh"
    # None.
    X = "x"

    allowed_values = [A, B, C, E, ROOH, X]