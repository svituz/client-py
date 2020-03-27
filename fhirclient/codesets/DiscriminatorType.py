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

class DiscriminatorType(object):
    """ How an element value is interpreted when discrimination is evaluated.
    URL: http://hl7.org/fhir/discriminator-type
    ValueSet: http://hl7.org/fhir/ValueSet/discriminator-type
    """
    # The slices have different values in the nominated element.
    value = "value"
    # The slices are differentiated by the presence or absence of the nominated element.
    exists = "exists"
    # The slices have different values in the nominated element, as determined by testing them against the applicable
	/// ElementDefinition.pattern[x].
    pattern = "pattern"
    # The slices are differentiated by type of the nominated element.
    type = "type"
    # The slices are differentiated by conformance of the nominated element to a specified profile. Note that if the
	/// path specifies .resolve() then the profile is the target profile on the reference. In this case, validation by
	/// the possible profiles is required to differentiate the slices.
    profile = "profile"