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

class MessageSignificanceCategory(object):
    """ The impact of the content of a message.
    URL: http://hl7.org/fhir/message-significance-category
    ValueSet: http://hl7.org/fhir/ValueSet/message-significance-category
    """
    # The message represents/requests a change that should not be processed more than once; e.g., making a booking for
    # an appointment.
    CONSEQUENCE = "consequence"
    # The message represents a response to query for current information. Retrospective processing is wrong and/or
    # wasteful.
    CURRENCY = "currency"
    # The content is not necessarily intended to be current, and it can be reprocessed, though there may be version
    # issues created by processing old notifications.
    NOTIFICATION = "notification"

    allowed_values = [CONSEQUENCE, CURRENCY, NOTIFICATION]