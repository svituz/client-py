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

class ResearchStudyPrimaryPurposeType(object):
    """ Codes for the main intent of the study.
    URL: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-prim-purp-type
    """
    """One or more interventions are being evaluated for treating a disease, syndrome, or condition."""
    TREATMENT = "treatment"
    """One or more interventions are being assessed for preventing the development of a specific disease or health
	/// condition."""
    PREVENTION = "prevention"
    """One or more interventions are being evaluated for identifying a disease or health condition."""
    DIAGNOSTIC = "diagnostic"
    """One or more interventions are evaluated for maximizing comfort, minimizing side effects, or mitigating against a
	/// decline in the participant's health or function."""
    SUPPORTIVECARE = "supportive-care"
    """One or more interventions are assessed or examined for identifying a condition, or risk factors for a condition,
	/// in people who are not yet known to have the condition or risk factor."""
    SCREENING = "screening"
    """One or more interventions for evaluating the delivery, processes, management, organization, or financing of
	/// healthcare."""
    HEALTHSERVICESRESEARCH = "health-services-research"
    """One or more interventions for examining the basic mechanism of action (for example, physiology or biomechanics
	/// of an intervention)."""
    BASICSCIENCE = "basic-science"
    """An intervention of a device product is being evaluated to determine the feasibility of the product or to test a
	/// prototype device and not health outcomes. Such studies are conducted to confirm the design and operating
	/// specifications of a device before beginning a full clinical trial."""
    DEVICEFEASIBILITY = "device-feasibility"
    allowed_values = ['TREATMENT', 'PREVENTION', 'DIAGNOSTIC', 'SUPPORTIVECARE', 'SCREENING', 'HEALTHSERVICESRESEARCH', 'BASICSCIENCE', 'DEVICEFEASIBILITY']