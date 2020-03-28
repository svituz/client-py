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

class ConceptSubsumptionOutcome(object):
    """ The subsumption relationship between code/Coding "A" and code/Coding "B". There are 4 possible codes to be returned:
equivalent, subsumes, subsumed-by, and not-subsumed. If the server is unable to determine the relationship between the
codes/Codings, then it returns an error (i.e. an OperationOutcome).
    URL: http://hl7.org/fhir/concept-subsumption-outcome
    ValueSet: http://hl7.org/fhir/ValueSet/concept-subsumption-outcome
    """
    # The two concepts are equivalent (have the same properties).
    EQUIVALENT = "equivalent"
    # Coding/code "A" subsumes Coding/code "B" (e.g. B has all the properties A has, and some of it's own).
    SUBSUMES = "subsumes"
    # Coding/code "A" is subsumed by Coding/code "B" (e.g. A has all the properties B has, and some of it's own).
    SUBSUMEDBY = "subsumed-by"
    # Coding/code "A" and Coding/code "B" are disjoint (e.g. each has propeties that the other doesn't have).
    NOTSUBSUMED = "not-subsumed"

    allowed_values = [EQUIVALENT, SUBSUMES, SUBSUMEDBY, NOTSUBSUMED]