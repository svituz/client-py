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

class ProcessPriorityCodes(object):
    """ This value set includes the financial processing priority codes.
    URL: http://terminology.hl7.org/CodeSystem/processpriority
    ValueSet: http://hl7.org/fhir/ValueSet/process-priority
    """
    # Immediately in real time.
    stat = "stat"
    # With best effort.
    normal = "normal"
    # Later, when possible.
    deferred = "deferred"