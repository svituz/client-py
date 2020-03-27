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

class ImmunizationFundingSource(object):
    """ The value set to instantiate this attribute should be drawn from a terminologically robust code system that consists of
or contains concepts to support describing the source of the vaccine administered. This value set is provided as a
suggestive example.
    URL: http://terminology.hl7.org/CodeSystem/immunization-funding-source
    ValueSet: http://hl7.org/fhir/ValueSet/immunization-funding-source
    """
    # The vaccine was purchased with private funds.
    private = "private"
    # The vaccine was purchased with public funds.
    public = "public"