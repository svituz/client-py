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
    productProblem = "product-problem"
    # The adverse event pertains to product quality.
    productQuality = "product-quality"
    # The adverse event pertains to a product use error.
    productUseError = "product-use-error"
    # The adverse event pertains to a wrong dose.
    wrongDose = "wrong-dose"
    # The adverse event pertains to incorrect perscribing information.
    incorrectPrescribingInformation = "incorrect-prescribing-information"
    # The adverse event pertains to a wrong technique.
    wrongTechnique = "wrong-technique"
    # The adverse event pertains to a wrong route of administration.
    wrongRouteOfAdministration = "wrong-route-of-administration"
    # The adverse event pertains to a wrong rate.
    wrongRate = "wrong-rate"
    # The adverse event pertains to a wrong duration.
    wrongDuration = "wrong-duration"
    # The adverse event pertains to a wrong time.
    wrongTime = "wrong-time"
    # The adverse event pertains to an expired drug.
    expiredDrug = "expired-drug"
    # The adverse event pertains to a medical device use error.
    medicalDeviceUseError = "medical-device-use-error"
    # The adverse event pertains to a problem with a different manufacturer of the same medication.
    problemDifferentManufacturer = "problem-different-manufacturer"
    # The adverse event pertains to an unsafe physical environment.
    unsafePhysicalEnvironment = "unsafe-physical-environment"