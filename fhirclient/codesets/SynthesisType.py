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

class SynthesisType(object):
    """ Types of combining results from a body of evidence (eg. summary data meta-analysis).
    URL: http://terminology.hl7.org/CodeSystem/synthesis-type
    ValueSet: http://hl7.org/fhir/ValueSet/synthesis-type
    """
    # A meta-analysis of the summary data of estimates from individual studies or data sets.
    stdMA = "std-MA"
    # A meta-analysis of the individual participant data from individual studies or data sets.
    IPDMA = "IPD-MA"
    # An indirect meta-analysis derived from 2 or more direct comparisons in a network meta-analysis.
    indirectNMA = "indirect-NMA"
    # An composite meta-analysis derived from direct comparisons and indirect comparisons in a network meta-analysis.
    combinedNMA = "combined-NMA"
    # A range of results across a body of evidence.
    range = "range"
    # An approach describing a body of evidence by categorically classifying individual studies (eg 3 studies showed
	/// beneft and 2 studied found no effect).
    classification = "classification"