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

class ResponseType(object):
    """ The kind of response to a message.
    URL: http://hl7.org/fhir/response-code
    ValueSet: http://hl7.org/fhir/ValueSet/response-code
    """
    # The message was accepted and processed without error.
    OK = "ok"
    # Some internal unexpected error occurred - wait and try again. Note - this is usually used for things like
    # database unavailable, which may be expected to resolve, though human intervention may be required.
    TRANSIENTERROR = "transient-error"
    # The message was rejected because of a problem with the content. There is no point in re-sending without change.
    # The response narrative SHALL describe the issue.
    FATALERROR = "fatal-error"

    allowed_values = [OK, TRANSIENTERROR, FATALERROR]