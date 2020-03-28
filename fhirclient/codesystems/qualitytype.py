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

class QualityType(object):
    """ Type for quality report.
    URL: http://hl7.org/fhir/quality-type
    ValueSet: http://hl7.org/fhir/ValueSet/quality-type
    """
    # INDEL Comparison.
    INDEL = "indel"
    # SNP Comparison.
    SNP = "snp"
    # UNKNOWN Comparison.
    UNKNOWN = "unknown"

    allowed_values = [INDEL, SNP, UNKNOWN]