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

class ResearchSubjectStatus(object):
    """ Indicates the progression of a study subject through a study.
    URL: http://hl7.org/fhir/research-subject-status
    ValueSet: http://hl7.org/fhir/ValueSet/research-subject-status
    """
    """An identified person that can be considered for inclusion in a study."""
    CANDIDATE = "candidate"
    """A person that has met the eligibility criteria for inclusion in a study."""
    ELIGIBLE = "eligible"
    """A person is no longer receiving study intervention and/or being evaluated with tests and procedures according to
	/// the protocol, but they are being monitored on a protocol-prescribed schedule."""
    FOLLOWUP = "follow-up"
    """A person who did not meet one or more criteria required for participation in a study is considered to have
	/// failed screening or
	/// is ineligible for the study."""
    INELIGIBLE = "ineligible"
    """A person for whom registration was not completed."""
    NOTREGISTERED = "not-registered"
    """A person that has ended their participation on a study either because their treatment/observation is complete or
	/// through not
	/// responding, withdrawal, non-compliance and/or adverse event."""
    OFFSTUDY = "off-study"
    """A person that is enrolled or registered on a study."""
    ONSTUDY = "on-study"
    """The person is receiving the treatment or participating in an activity (e.g. yoga, diet, etc.) that the study is
	/// evaluating."""
    ONSTUDYINTERVENTION = "on-study-intervention"
    """The subject is being evaluated via tests and assessments according to the study calendar, but is not receiving
	/// any intervention. Note that this state is study-dependent and might not exist in all studies.  A synonym for
	/// this is "short-term follow-up"."""
    ONSTUDYOBSERVATION = "on-study-observation"
    """A person is pre-registered for a study."""
    PENDINGONSTUDY = "pending-on-study"
    """A person that is potentially eligible for participation in the study."""
    POTENTIALCANDIDATE = "potential-candidate"
    """A person who is being evaluated for eligibility for a study."""
    SCREENING = "screening"
    """The person has withdrawn their participation in the study before registration."""
    WITHDRAWN = "withdrawn"
    allowed_values = ['CANDIDATE', 'ELIGIBLE', 'FOLLOWUP', 'INELIGIBLE', 'NOTREGISTERED', 'OFFSTUDY', 'ONSTUDY', 'ONSTUDYINTERVENTION', 'ONSTUDYOBSERVATION', 'PENDINGONSTUDY', 'POTENTIALCANDIDATE', 'SCREENING', 'WITHDRAWN']