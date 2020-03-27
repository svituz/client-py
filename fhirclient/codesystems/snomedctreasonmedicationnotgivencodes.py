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

class SNOMEDCTReasonMedicationNotGivenCodes(object):
    """ This value set includes all medication refused, medication not administered, and non-administration of necessary drug or
medicine codes from SNOMED CT - provided as an exemplar value set.
    URL: http://hl7.org/fhir/reason-medication-not-given
    """
    """No reason known."""
    A = "a"
    """The patient was not available when the dose was scheduled."""
    B = "b"
    """The patient was asleep when the dose was scheduled."""
    C = "c"
    """The patient was given the medication and immediately vomited it back."""
    D = "d"
    allowed_values = ['A', 'B', 'C', 'D']