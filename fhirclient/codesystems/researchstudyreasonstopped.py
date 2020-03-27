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

class ResearchStudyReasonStopped(object):
    """ Codes for why the study ended prematurely.
    URL: http://terminology.hl7.org/CodeSystem/research-study-reason-stopped
    ValueSet: http://hl7.org/fhir/ValueSet/research-study-reason-stopped
    """
    """The study prematurely ended because the accrual goal was met."""
    ACCRUALGOALMET = "accrual-goal-met"
    """The study prematurely ended due to toxicity."""
    CLOSEDDUETOTOXICITY = "closed-due-to-toxicity"
    """The study prematurely ended due to lack of study progress."""
    CLOSEDDUETOLACKOFSTUDYPROGRESS = "closed-due-to-lack-of-study-progress"
    """The study prematurely ended temporarily per study design."""
    TEMPORARILYCLOSEDPERSTUDYDESIGN = "temporarily-closed-per-study-design"
    allowed_values = ['ACCRUALGOALMET', 'CLOSEDDUETOTOXICITY', 'CLOSEDDUETOLACKOFSTUDYPROGRESS', 'TEMPORARILYCLOSEDPERSTUDYDESIGN']