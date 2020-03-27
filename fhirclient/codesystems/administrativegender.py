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

class AdministrativeGender(object):
    """ The gender of a person used for administrative purposes.
    URL: http://hl7.org/fhir/administrative-gender
    ValueSet: http://hl7.org/fhir/ValueSet/administrative-gender
    """
    """Male."""
    MALE = "male"
    """Female."""
    FEMALE = "female"
    """Other."""
    OTHER = "other"
    """Unknown."""
    UNKNOWN = "unknown"
    allowed_values = ['MALE', 'FEMALE', 'OTHER', 'UNKNOWN']