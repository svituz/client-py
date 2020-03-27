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

class GraphCompartmentRule(object):
    """ How a compartment must be linked.
    URL: http://hl7.org/fhir/graph-compartment-rule
    ValueSet: http://hl7.org/fhir/ValueSet/graph-compartment-rule
    """
    """The compartment must be identical (the same literal reference)."""
    IDENTICAL = "identical"
    """The compartment must be the same - the record must be about the same patient, but the reference may be
	/// different."""
    MATCHING = "matching"
    """The compartment must be different."""
    DIFFERENT = "different"
    """The compartment rule is defined in the accompanying FHIRPath expression."""
    CUSTOM = "custom"
    allowed_values = ['IDENTICAL', 'MATCHING', 'DIFFERENT', 'CUSTOM']