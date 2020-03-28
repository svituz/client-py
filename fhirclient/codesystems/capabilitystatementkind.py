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

class CapabilityStatementKind(object):
    """ How a capability statement is intended to be used.
    URL: http://hl7.org/fhir/capability-statement-kind
    ValueSet: http://hl7.org/fhir/ValueSet/capability-statement-kind
    """
    # The CapabilityStatement instance represents the present capabilities of a specific system instance.  This is the
    # kind returned by /metadata for a FHIR server end-point.
    INSTANCE = "instance"
    # The CapabilityStatement instance represents the capabilities of a system or piece of software, independent of a
    # particular installation.
    CAPABILITY = "capability"
    # The CapabilityStatement instance represents a set of requirements for other systems to meet; e.g. as part of an
    # implementation guide or 'request for proposal'.
    REQUIREMENTS = "requirements"

    allowed_values = [INSTANCE, CAPABILITY, REQUIREMENTS]