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

class CompositionStatus(object):
    """ The workflow/clinical status of the composition.
    URL: http://hl7.org/fhir/composition-status
    ValueSet: http://hl7.org/fhir/ValueSet/composition-status
    """
    """This is a preliminary composition or document (also known as initial or interim). The content may be incomplete
	/// or unverified."""
    PRELIMINARY = "preliminary"
    """This version of the composition is complete and verified by an appropriate person and no further work is
	/// planned. Any subsequent updates would be on a new version of the composition."""
    FINAL = "final"
    """The composition content or the referenced resources have been modified (edited or added to) subsequent to being
	/// released as "final" and the composition is complete and verified by an authorized person."""
    AMENDED = "amended"
    """The composition or document was originally created/issued in error, and this is an amendment that marks that the
	/// entire series should not be considered as valid."""
    ENTEREDINERROR = "entered-in-error"
    allowed_values = ['PRELIMINARY', 'FINAL', 'AMENDED', 'ENTEREDINERROR']