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

class RequestIntent(object):
    """ Codes indicating the degree of authority/intentionality associated with a request.
    URL: http://hl7.org/fhir/request-intent
    ValueSet: http://hl7.org/fhir/ValueSet/request-intent
    """
    # The request is a suggestion made by someone/something that does not have an intention to ensure it occurs and
	/// without providing an authorization to act.
    proposal = "proposal"
    # The request represents an intention to ensure something occurs without providing an authorization for others to
	/// act.
    plan = "plan"
    # The request represents a legally binding instruction authored by a Patient or RelatedPerson.
    directive = "directive"
    # The request represents a request/demand and authorization for action by a Practitioner.
    order = "order"
    # The request represents an original authorization for action.
    originalOrder = "original-order"
    # The request represents an automatically generated supplemental authorization for action based on a parent
	/// authorization together with initial results of the action taken against that parent authorization.
    reflexOrder = "reflex-order"
    # The request represents the view of an authorization instantiated by a fulfilling system representing the details
	/// of the fulfiller's intention to act upon a submitted order.
    fillerOrder = "filler-order"
    # An order created in fulfillment of a broader order that represents the authorization for a single activity
	/// occurrence.  E.g. The administration of a single dose of a drug.
    instanceOrder = "instance-order"
    # The request represents a component or option for a RequestGroup that establishes timing, conditionality and/or
	/// other constraints among a set of requests.  Refer to [[[RequestGroup]]] for additional information on how this
	/// status is used.
    option = "option"