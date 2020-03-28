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

class SubscriptionTag(object):
    """ Tags to put on a resource after subscriptions have been sent.
    URL: http://terminology.hl7.org/CodeSystem/subscription-tag
    ValueSet: http://hl7.org/fhir/ValueSet/subscription-tag
    """
    # The message has been queued for processing on a destination systems.
    QUEUED = "queued"
    # The message has been delivered to its intended recipient.
    DELIVERED = "delivered"

    allowed_values = [QUEUED, DELIVERED]