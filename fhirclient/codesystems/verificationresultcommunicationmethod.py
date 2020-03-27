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

class VerificationresultCommunicationMethod(object):
    """ Attested information may be validated by process that are manual or automated. For automated processes it may
accomplished by the system of record reaching out through another system's API or information may be sent to the system
of record. This value set defines a set of codes to describing the process, the how, a resource or data element is
validated.
    URL: http://terminology.hl7.org/CodeSystem/verificationresult-communication-method
    ValueSet: http://hl7.org/fhir/ValueSet/verificationresult-communication-method
    """
    """The information is submitted/retrieved manually (e.g. by phone, fax, paper-based)"""
    MANUAL = "manual"
    """The information is submitted/retrieved via a portal"""
    PORTAL = "portal"
    """The information is retrieved (i.e. pulled) from a source (e.g. over an API)"""
    PULL = "pull"
    """The information is sent (i.e. pushed) from a source (e.g. over an API, asynchronously, secure messaging)"""
    PUSH = "push"
    allowed_values = ['MANUAL', 'PORTAL', 'PULL', 'PUSH']