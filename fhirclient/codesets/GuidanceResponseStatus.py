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

class GuidanceResponseStatus(object):
    """ The status of a guidance response.
    URL: http://hl7.org/fhir/guidance-response-status
    ValueSet: http://hl7.org/fhir/ValueSet/guidance-response-status
    """
    # The request was processed successfully.
    success = "success"
    # The request was processed successfully, but more data may result in a more complete evaluation.
    dataRequested = "data-requested"
    # The request was processed, but more data is required to complete the evaluation.
    dataRequired = "data-required"
    # The request is currently being processed.
    inProgress = "in-progress"
    # The request was not processed successfully.
    failure = "failure"
    # The response was entered in error.
    enteredInError = "entered-in-error"