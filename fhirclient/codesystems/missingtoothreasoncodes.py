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

class MissingToothReasonCodes(object):
    """ This value set includes sample Missing Tooth Reason codes.
    URL: http://terminology.hl7.org/CodeSystem/missingtoothreason
    ValueSet: http://hl7.org/fhir/ValueSet/missing-tooth-reason
    """
    # Extraction
    E = "e"
    # Congenital
    C = "c"
    # Unknown
    U = "u"
    # Other
    O = "o"

    allowed_values = [E, C, U, O]