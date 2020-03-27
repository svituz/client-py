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

class IdentifierUse(object):
    """ Identifies the purpose for this identifier, if known .
    URL: http://hl7.org/fhir/identifier-use
    ValueSet: http://hl7.org/fhir/ValueSet/identifier-use
    """
    # The identifier recommended for display and use in real-world interactions.
    usual = "usual"
    # The identifier considered to be most trusted for the identification of this item. Sometimes also known as
	/// "primary" and "main". The determination of "official" is subjective and implementation guides often provide
	/// additional guidelines for use.
    official = "official"
    # A temporary identifier.
    temp = "temp"
    # An identifier that was assigned in secondary use - it serves to identify the object in a relative context, but
	/// cannot be consistently assigned to the same object again in a different context.
    secondary = "secondary"
    # The identifier id no longer considered valid, but may be relevant for search purposes.  E.g. Changes to
	/// identifier schemes, account merges, etc.
    old = "old"