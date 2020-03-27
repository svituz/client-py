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

class ConsentScopeCodes(object):
    """ This value set includes the four Consent scope codes.
    URL: http://terminology.hl7.org/CodeSystem/consentscope
    ValueSet: http://hl7.org/fhir/ValueSet/consent-scope
    """
    """Actions to be taken if they are no longer able to make decisions for themselves"""
    ADR = "adr"
    """Consent to participate in research protocol and information sharing required"""
    RESEARCH = "research"
    """Agreement to collect, access, use or disclose (share) information"""
    PATIENTPRIVACY = "patient-privacy"
    """Consent to undergo a specific treatment"""
    TREATMENT = "treatment"
    allowed_values = ['ADR', 'RESEARCH', 'PATIENTPRIVACY', 'TREATMENT']