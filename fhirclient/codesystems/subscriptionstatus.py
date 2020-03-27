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

class SubscriptionStatus(object):
    """ The status of a subscription.
    URL: http://hl7.org/fhir/subscription-status
    ValueSet: http://hl7.org/fhir/ValueSet/subscription-status
    """
    """The client has requested the subscription, and the server has not yet set it up."""
    REQUESTED = "requested"
    """The subscription is active."""
    ACTIVE = "active"
    """The server has an error executing the notification."""
    ERROR = "error"
    """Too many errors have occurred or the subscription has expired."""
    OFF = "off"
    allowed_values = ['REQUESTED', 'ACTIVE', 'ERROR', 'OFF']