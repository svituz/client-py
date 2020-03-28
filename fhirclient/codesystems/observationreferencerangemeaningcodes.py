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

class ObservationReferenceRangeMeaningCodes(object):
    """ This value set defines a set of codes that can be used to indicate the meaning/use of a reference range for a particular
target population.
    URL: http://terminology.hl7.org/CodeSystem/referencerange-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/referencerange-meaning
    """
    # General types of reference range.
    TYPE = "type"
    # Values expected for a normal member of the relevant control population being measured. Typically each results
    # producer such as a laboratory has specific normal ranges and they are usually defined as within two standard
    # deviations from the mean and account for 95.45% of this population.
    NORMAL = "normal"
    # The range that is recommended by a relevant professional body.
    RECOMMENDED = "recommended"
    # The range at which treatment would/should be considered.
    TREATMENT = "treatment"
    # The optimal range for best therapeutic outcomes.
    THERAPEUTIC = "therapeutic"
    # The optimal range for best therapeutic outcomes for a specimen taken immediately before administration.
    PRE = "pre"
    # The optimal range for best therapeutic outcomes for a specimen taken immediately after administration.
    POST = "post"
    # Endocrine related states that change the expected value.
    ENDOCRINE = "endocrine"
    # An expected range in an individual prior to puberty.
    PREPUBERTY = "pre-puberty"
    # An expected range in an individual during the follicular stage of the cycle.
    FOLLICULAR = "follicular"
    # An expected range in an individual during the midcycle stage of the cycle.
    MIDCYCLE = "midcycle"
    # An expected range in an individual during the luteal stage of the cycle.
    LUTEAL = "luteal"
    # An expected range in an individual post-menopause.
    POSTMENOPAUSAL = "postmenopausal"

    allowed_values = [TYPE, NORMAL, RECOMMENDED, TREATMENT, THERAPEUTIC, PRE, POST, ENDOCRINE, PREPUBERTY, FOLLICULAR, MIDCYCLE, LUTEAL, POSTMENOPAUSAL]