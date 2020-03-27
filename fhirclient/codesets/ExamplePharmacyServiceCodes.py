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
    smokecess = "smokecess"
    # Flu Shot
    flushot = "flushot"
    # The wholesale price of the medication.
    drugcost = "drugcost"
    # The additional cost assessed on the drug.
    markup = "markup"
    # The professional fee charged for dispensing the product or service.
    dispensefee = "dispensefee"
    # The professional fee charged for compounding the medication.
    compoundfee = "compoundfee"