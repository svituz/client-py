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

class StructureMapModelMode(object):
    """ How the referenced structure is used in this mapping.
    URL: http://hl7.org/fhir/map-model-mode
    ValueSet: http://hl7.org/fhir/ValueSet/map-model-mode
    """
    # This structure describes an instance passed to the mapping engine that is used a source of data.
    source = "source"
    # This structure describes an instance that the mapping engine may ask for that is used a source of data.
    queried = "queried"
    # This structure describes an instance passed to the mapping engine that is used a target of data.
    target = "target"
    # This structure describes an instance that the mapping engine may ask to create that is used a target of data.
    produced = "produced"