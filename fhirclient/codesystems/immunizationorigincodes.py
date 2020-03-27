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

class ImmunizationOriginCodes(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the source of the data when the report of the immunization event is not based
on information from the person, entity or organization who administered the vaccine. This value set is provided as a
suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-origin
    """
    """The data for the immunization event originated with another provider."""
    PROVIDER = "provider"
    """The data for the immunization event originated with a written record for the patient."""
    RECORD = "record"
    """The data for the immunization event originated from the recollection of the patient or parent/guardian of the
	/// patient."""
    RECALL = "recall"
    """The data for the immunization event originated with a school record for the patient."""
    SCHOOL = "school"
    """The data for the immunization event originated with an immunization information system (IIS) or registry
	/// operating within the jurisdiction."""
    JURISDICTION = "jurisdiction"
    allowed_values = ['PROVIDER', 'RECORD', 'RECALL', 'SCHOOL', 'JURISDICTION']