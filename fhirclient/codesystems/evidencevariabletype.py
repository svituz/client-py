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

class EvidenceVariableType(object):
    """ The possible types of variables for exposures or outcomes (E.g. Dichotomous, Continuous, Descriptive).
    URL: http://hl7.org/fhir/variable-type
    ValueSet: http://hl7.org/fhir/ValueSet/variable-type
    """
    """The variable is dichotomous, such as present or absent."""
    DICHOTOMOUS = "dichotomous"
    """The variable is a continuous result such as a quantity."""
    CONTINUOUS = "continuous"
    """The variable is described narratively rather than quantitatively."""
    DESCRIPTIVE = "descriptive"
    allowed_values = ['DICHOTOMOUS', 'CONTINUOUS', 'DESCRIPTIVE']