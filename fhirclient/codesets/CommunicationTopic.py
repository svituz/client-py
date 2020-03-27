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

class CommunicationTopic(object):
    """ Codes describing the purpose or content of the communication.
    URL: http://terminology.hl7.org/CodeSystem/communication-topic
    ValueSet: http://hl7.org/fhir/ValueSet/communication-topic
    """
    # The purpose or content of the communication is a prescription refill request.
    prescriptionRefillRequest = "prescription-refill-request"
    # The purpose or content of the communication is a progress update.
    progressUpdate = "progress-update"
    # The purpose or content of the communication is to report labs.
    reportLabs = "report-labs"
    # The purpose or content of the communication is an appointment reminder.
    appointmentReminder = "appointment-reminder"
    # The purpose or content of the communication is a phone consult.
    phoneConsult = "phone-consult"
    # The purpose or content of the communication is a summary report.
    summaryReport = "summary-report"