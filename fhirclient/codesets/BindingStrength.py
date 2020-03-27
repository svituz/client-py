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

class BindingStrength(object):
    """ Indication of the degree of conformance expectations associated with a binding.
    URL: http://hl7.org/fhir/binding-strength
    ValueSet: http://hl7.org/fhir/ValueSet/binding-strength
    """
    # To be conformant, the concept in this element SHALL be from the specified value set.
    required = "required"
    # To be conformant, the concept in this element SHALL be from the specified value set if any of the codes within
	/// the value set can apply to the concept being communicated.  If the value set does not cover the concept (based
	/// on human review), alternate codings (or, data type allowing, text) may be included instead.
    extensible = "extensible"
    # Instances are encouraged to draw from the specified codes for interoperability purposes but are not required to
	/// do so to be considered conformant.
    preferred = "preferred"
    # Instances are not expected or even encouraged to draw from the specified value set.  The value set merely
	/// provides examples of the types of concepts intended to be included.
    example = "example"