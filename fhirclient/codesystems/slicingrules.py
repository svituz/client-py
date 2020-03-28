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

class SlicingRules(object):
    """ How slices are interpreted when evaluating an instance.
    URL: http://hl7.org/fhir/resource-slicing-rules
    ValueSet: http://hl7.org/fhir/ValueSet/resource-slicing-rules
    """
    # No additional content is allowed other than that described by the slices in this profile.
    CLOSED = "closed"
    # Additional content is allowed anywhere in the list.
    OPEN = "open"
    # Additional content is allowed, but only at the end of the list. Note that using this requires that the slices be
    # ordered, which makes it hard to share uses. This should only be done where absolutely required.
    OPENATEND = "openAtEnd"

    allowed_values = [CLOSED, OPEN, OPENATEND]