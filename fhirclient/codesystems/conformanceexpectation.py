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

class ConformanceExpectation(object):
    """ Indicates the degree of adherence to a specified behavior or capability expected for a system to be deemed conformant
with a specification.
    URL: http://terminology.hl7.org/CodeSystem/conformance-expectation
    ValueSet: http://hl7.org/fhir/ValueSet/conformance-expectation
    """
    # Support for the specified capability is required to be considered conformant.
    SHALL = "SHALL"
    # Support for the specified capability is strongly encouraged, and failure to support it should only occur after
    # careful consideration.
    SHOULD = "SHOULD"
    # Support for the specified capability is not necessary to be considered conformant, and the requirement should be
    # considered strictly optional.
    MAY = "MAY"
    # Support for the specified capability is strongly discouraged and should occur only after careful consideration.
    SHOULDNOT = "SHOULD-NOT"

    allowed_values = [SHALL, SHOULD, MAY, SHOULDNOT]