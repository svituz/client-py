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

class GoalRelationshipType(object):
    """ Types of relationships between two goals.
    URL: http://terminology.hl7.org/CodeSystem/goal-relationship-type
    ValueSet: http://hl7.org/fhir/ValueSet/goal-relationship-type
    """
    # Indicates that the target goal is one which must be met before striving for the current goal.
    predecessor = "predecessor"
    # Indicates that the target goal is a desired objective once the current goal is met.
    successor = "successor"
    # Indicates that this goal has been replaced by the target goal.
    replacement = "replacement"
    # Indicates that the target goal is considered to be a "piece" of attaining this goal.
    milestone = "milestone"
    # Indicates that the relationship is not covered by one of the pre-defined codes.  (An extension may convey more
	/// information about the meaning of the relationship.).
    other = "other"