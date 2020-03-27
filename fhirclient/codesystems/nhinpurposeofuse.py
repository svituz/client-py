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

class NHINPurposeOfUse(object):
    """ This value set is suitable for use with the provenance resource. It is derived from, but not compatible with, the HL7 v3
Purpose of use Code system.
    URL: http://healthit.gov/nhin/purposeofuse
    ValueSet: http://hl7.org/fhir/ValueSet/nhin-purposeofuse
    """
    """Treatment"""
    TREATMENT = "TREATMENT"
    """Payment"""
    PAYMENT = "PAYMENT"
    """Healthcare Operations"""
    OPERATIONS = "OPERATIONS"
    """System Administration"""
    SYSADMIN = "SYSADMIN"
    """Fraud detection"""
    FRAUD = "FRAUD"
    """Use or disclosure of Psychotherapy Notes"""
    PSYCHOTHERAPY = "PSYCHOTHERAPY"
    """Use or disclosure by the covered entity for its own training programs"""
    TRAINING = "TRAINING"
    """Use or disclosure by the covered entity to defend itself in a legal action"""
    LEGAL = "LEGAL"
    """Marketing"""
    MARKETING = "MARKETING"
    """Use and disclosure for facility directories"""
    DIRECTORY = "DIRECTORY"
    """Disclose to a family member, other relative, or a close personal friend of the individual"""
    FAMILY = "FAMILY"
    """Uses and disclosures with the individual present."""
    PRESENT = "PRESENT"
    """Permission cannot practicably be provided because of the individual's incapacity or an emergency."""
    EMERGENCY = "EMERGENCY"
    """Use and disclosures for disaster relief purposes."""
    DISASTER = "DISASTER"
    """Uses and disclosures for public health activities."""
    PUBLICHEALTH = "PUBLICHEALTH"
    """Disclosures about victims of abuse, neglect or domestic violence."""
    ABUSE = "ABUSE"
    """Uses and disclosures for health oversight activities."""
    OVERSIGHT = "OVERSIGHT"
    """Disclosures for judicial and administrative proceedings."""
    JUDICIAL = "JUDICIAL"
    """Disclosures for law enforcement purposes."""
    LAW = "LAW"
    """Uses and disclosures about decedents."""
    DECEASED = "DECEASED"
    """Uses and disclosures for cadaveric organ,  eye or tissue donation purposes"""
    DONATION = "DONATION"
    """Uses and disclosures for research purposes."""
    RESEARCH = "RESEARCH"
    """Uses and disclosures to avert a serious threat to health or safety."""
    THREAT = "THREAT"
    """Uses and disclosures for specialized government functions."""
    GOVERNMENT = "GOVERNMENT"
    """Disclosures for workers' compensation."""
    WORKERSCOMP = "WORKERSCOMP"
    """Disclosures for insurance or disability coverage determination"""
    COVERAGE = "COVERAGE"
    """Request of the Individual"""
    REQUEST = "REQUEST"
    allowed_values = ['TREATMENT', 'PAYMENT', 'OPERATIONS', 'SYSADMIN', 'FRAUD', 'PSYCHOTHERAPY', 'TRAINING', 'LEGAL', 'MARKETING', 'DIRECTORY', 'FAMILY', 'PRESENT', 'EMERGENCY', 'DISASTER', 'PUBLICHEALTH', 'ABUSE', 'OVERSIGHT', 'JUDICIAL', 'LAW', 'DECEASED', 'DONATION', 'RESEARCH', 'THREAT', 'GOVERNMENT', 'WORKERSCOMP', 'COVERAGE', 'REQUEST']