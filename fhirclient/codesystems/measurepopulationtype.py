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

class MeasurePopulationType(object):
    """ The type of population.
    URL: http://terminology.hl7.org/CodeSystem/measure-population
    ValueSet: http://hl7.org/fhir/ValueSet/measure-population
    """
    # The initial population refers to all patients or events to be evaluated by a quality measure involving patients
    # who share a common set of specified characterstics. All patients or events counted (for example, as numerator,
    # as denominator) are drawn from the initial population.
    INITIALPOPULATION = "initial-population"
    # The upper portion of a fraction used to calculate a rate, proportion, or ratio. Also called the measure focus,
    # it is the target process, condition, event, or outcome. Numerator criteria are the processes or outcomes
    # expected for each patient, or event defined in the denominator. A numerator statement describes the clinical
    # action that satisfies the conditions of the measure.
    NUMERATOR = "numerator"
    # Numerator exclusion criteria define patients or events to be removed from the numerator. Numerator exclusions
    # are used in proportion and ratio measures to help narrow the numerator (for inverted measures).
    NUMERATOREXCLUSION = "numerator-exclusion"
    # The lower portion of a fraction used to calculate a rate, proportion, or ratio. The denominator can be the same
    # as the initial population, or a subset of the initial population to further constrain the population for the
    # purpose of the measure.
    DENOMINATOR = "denominator"
    # Denominator exclusion criteria define patients or events that should be removed from the denominator before
    # determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to
    # help narrow the denominator. For example, patients with bilateral lower extremity amputations would be listed as
    # a denominator exclusion for a measure requiring foot exams.
    DENOMINATOREXCLUSION = "denominator-exclusion"
    # Denominator exceptions are conditions that should remove a patient or event from the denominator of a measure
    # only if the numerator criteria are not met. Denominator exception allows for adjustment of the calculated score
    # for those providers with higher risk populations. Denominator exception criteria are only used in proportion
    # measures.
    DENOMINATOREXCEPTION = "denominator-exception"
    # Measure population criteria define the patients or events for which the individual observation for the measure
    # should be taken. Measure populations are used for continuous variable measures rather than numerator and
    # denominator criteria.
    MEASUREPOPULATION = "measure-population"
    # Measure population criteria define the patients or events that should be removed from the measure population
    # before determining the outcome of one or more continuous variables defined for the measure observation. Measure
    # population exclusion criteria are used within continuous variable measures to help narrow the measure
    # population.
    MEASUREPOPULATIONEXCLUSION = "measure-population-exclusion"
    # Defines the individual observation to be performed for each patient or event in the measure population. Measure
    # observations for each case in the population are aggregated to determine the overall measure score for the
    # population.
    MEASUREOBSERVATION = "measure-observation"

    allowed_values = [INITIALPOPULATION, NUMERATOR, NUMERATOREXCLUSION, DENOMINATOR, DENOMINATOREXCLUSION, DENOMINATOREXCEPTION, MEASUREPOPULATION, MEASUREPOPULATIONEXCLUSION, MEASUREOBSERVATION]