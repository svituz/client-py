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
    alert = "alert"
    # The communication conveys a notification.
    notification = "notification"
    # The communication conveys a reminder.
    reminder = "reminder"
    # The communication conveys an instruction.
    instruction = "instruction"