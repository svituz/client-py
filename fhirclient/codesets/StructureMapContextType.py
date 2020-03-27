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

class StructureMapContextType(object):
    """ How to interpret the context.
    URL: http://hl7.org/fhir/map-context-type
    ValueSet: http://hl7.org/fhir/ValueSet/map-context-type
    """
    # The context specifies a type.
    type = "type"
    # The context specifies a variable.
    variable = "variable"