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

class RequestPriority(object):
    """ Identifies the level of importance to be assigned to actioning the request.
    URL: http://hl7.org/fhir/request-priority
    ValueSet: http://hl7.org/fhir/ValueSet/request-priority
    """
    """The request has normal priority."""
    ROUTINE = "routine"
    """The request should be actioned promptly - higher priority than routine."""
    URGENT = "urgent"
    """The request should be actioned as soon as possible - higher priority than urgent."""
    ASAP = "asap"
    """The request should be actioned immediately - highest possible priority.  E.g. an emergency."""
    STAT = "stat"
    allowed_values = ['ROUTINE', 'URGENT', 'ASAP', 'STAT']