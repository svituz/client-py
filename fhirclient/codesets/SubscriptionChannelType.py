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

class SubscriptionChannelType(object):
    """ The type of method used to execute a subscription.
    URL: http://hl7.org/fhir/subscription-channel-type
    ValueSet: http://hl7.org/fhir/ValueSet/subscription-channel-type
    """
    # The channel is executed by making a post to the URI. If a payload is included, the URL is interpreted as the
	/// service base, and an update (PUT) is made.
    restHook = "rest-hook"
    # The channel is executed by sending a packet across a web socket connection maintained by the client. The URL
	/// identifies the websocket, and the client binds to this URL.
    websocket = "websocket"
    # The channel is executed by sending an email to the email addressed in the URI (which must be a mailto:).
    email = "email"
    # The channel is executed by sending an SMS message to the phone number identified in the URL (tel:).
    sms = "sms"
    # The channel is executed by sending a message (e.g. a Bundle with a MessageHeader resource etc.) to the
	/// application identified in the URI.
    message = "message"