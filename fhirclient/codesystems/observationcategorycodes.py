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

class ObservationCategoryCodes(object):
    """ Codes to denote a guideline or policy statement.when a genetic test result is being shared as a secondary finding.
    URL: http://hl7.org/fhir/secondary-finding
    ValueSet: http://hl7.org/fhir/ValueSet/secondary-finding
    """
    """First release (2013): ACMG Recommendations for Reporting of Incidental Findings in Clinical Exome and Genome
	/// Sequencing.  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3727274/"""
    ACMGVERSION1 = "acmg-version1"
    """Second release (2016): Recommendations for reporting of secondary findings in clinical exome and genome
	/// sequencing, 2016 update (ACMG SF v2.0): a policy statement of the American College of Medical Genetics and
	/// Genomics. https://www.ncbi.nlm.nih.gov/pubmed/27854360"""
    ACMGVERSION2 = "acmg-version2"
    allowed_values = ['ACMGVERSION1', 'ACMGVERSION2']