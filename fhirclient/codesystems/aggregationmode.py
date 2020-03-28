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

class AggregationMode(object):
    """ How resource references can be aggregated.
    URL: http://hl7.org/fhir/resource-aggregation-mode
    ValueSet: http://hl7.org/fhir/ValueSet/resource-aggregation-mode
    """
    # The reference is a local reference to a contained resource.
    CONTAINED = "contained"
    # The reference to a resource that has to be resolved externally to the resource that includes the reference.
    REFERENCED = "referenced"
    # The resource the reference points to will be found in the same bundle as the resource that includes the
    # reference.
    BUNDLED = "bundled"

    allowed_values = [CONTAINED, REFERENCED, BUNDLED]