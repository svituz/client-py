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

class FamilyHistoryAbsentReason(object):
    """ Codes describing the reason why a family member's history is not available.
    URL: http://terminology.hl7.org/CodeSystem/history-absent-reason
    ValueSet: http://hl7.org/fhir/ValueSet/history-absent-reason
    """
    # Patient does not know the subject, e.g. the biological parent of an adopted patient.
    subjectUnknown = "subject-unknown"
    # The patient withheld or refused to share the information.
    withheld = "withheld"
    # Information cannot be obtained; e.g. unconscious patient.
    unableToObtain = "unable-to-obtain"
    # Patient does not have the information now, but can provide the information at a later date.
    deferred = "deferred"