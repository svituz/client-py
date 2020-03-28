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

class EndpointStatus(object):
    """ The status of the endpoint.
    URL: http://hl7.org/fhir/endpoint-status
    ValueSet: http://hl7.org/fhir/ValueSet/endpoint-status
    """
    # This endpoint is expected to be active and can be used.
    ACTIVE = "active"
    # This endpoint is temporarily unavailable.
    SUSPENDED = "suspended"
    # This endpoint has exceeded connectivity thresholds and is considered in an error state and should no longer be
    # attempted to connect to until corrective action is taken.
    ERROR = "error"
    # This endpoint is no longer to be used.
    OFF = "off"
    # This instance should not have been part of this patient's medical record.
    ENTEREDINERROR = "entered-in-error"
    # This endpoint is not intended for production usage.
    TEST = "test"

    allowed_values = [ACTIVE, SUSPENDED, ERROR, OFF, ENTEREDINERROR, TEST]