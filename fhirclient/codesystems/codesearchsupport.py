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

class CodeSearchSupport(object):
    """ The degree to which the server supports the code search parameter on ValueSet, if it is supported.
    URL: http://hl7.org/fhir/code-search-support
    ValueSet: http://hl7.org/fhir/ValueSet/code-search-support
    """
    """The search for code on ValueSet only includes codes explicitly detailed on includes or expansions."""
    EXPLICIT = "explicit"
    """The search for code on ValueSet only includes all codes based on the expansion of the value set."""
    ALL = "all"
    allowed_values = ['EXPLICIT', 'ALL']