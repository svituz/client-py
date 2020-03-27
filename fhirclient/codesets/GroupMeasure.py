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

class GroupMeasure(object):
    """ Possible group measure aggregates (E.g. Mean, Median).
    URL: http://hl7.org/fhir/group-measure
    ValueSet: http://hl7.org/fhir/ValueSet/group-measure
    """
    # Aggregated using Mean of participant values.
    mean = "mean"
    # Aggregated using Median of participant values.
    median = "median"
    # Aggregated using Mean of study mean values.
    meanOfMean = "mean-of-mean"
    # Aggregated using Mean of study median values.
    meanOfMedian = "mean-of-median"
    # Aggregated using Median of study mean values.
    medianOfMean = "median-of-mean"
    # Aggregated using Median of study median values.
    medianOfMedian = "median-of-median"