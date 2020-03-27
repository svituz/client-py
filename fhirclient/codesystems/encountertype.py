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

class EncounterType(object):
    """ This example value set defines a set of codes that can be used to indicate the type of encounter: a specific code
indicating type of service provided.
    URL: http://terminology.hl7.org/CodeSystem/encounter-type
    ValueSet: http://hl7.org/fhir/ValueSet/encounter-type
    """
    """ADMS"""
    ADMS = "ADMS"
    """bDBMClin"""
    BDBMCLIN = "BD/BM-clin"
    """CCS60"""
    CCS60 = "CCS60"
    """OKI"""
    OKI = "OKI"
    allowed_values = ['ADMS', 'BDBMCLIN', 'CCS60', 'OKI']