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

class TypeDerivationRule(object):
    """ How a type relates to its baseDefinition.
    URL: http://hl7.org/fhir/type-derivation-rule
    ValueSet: http://hl7.org/fhir/ValueSet/type-derivation-rule
    """
    """This definition defines a new type that adds additional elements to the base type."""
    SPECIALIZATION = "specialization"
    """This definition adds additional rules to an existing concrete type."""
    CONSTRAINT = "constraint"
    allowed_values = ['SPECIALIZATION', 'CONSTRAINT']