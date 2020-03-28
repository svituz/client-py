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
    RISKOFBIAS = "RiskOfBias"
    # concerns that findings are not similar enough to support certainty.
    INCONSISTENCY = "Inconsistency"
    # concerns reducing external validity.
    INDIRECTNESS = "Indirectness"
    # High quality evidence.
    IMPRECISION = "Imprecision"
    # likelihood that what is published misrepresents what is available to publish.
    PUBLICATIONBIAS = "PublicationBias"
    # higher certainty due to dose response relationship.
    DOSERESPONSEGRADIENT = "DoseResponseGradient"
    # higher certainty due to risk of bias in opposite direction.
    PLAUSIBLECONFOUNDING = "PlausibleConfounding"
    # higher certainty due to large effect size.
    LARGEEFFECT = "LargeEffect"

    allowed_values = [RISKOFBIAS, INCONSISTENCY, INDIRECTNESS, IMPRECISION, PUBLICATIONBIAS, DOSERESPONSEGRADIENT, PLAUSIBLECONFOUNDING, LARGEEFFECT]