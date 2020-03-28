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

class CodeSystemHierarchyMeaning(object):
    """ The meaning of the hierarchy of concepts in a code system.
    URL: http://hl7.org/fhir/codesystem-hierarchy-meaning
    ValueSet: http://hl7.org/fhir/ValueSet/codesystem-hierarchy-meaning
    """
    # No particular relationship between the concepts can be assumed, except what can be determined by inspection of
    # the definitions of the elements (possible reasons to use this: importing from a source where this is not
    # defined, or where various parts of the hierarchy have different meanings).
    GROUPEDBY = "grouped-by"
    # A hierarchy where the child concepts have an IS-A relationship with the parents - that is, all the properties of
    # the parent are also true for its child concepts. Not that is-a is a property of the concepts, so additional
    # subsumption relationships may be defined using properties or the [subsumes](extension-codesystem-subsumes.html)
    # extension.
    ISA = "is-a"
    # Child elements list the individual parts of a composite whole (e.g. body site).
    PARTOF = "part-of"
    # Child concepts in the hierarchy may have only one parent, and there is a presumption that the code system is a
    # "closed world" meaning all things must be in the hierarchy. This results in concepts such as "not otherwise
    # classified.".
    CLASSIFIEDWITH = "classified-with"

    allowed_values = [GROUPEDBY, ISA, PARTOF, CLASSIFIEDWITH]