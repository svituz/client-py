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

class MedicationRequestIntent(object):
    """ MedicationRequest Intent Codes
    URL: http://hl7.org/fhir/CodeSystem/medicationrequest-intent
    ValueSet: http://hl7.org/fhir/ValueSet/medicationrequest-intent
    """
    """The request is a suggestion made by someone/something that doesn't have an intention to ensure it occurs and
	/// without providing an authorization to act"""
    PROPOSAL = "proposal"
    """The request represents an intention to ensure something occurs without providing an authorization for others to
	/// act."""
    PLAN = "plan"
    """The request represents a request/demand and authorization for action"""
    ORDER = "order"
    """The request represents the original authorization for the medication request."""
    ORIGINALORDER = "original-order"
    """The request represents an automatically generated supplemental authorization for action based on a parent
	/// authorization together with initial results of the action taken against that parent authorization.."""
    REFLEXORDER = "reflex-order"
    """The request represents the view of an authorization instantiated by a fulfilling system representing the details
	/// of the fulfiller's intention to act upon a submitted order."""
    FILLERORDER = "filler-order"
    """The request represents an instance for the particular order, for example a medication administration record."""
    INSTANCEORDER = "instance-order"
    """The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or
	/// other constraints among a set of requests."""
    OPTION = "option"
    allowed_values = ['PROPOSAL', 'PLAN', 'ORDER', 'ORIGINALORDER', 'REFLEXORDER', 'FILLERORDER', 'INSTANCEORDER', 'OPTION']