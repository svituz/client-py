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

class NamingSystemType(object):
    """ Identifies the purpose of the naming system.
    URL: http://hl7.org/fhir/namingsystem-type
    ValueSet: http://hl7.org/fhir/ValueSet/namingsystem-type
    """
    """The naming system is used to define concepts and symbols to represent those concepts; e.g. UCUM, LOINC, NDC
	/// code, local lab codes, etc."""
    CODESYSTEM = "codesystem"
    """The naming system is used to manage identifiers (e.g. license numbers, order numbers, etc.)."""
    IDENTIFIER = "identifier"
    """The naming system is used as the root for other identifiers and naming systems."""
    ROOT = "root"
    allowed_values = ['CODESYSTEM', 'IDENTIFIER', 'ROOT']