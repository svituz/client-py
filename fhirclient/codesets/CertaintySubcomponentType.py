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

class CertaintySubcomponentType(object):
    """ The subcomponent classification of quality of evidence rating systems.
    URL: http://terminology.hl7.org/CodeSystem/certainty-subcomponent-type
    ValueSet: http://hl7.org/fhir/ValueSet/certainty-subcomponent-type
    """
    # methodologic concerns reducing internal validity.
    riskOfBias = "RiskOfBias"
    # concerns that findings are not similar enough to support certainty.
    inconsistency = "Inconsistency"
    # concerns reducing external validity.
    indirectness = "Indirectness"
    # High quality evidence.
    imprecision = "Imprecision"
    # likelihood that what is published misrepresents what is available to publish.
    publicationBias = "PublicationBias"
    # higher certainty due to dose response relationship.
    doseResponseGradient = "DoseResponseGradient"
    # higher certainty due to risk of bias in opposite direction.
    plausibleConfounding = "PlausibleConfounding"
    # higher certainty due to large effect size.
    largeEffect = "LargeEffect"