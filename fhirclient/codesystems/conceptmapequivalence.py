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

class ConceptMapEquivalence(object):
    """ The degree of equivalence between concepts.
    URL: http://hl7.org/fhir/concept-map-equivalence
    ValueSet: http://hl7.org/fhir/ValueSet/concept-map-equivalence
    """
    # The concepts are related to each other, and have at least some overlap in meaning, but the exact relationship is
    # not known.
    RELATEDTO = "relatedto"
    # The definitions of the concepts mean the same thing (including when structural implications of meaning are
    # considered) (i.e. extensionally identical).
    EQUIVALENT = "equivalent"
    # The definitions of the concepts are exactly the same (i.e. only grammatical differences) and structural
    # implications of meaning are identical or irrelevant (i.e. intentionally identical).
    EQUAL = "equal"
    # The target mapping is wider in meaning than the source concept.
    WIDER = "wider"
    # The target mapping subsumes the meaning of the source concept (e.g. the source is-a target).
    SUBSUMES = "subsumes"
    # The target mapping is narrower in meaning than the source concept. The sense in which the mapping is narrower
    # SHALL be described in the comments in this case, and applications should be careful when attempting to use these
    # mappings operationally.
    NARROWER = "narrower"
    # The target mapping specializes the meaning of the source concept (e.g. the target is-a source).
    SPECIALIZES = "specializes"
    # The target mapping overlaps with the source concept, but both source and target cover additional meaning, or the
    # definitions are imprecise and it is uncertain whether they have the same boundaries to their meaning. The sense
    # in which the mapping is inexact SHALL be described in the comments in this case, and applications should be
    # careful when attempting to use these mappings operationally.
    INEXACT = "inexact"
    # There is no match for this concept in the target code system.
    UNMATCHED = "unmatched"
    # This is an explicit assertion that there is no mapping between the source and target concept.
    DISJOINT = "disjoint"

    allowed_values = [RELATEDTO, EQUIVALENT, EQUAL, WIDER, SUBSUMES, NARROWER, SPECIALIZES, INEXACT, UNMATCHED, DISJOINT]