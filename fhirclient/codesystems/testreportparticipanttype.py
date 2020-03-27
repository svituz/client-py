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

class TestReportParticipantType(object):
    """ The type of participant.
    URL: http://hl7.org/fhir/report-participant-type
    ValueSet: http://hl7.org/fhir/ValueSet/report-participant-type
    """
    """The test execution engine."""
    TESTENGINE = "test-engine"
    """A FHIR Client."""
    CLIENT = "client"
    """A FHIR Server."""
    SERVER = "server"
    allowed_values = ['TESTENGINE', 'CLIENT', 'SERVER']