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

class MatchGrade(object):
    """ A Master Patient Index (MPI) assessment of whether a candidate patient record is a match or not.
    URL: http://terminology.hl7.org/CodeSystem/match-grade
    ValueSet: http://hl7.org/fhir/ValueSet/match-grade
    """
    # This record meets the matching criteria to be automatically considered as a full match.
    certain = "certain"
    # This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required
	/// before using this as a match.
    probable = "probable"
    # This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as
	/// a match.
    possible = "possible"
    # This record is known not to be a match. Note that usually non-matching records are not returned, but in some
	/// cases records previously or likely considered as a match may specifically be negated by the matching engine.
    certainlyNot = "certainly-not"