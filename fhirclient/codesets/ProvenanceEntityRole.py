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

class ProvenanceEntityRole(object):
    """ How an entity was used in an activity.
    URL: http://hl7.org/fhir/provenance-entity-role
    ValueSet: http://hl7.org/fhir/ValueSet/provenance-entity-role
    """
    # A transformation of an entity into another, an update of an entity resulting in a new one, or the construction
	/// of a new entity based on a pre-existing entity.
    derivation = "derivation"
    # A derivation for which the resulting entity is a revised version of some original.
    revision = "revision"
    # The repeat of (some or all of) an entity, such as text or image, by someone who might or might not be its
	/// original author.
    quotation = "quotation"
    # A primary source for a topic refers to something produced by some agent with direct experience and knowledge
	/// about the topic, at the time of the topic's study, without benefit from hindsight.
    source = "source"
    # A derivation for which the entity is removed from accessibility usually through the use of the Delete operation.
    removal = "removal"