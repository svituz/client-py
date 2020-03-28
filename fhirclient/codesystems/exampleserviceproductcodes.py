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

class ExampleServiceProductCodes(object):
    """ This value set includes a smattering of Service/Product codes.
    URL: http://hl7.org/fhir/ex-serviceproduct
    ValueSet: http://hl7.org/fhir/ValueSet/service-product
    """
    # Exam
    EXAM = "exam"
    # Flu shot
    FLUSHOT = "flushot"

    allowed_values = [EXAM, FLUSHOT]