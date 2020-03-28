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

class CommunicationCategory(object):
    """ Codes for general categories of communications such as alerts, instructions, etc.
    URL: http://terminology.hl7.org/CodeSystem/communication-category
    ValueSet: http://hl7.org/fhir/ValueSet/communication-category
    """
    # The communication conveys an alert.
    ALERT = "alert"
    # The communication conveys a notification.
    NOTIFICATION = "notification"
    # The communication conveys a reminder.
    REMINDER = "reminder"
    # The communication conveys an instruction.
    INSTRUCTION = "instruction"

    allowed_values = [ALERT, NOTIFICATION, REMINDER, INSTRUCTION]