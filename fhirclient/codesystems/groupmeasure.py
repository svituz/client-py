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
    """Aggregated using Mean of participant values."""
    MEAN = "mean"
    """Aggregated using Median of participant values."""
    MEDIAN = "median"
    """Aggregated using Mean of study mean values."""
    MEANOFMEAN = "mean-of-mean"
    """Aggregated using Mean of study median values."""
    MEANOFMEDIAN = "mean-of-median"
    """Aggregated using Median of study mean values."""
    MEDIANOFMEAN = "median-of-mean"
    """Aggregated using Median of study median values."""
    MEDIANOFMEDIAN = "median-of-median"
    allowed_values = ['MEAN', 'MEDIAN', 'MEANOFMEAN', 'MEANOFMEDIAN', 'MEDIANOFMEAN', 'MEDIANOFMEDIAN']