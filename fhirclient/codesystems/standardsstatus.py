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

class StandardsStatus(object):
    """ HL7 Ballot/Standards status of artifact.
    URL: http://terminology.hl7.org/CodeSystem/standards-status
    ValueSet: http://hl7.org/fhir/ValueSet/standards-status
    """
    # This portion of the specification is not considered to be complete enough or sufficiently reviewed to be safe
    # for implementation. It may have known issues or still be in the "in development" stage. It is included in the
    # publication as a place-holder, to solicit feedback from the implementation community and/or to give implementers
    # some insight as to functionality likely to be included in future versions of the specification. Content at this
    # level should only be implemented by the brave or desperate and is very much "use at your own risk". The content
    # that is Draft that will usually be elevated to Trial Use once review and correction is complete after it has
    # been subjected to ballot.
    DRAFT = "draft"
    # This content has been subject to review and production implementation in a wide variety of environments. The
    # content is considered to be stable and has been 'locked', subjecting it to FHIR Inter-version Compatibility
    # Rules. While changes are possible, they are expected to be infrequent and are tightly constrained. Compatibility
    # Rules.
    NORMATIVE = "normative"
    # This content has been well reviewed and is considered by the authors to be ready for use in production systems.
    # It has been subjected to ballot and approved as an official standard. However, it has not yet seen widespread
    # use in production across the full spectrum of environments it is intended to be used in. In some cases, there
    # may be documented known issues that require implementation experience to determine appropriate resolutions for.
    # 
    # Future versions of FHIR may make significant changes to Trial Use content that are not compatible with
    # previously published content.
    TRIALUSE = "trial-use"
    # This portion of the specification is provided for implementer assistance, and does not make rules that
    # implementers are required to follow. Typical examples of this content in the FHIR specification are tables of
    # contents, registries, examples, and implementer advice.
    INFORMATIVE = "informative"
    # This portion of the specification is provided for implementer assistance, and does not make rules that
    # implementers are required to follow. Typical examples of this content in the FHIR specification are tables of
    # contents, registries, examples, and implementer advice.
    DEPRECATED = "deprecated"
    # This is content that is managed outside the FHIR Specification, but included for implementer convenience.
    EXTERNAL = "external"

    allowed_values = [DRAFT, NORMATIVE, TRIALUSE, INFORMATIVE, DEPRECATED, EXTERNAL]