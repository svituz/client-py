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

class ExpansionParameterSource(object):
    """ Declares what the source of a parameter is.
    URL: http://terminology.hl7.org/CodeSystem/expansion-parameter-source
    ValueSet: http://hl7.org/fhir/ValueSet/expansion-parameter-source
    """
    """The parameter was supplied by the client in the $expand request."""
    INPUT = "input"
    """The parameter was added by the expansion engine on the server."""
    SERVER = "server"
    """The parameter was added from one the code systems used in the $expand operation."""
    CODESYSTEM = "codesystem"
    allowed_values = ['INPUT', 'SERVER', 'CODESYSTEM']