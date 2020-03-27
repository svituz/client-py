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

class ConceptMapGroupUnmappedMode(object):
    """ Defines which action to take if there is no match in the group.
    URL: http://hl7.org/fhir/conceptmap-unmapped-mode
    ValueSet: http://hl7.org/fhir/ValueSet/conceptmap-unmapped-mode
    """
    # Use the code as provided in the $translate request.
    provided = "provided"
    # Use the code explicitly provided in the group.unmapped.
    fixed = "fixed"
    # Use the map identified by the canonical URL in the url element.
    otherMap = "other-map"