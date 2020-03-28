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

class ExamplePharmacyServiceCodes(object):
    """ This value set includes a smattering of Pharmacy Service codes.
    URL: http://hl7.org/fhir/ex-pharmaservice
    ValueSet: http://hl7.org/fhir/ValueSet/service-pharmacy
    """
    # Smoking cessation
    SMOKECESS = "smokecess"
    # Flu Shot
    FLUSHOT = "flushot"
    # The wholesale price of the medication.
    DRUGCOST = "drugcost"
    # The additional cost assessed on the drug.
    MARKUP = "markup"
    # The professional fee charged for dispensing the product or service.
    DISPENSEFEE = "dispensefee"
    # The professional fee charged for compounding the medication.
    COMPOUNDFEE = "compoundfee"

    allowed_values = [SMOKECESS, FLUSHOT, DRUGCOST, MARKUP, DISPENSEFEE, COMPOUNDFEE]