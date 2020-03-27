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

class ConditionalDeleteStatus(object):
    """ A code that indicates how the server supports conditional delete.
    URL: http://hl7.org/fhir/conditional-delete-status
    ValueSet: http://hl7.org/fhir/ValueSet/conditional-delete-status
    """
    """No support for conditional deletes."""
    NOTSUPPORTED = "not-supported"
    """Conditional deletes are supported, but only single resources at a time."""
    SINGLE = "single"
    """Conditional deletes are supported, and multiple resources can be deleted in a single interaction."""
    MULTIPLE = "multiple"
    allowed_values = ['NOTSUPPORTED', 'SINGLE', 'MULTIPLE']