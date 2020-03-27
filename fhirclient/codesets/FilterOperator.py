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

class FilterOperator(object):
    """ The kind of operation to perform as a part of a property based filter.
    URL: http://hl7.org/fhir/filter-operator
    ValueSet: http://hl7.org/fhir/ValueSet/filter-operator
    """
    # The specified property of the code equals the provided value.
    eq = "="
    # Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value,
	/// including the provided concept itself (include descendant codes and self).
    isA = "is-a"
    # Includes all concept ids that have a transitive is-a relationship with the concept Id provided as the value,
	/// excluding the provided concept itself i.e. include descendant codes only).
    descendentOf = "descendent-of"
    # The specified property of the code does not have an is-a relationship with the provided value.
    isNotA = "is-not-a"
    # The specified property of the code  matches the regex specified in the provided value.
    regex = "regex"
    # The specified property of the code is in the set of codes or concepts specified in the provided value (comma
	/// separated list).
    in = "in"
    # The specified property of the code is not in the set of codes or concepts specified in the provided value (comma
	/// separated list).
    notIn = "not-in"
    # Includes all concept ids that have a transitive is-a relationship from the concept Id provided as the value,
	/// including the provided concept itself (i.e. include ancestor codes and self).
    generalizes = "generalizes"
    # The specified property of the code has at least one value (if the specified value is true; if the specified
	/// value is false, then matches when the specified property of the code has no values).
    exists = "exists"