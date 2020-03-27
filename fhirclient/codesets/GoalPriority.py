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

class GoalPriority(object):
    """ Indicates the level of importance associated with reaching or sustaining a goal.
    URL: http://terminology.hl7.org/CodeSystem/goal-priority
    ValueSet: http://hl7.org/fhir/ValueSet/goal-priority
    """
    # Indicates that the goal is of considerable importance and should be a primary focus of care delivery.
    highPriority = "high-priority"
    # Indicates that the goal has a reasonable degree of importance and that concrete action should be taken towards
	/// the goal.  Attainment is not as critical as high-priority goals.
    mediumPriority = "medium-priority"
    # The goal is desirable but is not sufficiently important to devote significant resources to.  Achievement of the
	/// goal may be sought when incidental to achieving other goals.
    lowPriority = "low-priority"