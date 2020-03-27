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

class ConstraintSeverity(object):
    """ SHALL applications comply with this constraint?
    URL: http://hl7.org/fhir/constraint-severity
    ValueSet: http://hl7.org/fhir/ValueSet/constraint-severity
    """
    # If the constraint is violated, the resource is not conformant.
    error = "error"
    # If the constraint is violated, the resource is conformant, but it is not necessarily following best practice.
    warning = "warning"