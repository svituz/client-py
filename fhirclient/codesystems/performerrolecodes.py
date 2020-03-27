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

class PerformerRoleCodes(object):
    """ This value set includes sample Performer Role codes.
    URL: http://hl7.org/fhir/consentperformer
    ValueSet: http://hl7.org/fhir/ValueSet/consent-performer
    """
    """An entity or an entity's delegatee who is the grantee in an agreement such as a consent for services, advanced
	/// directive, or a privacy consent directive in accordance with jurisdictional, organizational, or patient policy."""
    CONSENTER = "consenter"
    """An entity which accepts certain rights or authority from a grantor."""
    GRANTEE = "grantee"
    """An entity which agrees to confer certain rights or authority to a grantee."""
    GRANTOR = "grantor"
    """A party to whom some right or authority is granted by a delegator."""
    DELEGATEE = "delegatee"
    """A party that grants all or some portion its right or authority to another party."""
    DELEGATOR = "delegator"
    allowed_values = ['CONSENTER', 'GRANTEE', 'GRANTOR', 'DELEGATEE', 'DELEGATOR']