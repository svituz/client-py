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

class AuditEventID(object):
    """ Event Types for Audit Events - defined by DICOM with some FHIR specific additions.
    URL: http://terminology.hl7.org/CodeSystem/audit-event-type
    """
    # Audit Event: Execution of a RESTful operation as defined by FHIR.
    rest = "rest"