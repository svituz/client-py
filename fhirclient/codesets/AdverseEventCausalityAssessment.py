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

class AdverseEventCausalityAssessment(object):
    """ Codes for the assessment of whether the entity caused the event.
    URL: http://terminology.hl7.org/CodeSystem/adverse-event-causality-assess
    ValueSet: http://hl7.org/fhir/ValueSet/adverse-event-causality-assess
    """
    # i) Event or laboratory test abnormality, with plausible time relationship to drug intake; ii) Cannot be
	/// explained by disease or other drugs; iii) Response to withdrawal plausible (pharmacologically, pathologically);
	/// iv) Event definitive pharmacologically or phenomenologically (i.e. an objective and specific medical disorder or
	/// a recognized pharmacological phenomenon); or v) Re-challenge satisfactory, if necessary.
    certain = "Certain"
    # i) Event or laboratory test abnormality, with reasonable time relationship to drug intake; ii) Unlikely to be
	/// attributed to disease or other drugs; iii) Response to withdrawal clinically reasonable; or iv) Re-challenge not
	/// required.
    probablyLikely = "Probably-Likely"
    # i) Event or laboratory test abnormality, with reasonable time relationship to drug intake; ii) Could also be
	/// explained by disease or other drugs; or iii) Information on drug withdrawal may be lacking or unclear.
    possible = "Possible"
    # i) Event or laboratory test abnormality, with a time to drug intake that makes a relationship improbable (but
	/// not impossible); or ii) Disease or other drugs provide plausible explanations.
    unlikely = "Unlikely"
    # i) Event or laboratory test abnormality; ii) More data for proper assessment needed; or iii) Additional data
	/// under examination.
    conditionalClassified = "Conditional-Classified"
    # i) Report suggesting an adverse reaction; ii) Cannot be judged because information is insufficient or
	/// contradictory; or iii) Data cannot be supplemented or verified.
    unassessableUnclassifiable = "Unassessable-Unclassifiable"