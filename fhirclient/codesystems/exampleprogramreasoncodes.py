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

class ExampleProgramReasonCodes(object):
    """ This value set includes sample Program Reason Span codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-programcode
    ValueSet: http://hl7.org/fhir/ValueSet/ex-program-code
    """
    # Child Asthma Program
    AS = "as"
    # Hemodialysis Program.
    HD = "hd"
    # Autism Screening Program.
    AUSCR = "auscr"
    # No program code applies.
    NONE = "none"

    allowed_values = [AS, HD, AUSCR, NONE]