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

class GraphCompartmentUse(object):
    """ Defines how a compartment rule is used.
    URL: http://hl7.org/fhir/graph-compartment-use
    ValueSet: http://hl7.org/fhir/ValueSet/graph-compartment-use
    """
    """This compartment rule is a condition for whether the rule applies."""
    CONDITION = "condition"
    """This compartment rule is enforced on any relationships that meet the conditions."""
    REQUIREMENT = "requirement"
    allowed_values = ['CONDITION', 'REQUIREMENT']