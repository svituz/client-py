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

class StudyType(object):
    """ Types of research studies (types of research methods).
    URL: http://terminology.hl7.org/CodeSystem/study-type
    ValueSet: http://hl7.org/fhir/ValueSet/study-type
    """
    # randomized controlled trial.
    RCT = "RCT"
    # controlled (but not randomized) trial.
    CCT = "CCT"
    # observational study comparing cohorts.
    cohort = "cohort"
    # case-control study.
    caseControl = "case-control"
    # uncontrolled cohort or case series.
    series = "series"
    # a single case report.
    caseReport = "case-report"
    # a combination of 1 or more types of studies.
    mixed = "mixed"