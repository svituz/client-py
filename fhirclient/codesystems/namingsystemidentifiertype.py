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

class NamingSystemIdentifierType(object):
    """ Identifies the style of unique identifier used to identify a namespace.
    URL: http://hl7.org/fhir/namingsystem-identifier-type
    ValueSet: http://hl7.org/fhir/ValueSet/namingsystem-identifier-type
    """
    """An ISO object identifier; e.g. 1.2.3.4.5."""
    OID = "oid"
    """A universally unique identifier of the form a5afddf4-e880-459b-876e-e4591b0acc11."""
    UUID = "uuid"
    """A uniform resource identifier (ideally a URL - uniform resource locator); e.g. http://unitsofmeasure.org."""
    URI = "uri"
    """Some other type of unique identifier; e.g. HL7-assigned reserved string such as LN for LOINC."""
    OTHER = "other"
    allowed_values = ['OID', 'UUID', 'URI', 'OTHER']