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

class NarrativeStatus(object):
    """ The status of a resource narrative.
    URL: http://hl7.org/fhir/narrative-status
    ValueSet: http://hl7.org/fhir/ValueSet/narrative-status
    """
    """The contents of the narrative are entirely generated from the core elements in the content."""
    GENERATED = "generated"
    """The contents of the narrative are entirely generated from the core elements in the content and some of the
	/// content is generated from extensions. The narrative SHALL reflect the impact of all modifier extensions."""
    EXTENSIONS = "extensions"
    """The contents of the narrative may contain additional information not found in the structured data. Note that
	/// there is no computable way to determine what the extra information is, other than by human inspection."""
    ADDITIONAL = "additional"
    """The contents of the narrative are some equivalent of "No human-readable text provided in this case"."""
    EMPTY = "empty"
    allowed_values = ['GENERATED', 'EXTENSIONS', 'ADDITIONAL', 'EMPTY']