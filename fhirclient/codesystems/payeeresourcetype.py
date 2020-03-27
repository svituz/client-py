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

class PayeeResourceType(object):
    """ The type of payee Resource.
    URL: http://terminology.hl7.org/CodeSystem/resource-type-link
    ValueSet: http://hl7.org/fhir/ValueSet/resource-type-link
    """
    """Organization resource."""
    ORGANIZATION = "organization"
    """Patient resource."""
    PATIENT = "patient"
    """Practitioner resource."""
    PRACTITIONER = "practitioner"
    """RelatedPerson resource."""
    RELATEDPERSON = "relatedperson"
    allowed_values = ['ORGANIZATION', 'PATIENT', 'PRACTITIONER', 'RELATEDPERSON']