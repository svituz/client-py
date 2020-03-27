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

class HL7Workgroup(object):
    """ An HL7 administrative unit that owns artifacts in the FHIR specification.
    URL: http://terminology.hl7.org/CodeSystem/hl7-work-group
    ValueSet: http://hl7.org/fhir/ValueSet/hl7-work-group
    """
    """Community Based Collaborative Care (http://www.hl7.org/Special/committees/cbcc/index.cfm)."""
    CBCC = "cbcc"
    """Clinical Decision Support (http://www.hl7.org/Special/committees/dss/index.cfm)."""
    CDS = "cds"
    """Clinical Quality Information (http://www.hl7.org/Special/committees/cqi/index.cfm)."""
    CQI = "cqi"
    """Clinical Genomics (http://www.hl7.org/Special/committees/clingenomics/index.cfm)."""
    CG = "cg"
    """Health Care Devices (http://www.hl7.org/Special/committees/healthcaredevices/index.cfm)."""
    DEV = "dev"
    """Electronic Health Records (http://www.hl7.org/special/committees/ehr/index.cfm)."""
    EHR = "ehr"
    """FHIR Infrastructure (http://www.hl7.org/Special/committees/fiwg/index.cfm)."""
    FHIR = "fhir"
    """Financial Management (http://www.hl7.org/Special/committees/fm/index.cfm)."""
    FM = "fm"
    """Health Standards Integration (http://www.hl7.org/Special/committees/hsi/index.cfm)."""
    HSI = "hsi"
    """Imaging Integration (http://www.hl7.org/Special/committees/imagemgt/index.cfm)."""
    II = "ii"
    """Infrastructure And Messaging (http://www.hl7.org/special/committees/inm/index.cfm)."""
    INM = "inm"
    """Implementable Technology Specifications (http://www.hl7.org/special/committees/xml/index.cfm)."""
    ITS = "its"
    """Modeling and Methodology (http://www.hl7.org/Special/committees/mnm/index.cfm)."""
    MNM = "mnm"
    """Orders and Observations (http://www.hl7.org/Special/committees/orders/index.cfm)."""
    OO = "oo"
    """Patient Administration (http://www.hl7.org/Special/committees/pafm/index.cfm)."""
    PA = "pa"
    """Patient Care (http://www.hl7.org/Special/committees/patientcare/index.cfm)."""
    PC = "pc"
    """Public Health and Emergency Response (http://www.hl7.org/Special/committees/pher/index.cfm)."""
    PHER = "pher"
    """Pharmacy (http://www.hl7.org/Special/committees/medication/index.cfm)."""
    PHX = "phx"
    """Biomedical Research and Regulation (http://www.hl7.org/Special/committees/rcrim/index.cfm)."""
    BRR = "brr"
    """Structured Documents (http://www.hl7.org/Special/committees/structure/index.cfm)."""
    SD = "sd"
    """Security (http://www.hl7.org/Special/committees/secure/index.cfm)."""
    SEC = "sec"
    """US Realm Taskforce (http://www.hl7.org/Special/committees/usrealm/index.cfm)."""
    US = "us"
    """Vocabulary (http://www.hl7.org/Special/committees/Vocab/index.cfm)."""
    VOCAB = "vocab"
    """Application Implementation and Design (http://www.hl7.org/Special/committees/java/index.cfm)."""
    AID = "aid"
    allowed_values = ['CBCC', 'CDS', 'CQI', 'CG', 'DEV', 'EHR', 'FHIR', 'FM', 'HSI', 'II', 'INM', 'ITS', 'MNM', 'OO', 'PA', 'PC', 'PHER', 'PHX', 'BRR', 'SD', 'SEC', 'US', 'VOCAB', 'AID']