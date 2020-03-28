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

class StructureMapInputMode(object):
    """ Mode for this instance of data.
    URL: http://hl7.org/fhir/map-input-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-input-mode
    """
    # Names an input instance used a source for mapping.
    SOURCE = "source"
    # Names an instance that is being populated.
    TARGET = "target"

    allowed_values = [SOURCE, TARGET]