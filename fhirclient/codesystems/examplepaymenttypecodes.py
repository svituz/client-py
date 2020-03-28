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

class ExamplePaymentTypeCodes(object):
    """ This value set includes example Payment Type codes.
    URL: http://terminology.hl7.org/CodeSystem/ex-paymenttype
    ValueSet: http://hl7.org/fhir/ValueSet/ex-paymenttype
    """
    # Complete (final) payment of the benefit under the Claim less any adjustments.
    COMPLETE = "complete"
    # Partial payment of the benefit under the Claim less any adjustments.
    PARTIAL = "partial"

    allowed_values = [COMPLETE, PARTIAL]