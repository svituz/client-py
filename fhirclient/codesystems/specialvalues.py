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

class SpecialValues(object):
    """ A set of generally useful codes defined so they can be included in value sets.
    URL: http://terminology.hl7.org/CodeSystem/special-values
    ValueSet: http://hl7.org/fhir/ValueSet/special-values
    """
    """Boolean true."""
    TRUE = "true"
    """Boolean false."""
    FALSE = "false"
    """The content is greater than zero, but too small to be quantified."""
    TRACE = "trace"
    """The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the
	/// bulk of the material."""
    SUFFICIENT = "sufficient"
    """The value is no longer available."""
    WITHDRAWN = "withdrawn"
    """The are no known applicable values in this context."""
    NILKNOWN = "nil-known"
    allowed_values = ['TRUE', 'FALSE', 'TRACE', 'SUFFICIENT', 'WITHDRAWN', 'NILKNOWN']