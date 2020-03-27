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

class CompositionAttestationMode(object):
    """ The way in which a person authenticated a composition.
    URL: http://hl7.org/fhir/composition-attestation-mode
    ValueSet: http://hl7.org/fhir/ValueSet/composition-attestation-mode
    """
    """The person authenticated the content in their personal capacity."""
    PERSONAL = "personal"
    """The person authenticated the content in their professional capacity."""
    PROFESSIONAL = "professional"
    """The person authenticated the content and accepted legal responsibility for its content."""
    LEGAL = "legal"
    """The organization authenticated the content as consistent with their policies and procedures."""
    OFFICIAL = "official"
    allowed_values = ['PERSONAL', 'PROFESSIONAL', 'LEGAL', 'OFFICIAL']