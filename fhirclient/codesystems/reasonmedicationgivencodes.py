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

class ReasonMedicationGivenCodes(object):
    """ This value set is provided as an example. The value set to instantiate this attribute should be drawn from a robust
terminology code system that consists of or contains concepts to support the medication process.
    URL: http://terminology.hl7.org/CodeSystem/reason-medication-given
    ValueSet: http://hl7.org/fhir/ValueSet/reason-medication-given-codes
    """
    # No reason known.
    A = "a"
    # The administration was following an ordered protocol.
    B = "b"
    # The administration was needed to treat an emergency.
    C = "c"

    allowed_values = [A, B, C]