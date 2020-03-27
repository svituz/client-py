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

class CatalogEntryRelationType(object):
    """ The type of relations between entries.
    URL: http://hl7.org/fhir/relation-type
    ValueSet: http://hl7.org/fhir/ValueSet/relation-type
    """
    # the related entry represents an activity that may be triggered by the current item.
    triggers = "triggers"
    # the related entry represents an item that replaces the current retired item.
    isReplacedBy = "is-replaced-by"