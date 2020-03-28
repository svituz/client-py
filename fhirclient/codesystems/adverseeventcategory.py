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

class AdverseEventCategory(object):
    """ Overall categorization of the event, e.g. product-related or situational.
    URL: http://terminology.hl7.org/CodeSystem/adverse-event-category
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-category
    """
    # The adverse event pertains to a product problem.
    PRODUCTPROBLEM = "product-problem"
    # The adverse event pertains to product quality.
    PRODUCTQUALITY = "product-quality"
    # The adverse event pertains to a product use error.
    PRODUCTUSEERROR = "product-use-error"
    # The adverse event pertains to a wrong dose.
    WRONGDOSE = "wrong-dose"
    # The adverse event pertains to incorrect perscribing information.
    INCORRECTPRESCRIBINGINFORMATION = "incorrect-prescribing-information"
    # The adverse event pertains to a wrong technique.
    WRONGTECHNIQUE = "wrong-technique"
    # The adverse event pertains to a wrong route of administration.
    WRONGROUTEOFADMINISTRATION = "wrong-route-of-administration"
    # The adverse event pertains to a wrong rate.
    WRONGRATE = "wrong-rate"
    # The adverse event pertains to a wrong duration.
    WRONGDURATION = "wrong-duration"
    # The adverse event pertains to a wrong time.
    WRONGTIME = "wrong-time"
    # The adverse event pertains to an expired drug.
    EXPIREDDRUG = "expired-drug"
    # The adverse event pertains to a medical device use error.
    MEDICALDEVICEUSEERROR = "medical-device-use-error"
    # The adverse event pertains to a problem with a different manufacturer of the same medication.
    PROBLEMDIFFERENTMANUFACTURER = "problem-different-manufacturer"
    # The adverse event pertains to an unsafe physical environment.
    UNSAFEPHYSICALENVIRONMENT = "unsafe-physical-environment"

    allowed_values = [PRODUCTPROBLEM, PRODUCTQUALITY, PRODUCTUSEERROR, WRONGDOSE, INCORRECTPRESCRIBINGINFORMATION, WRONGTECHNIQUE, WRONGROUTEOFADMINISTRATION, WRONGRATE, WRONGDURATION, WRONGTIME, EXPIREDDRUG, MEDICALDEVICEUSEERROR, PROBLEMDIFFERENTMANUFACTURER, UNSAFEPHYSICALENVIRONMENT]