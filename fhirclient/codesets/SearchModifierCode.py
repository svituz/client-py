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

class SearchModifierCode(object):
    """ A supported modifier for a search parameter.
    URL: http://hl7.org/fhir/search-modifier-code
    ValueSet: http://hl7.org/fhir/ValueSet/search-modifier-code
    """
    # The search parameter returns resources that have a value or not.
    missing = "missing"
    # The search parameter returns resources that have a value that exactly matches the supplied parameter (the whole
	/// string, including casing and accents).
    exact = "exact"
    # The search parameter returns resources that include the supplied parameter value anywhere within the field being
	/// searched.
    contains = "contains"
    # The search parameter returns resources that do not contain a match.
    not = "not"
    # The search parameter is processed as a string that searches text associated with the code/value - either
	/// CodeableConcept.text, Coding.display, or Identifier.type.text.
    text = "text"
    # The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests
	/// whether the coding is in the specified value set.
    in = "in"
    # The search parameter is a URI (relative or absolute) that identifies a value set, and the search parameter tests
	/// whether the coding is not in the specified value set.
    notIn = "not-in"
    # The search parameter tests whether the value in a resource is subsumed by the specified value (is-a, or
	/// hierarchical relationships).
    below = "below"
    # The search parameter tests whether the value in a resource subsumes the specified value (is-a, or hierarchical
	/// relationships).
    above = "above"
    # The search parameter only applies to the Resource Type specified as a modifier (e.g. the modifier is not
	/// actually :type, but :Patient etc.).
    type = "type"
    # The search parameter applies to the identifier on the resource, not the reference.
    identifier = "identifier"
    # The search parameter has the format system|code|value, where the system and code refer to an
	/// Identifier.type.coding.system and .code, and match if any of the type codes match. All 3 parts must be present.
    ofType = "ofType"