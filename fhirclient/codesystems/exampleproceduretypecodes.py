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

class ExampleProcedureTypeCodes(object):
    """ This value set includes example Procedure Type codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-procedure-type
    ValueSet: http://hl7.org/fhir/ValueSet/ex-procedure-type
    """
    # The first procedure in a series required to produce and overall patient outcome.
    PRIMARY = "primary"
    # The second procedure in a series required to produce and overall patient outcome.
    SECONDARY = "secondary"

    allowed_values = [PRIMARY, SECONDARY]