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

class QualityOfEvidenceRating(object):
    """ A rating system that describes the quality of evidence such as the GRADE, DynaMed, or Oxford CEBM systems.
    URL: http://terminology.hl7.org/CodeSystem/evidence-quality
    ValueSet: http://hl7.org/fhir/ValueSet/evidence-quality
    """
    # High quality evidence.
    HIGH = "high"
    # Moderate quality evidence.
    MODERATE = "moderate"
    # Low quality evidence.
    LOW = "low"
    # Very low quality evidence.
    VERYLOW = "very-low"

    allowed_values = [HIGH, MODERATE, LOW, VERYLOW]