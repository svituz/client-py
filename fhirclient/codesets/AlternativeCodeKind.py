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

class AlternativeCodeKind(object):
    """ Indicates the type of use for which the code is defined.
    URL: http://terminology.hl7.org/CodeSystem/codesystem-altcode-kind
    ValueSet: http://hl7.org/fhir/ValueSet/codesystem-altcode-kind
    """
    # The code is an alternative code that can be used in any of the circumstances that the primary code can be used.
    alternate = "alternate"
    # The code should no longer be used, but was used in the past.
    deprecated = "deprecated"
    # The code is an alternative to be used when a case insensitive code is required (when the primary codes are case
	/// sensitive).
    caseInsensitive = "case-insensitive"
    # The code is an alternative to be used when a case sensitive code is required (when the primary codes are case
	/// insensitive).
    caseSensitive = "case-sensitive"
    # The code is an alternative for the primary code that is built using the expression grammar defined by the code
	/// system.
    expression = "expression"